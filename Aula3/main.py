#!/usr/bin/env python2

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MeuWidget(BoxLayout):
    def apply(self, txt):
        num = self.ids.tx_bin.text
        if txt == '-':
            num = num[1:]
        else:
            if txt[1] == '0':
                num = '0' + num
            else:
                num = '1' + num

        self.ids.tx_bin.text = num
        if num:
            self.ids.tx_dec.text = str(int(num, 2))


class SegundoApp(App):
    pass

SegundoApp().run()
