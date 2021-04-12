from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
class Screen3(MDScreen):
    def go_back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = self.parent.current = "screen1"
        self.parent.transition = SlideTransition(direction="left")