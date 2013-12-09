# -*- coding: utf-8 -*-
import os
class Saver:
    def __init__(self, url):
        self.url = url
        self.rootDir = 'result'

    def createDir(self):
        if not os.path.exists(self.rootDir):
            os.makedirs(self.rootDir)
        path = self.url.replace('http://', '').replace('www.', '').split('/')
        path.insert(0, self.rootDir)
        if '' in path: path.remove('')
        filename = path[-1].split('.')[0]
        filename += '.txt'
        path = '/'.join(path[:-1])
        if not os.path.exists(path):
             os.makedirs(path)
        self.filepath = path + '/' + filename
        print self.filepath

    def saveFile(self, text):
        self.createDir()

        f = open(self.filepath, 'w')
        f.write(text)
        f.close()