# -*- coding: utf-8 -*-
"""
TAG_CFG - конфигурация для замены тегов.

SITES - для каждого сайта нужно установить теги, в которых содержаться: заголовок - title, текст - body
Для этих тегов можно дополнительно указать identifier, это либо class, либо id,
через двоеточие значение соответствующего атрибута

Так же можно указать мусорные блоки, которые следует удалить из текста trash:
ключ - имя тега, значение - атрибут:значение, например 'trash': {'div': 'class:vizhimka',}
"""
TAG_CFG = (
    ('a', u'[$href] $text',),
    ('p', u'$text\n',),
)

SITES = {
    'default': {
        'title': {'tag': 'title', 'identifier': ''},
        'body': {'tag': 'div', 'identifier': 'id:text'},
        'trash': {}
    },

    'news-region.com': {
        'title': {'tag': 'div', 'identifier': 'class:node-title'},
        'body': {'tag': 'div', 'identifier': 'class:node-body'},
        'trash': {'div': 'class:vizhimka',}
    },

    'lenta.ru': {
        'title': {'tag': 'h1', 'identifier': ''},
        'body': {'tag': 'div', 'identifier': 'class:b-text'},
        'trash': {
            'div': 'class:b-raw-video-player',
            'aside': '',
        }
    },

    'gazeta.ru': {
        'title': {'tag': 'h1', 'identifier': ''},
        'body': {'tag': 'div', 'identifier': 'class:text'},
        'trash': {
            'div': 'class:cf',
            'div': 'class:incut',
        }
    },
    'newsland.com': {
        'title': {'tag': 'h1', 'identifier': ''},
        'body': {'tag': 'div', 'identifier': 'class:text _reachbanner_ bbtext _ga1_on_'},
        'trash': {
            'h1': '',
            'div': 'class:infoline',

        }
    },
}