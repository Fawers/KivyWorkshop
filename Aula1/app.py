#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from kivy.app           import App
from kivy.uix.button    import Button

class Zepapp(App):
    def build(self):
        return Button(text="Olá Zep") # Mostra um botão na janela

if __name__ == '__main__':
    Zepapp().run() # instancia a classe e roda `run`
