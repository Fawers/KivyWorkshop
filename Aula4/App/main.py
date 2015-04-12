#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from random import shuffle

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


__version__ = '0.1'

class ScreenTraverserMixin(object):
    def goto_screen(self, number):
        current_screen_name = self.manager.current
        current_screen_number = self.manager.screen_names.index(current_screen_name)
        target_screen_name = self.manager.screen_names[number]

        if current_screen_number < number:
            self.manager.transition.direction = 'left'
        elif number < current_screen_number:
            self.manager.transition.direction = 'right'

        self.manager.current = target_screen_name


class SplashScreen(ScreenTraverserMixin, Screen):
    def __init__(self):
        Screen.__init__(self, **{'name': 'splash'})


class MainScreen(ScreenTraverserMixin, Screen):
    def __init__(self):
        Screen.__init__(self, **{'name': 'main'})
        from text.dilmes import DILMES
        self.dilmes = DILMES

    def get_blocks(self, blocks):
        shuffle(self.dilmes)
        return '\n\n'.join(self.dilmes[:blocks])

    def show_text(self, number):
        txt = self.manager.screens[-1].ids['txt']
        txt.text = self.get_blocks(number)
        self.goto_screen(2)


class TextScreen(ScreenTraverserMixin, Screen):
    def __init__(self):
        Screen.__init__(self, **{'name': 'text'})


class DilmesApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(SplashScreen())
        self.sm.add_widget(MainScreen())
        self.sm.add_widget(TextScreen())

        return self.sm


DilmesApp().run()
