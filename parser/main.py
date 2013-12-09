# -*- coding: utf-8 -*-
from parser import Parser
from saver import Saver
import sys

try:
    url = sys.argv[1]
except IndexError:
    print 'Не передан URL'
    sys.exit()

obj = Parser(url)
text = obj.result()

f = Saver(url)
f.saveFile(text)