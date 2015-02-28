#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from kivy.app           import App
from kivy.uix.button    import Button

# class Zepapp(App):
#     def build(self):
#         return Button(text="Olá Zep") # Mostra um botão na janela

# Para usar com zep.kv:
class zepapp(App):
    pass

if __name__ == '__main__':
    zepapp().run() # instancia a classe e roda `run`
