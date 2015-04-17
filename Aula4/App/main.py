#!/usr/bin/env python2


from random import shuffle

from kivy.app import App
from kivy.base import EventLoop
from kivy.uix.carousel import Carousel


__version__ = '0.3'

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
    def on_start(self):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *args):
        if key == 27:
            if self.root.previous_slide is None:
                exit()
            else:
                self.root.load_previous()
            return True


DilmesApp().run()
