#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from kivy.app import App
from kivy.uix.button import Button

class primeiroApp(App):
    def build(self):
        return Button(text="Sou um botão")

primeiroApp().run()
