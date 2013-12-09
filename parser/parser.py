# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup, Comment, BeautifulStoneSoup
import urllib2
import re
from string import Template
from settings import *

TAG_TEMPLATES = map(lambda x: (x[0], Template(x[1])), TAG_CFG)

class Parser:
    def __init__(self, url):
        self.url = url
        self.getSetings()
        page = urllib2.urlopen(self.url)
        self.soup = BeautifulSoup(''.join(page), convertEntities=BeautifulStoneSoup.HTML_ENTITIES)

    # отдаем результат
    def result(self):
        title = self.title()
        body = self.pageParser()
        return '{title}\n\n{body}'.format(title=title, body = body)

    # обрабатываем текст
    def pageParser(self):
        body = self.body()
        body = self.cleaner(body)
        for tag_name, config in TAG_TEMPLATES:
            self.convert_tags(body, tag_name, config)

        body = re.sub(r'<.+?>', "", body.renderContents())
        return body

    def convert_tags(self, parent, name, config):
        for tag in parent.findAll(name):
            if tag.parent is not None:
                tag.replaceWith(config.safe_substitute(text=tag.renderContents().decode('utf-8'), **dict(tag.attrs)))
        return parent

    # получаем заголовок
    def title(self):
        param = self.settings['title']
        indent = self.indent(param['identifier'])
        try:
            title = self.soup.find(param['tag'],
                {indent[0]: re.compile(indent[1])})
        except IndexError:
            title = self.soup.find(param['tag'])
        title = re.sub(r'<.+?>', "", title.renderContents())
        return title

    # получаем текст
    def body(self):
        param = self.settings['body']
        indent = self.indent(param['identifier'])
        try:
            body = self.soup.find(param['tag'],
                {indent[0]: re.compile(indent[1])})
        except IndexError:
            body = self.soup.find(param['tag'])
        return body

    # чистим от мусора, теги с мусором указаны в настройках trash
    def cleaner(self, body):
        listTrash = self.settings['trash']
        for tag in listTrash:
            indent = self.indent(listTrash[tag])
            try:
                trash = body.findAll(tag, {indent[0]: re.compile(indent[1])})
                if trash:
                    [trh.extract() for trh in trash]
            except IndexError:
                trash = body.findAll(tag)
                if trash:
                    [trh.extract() for trh in trash]
        comments = body.findAll(text=lambda text:isinstance(text, Comment))
        [comment.extract() for comment in comments]
        return body

    # получаем настройки
    def getSetings(self):
        if not 'http://' in self.url: self.url = 'http://' + self.url
        n = self.url.replace('www.', '').split('/')[2]
        try:
            self.settings = SITES[n]
        except KeyError:
            self.settings = SITES['default']

    # разбиваем id/class:name по двоеточию
    def indent(self, txt):
        return txt.split(':')

#тест на 4х сайтах по 10 урлов с каждого
if __name__ == '__main__':
    from saver import Saver
    for line in open('testLink.txt'):
        line = line.rstrip()
        test = Parser(line)
        f = Saver(line)
        f.saveFile(test.result())