# -*- coding: utf-8 -*-
import os

class Theme(object):
    def __init__(self):
        html = open(os.path.dirname(__file__)+'/html/theme.html', 'r').read()
        css  = open(os.path.dirname(__file__)+'/css/style.css', 'r').read()
        self.content = html.replace('{%CSS%}', css )

    def setPersistentData(self, smart, data):
        self.content = self.content.replace('{%'+smart+'%}', data)
        return self.content

    def setData(self, smart, data):
        return self.content.replace('{%'+smart+'%}', data)