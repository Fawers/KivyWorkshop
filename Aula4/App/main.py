#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from random import shuffle

from kivy.app import App
from kivy.uix.carousel import Carousel


__version__ = '0.2'

class Root(Carousel):
    def __init__(self):
        Carousel.__init__(self)
        from text.dilmes import DILMES
        self.dilmes = DILMES

    def show_text(self, num_of_blocks):
        shuffle(self.dilmes)
        text = '\n\n'.join(self.dilmes[:num_of_blocks])
        self.ids['target_txt'].text = text
        self.load_next()


class DilmesApp(App):
    def build(self):
        self.root = Root()

        return self.root


DilmesApp().run()
