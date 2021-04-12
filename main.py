from kivymd.app import MDApp
from kivy.lang import Builder

from kivmob import KivMob
from kivy.core.window import Window

# Securing Debugable Apps
from kivy.clock import Clock
# Hiding Debugs
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRaisedButton
Window.size = (450, 750)
class OneApp(MDApp):
    def __init__(self):

        super().__init__()
        self.theme_cls.primary_palette =  'LightBlue'
        self.title = 'Type To Write'


    def show_dialog(self):
        try:
            self.dialog = MDDialog(title='LOGOUT', text='Are you sure to log out',
                                   size_hint=(0.5, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)
                                       , MDRaisedButton(text='Sign Out', on_release=self.sign_out)])

            self.dialog.open()
        except:
            pass
    def close_dialog(self,*args):
        self.dialog.dismiss()
    def sign_out(self, obj):
        self.screen.ids.firebaseloginscreen.log_out()
        self.screen.current = "firebaseloginscreen"
        self.dialog.dismiss()
    def loading_screen(self,*args):
        self.screen.ids.firebaseloginscreen.display_loading_screen()
        Clock.schedule_once(self.hide_screen, 0.3)
    def hide_screen(self,*args):
        self.screen.ids.firebaseloginscreen.hide_loading_screen()


    def build(self):

        # Importing config.Config class from config.py


        # Put Banner Ads
        self.ads = KivMob('ca-app-pub-1818238534900904~2025018602')
        # Ads ID
        self.ads.new_banner('ca-app-pub-1818238534900904/4048546717', top_pos=False)
        # Requesting New Ads
        self.ads.request_banner()

        self.ads.show_banner()
        self.screen = Builder.load_file('main.kv')
        self.screen.ids.firebaseloginscreen.web_api_key = "AIzaSyBmrGpiwimYZ-HT_BSesv4gMjuPJcG3omM"
        self.screen.ids.firebaseloginscreen.debug = False
        self.screen.ids.firebaseloginscreen.remember_user = True
        self.screen.ids.firebaseloginscreen.require_email_verification = True
        return self.screen
        # Showing Ads To The Screen




if __name__ == '__main__':
    OneApp().run()

