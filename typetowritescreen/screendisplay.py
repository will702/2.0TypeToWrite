from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
class ScreenDisplay(MDScreen):
    def go_back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = self.parent.current = "screen3"
        self.parent.transition = SlideTransition(direction="left")