from kivy.uix.screenmanager import Screen


from kivy.utils import platform

from kivy.lang import Builder
from . import nulis


# KivyMD imports
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import  MDRaisedButton,MDFlatButton
#Api Imports
from google_trans_new import google_translator
from gingerit.gingerit import GingerIt

# Python imports
import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
import os.path
#Module Import
import glob
folder = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(folder + "/screen1.kv")
Builder.load_file(folder + "/screen2.kv")

Builder.load_file(folder + "/typetowritescreen.kv")

from  screen1 import Screen1
from screen2 import Screen2


class TypeToWriteScreen(Screen):
    try:
        #Put Screen2 On Main Layout

        # def call(self, button):
        #
        #     if button.icon == 'home':
        #         self.change_screen('screen1')
        #     if button.icon == 'notebook':
        #         self.see_recent_images()
        #     if button.icon == 'google':
        #         pass

        def default(self,*args):

            self.ids.screen1.spinn.text = '1' #Make Value To Default
            self.ids.screen1.spinn1.text = '1'#Make Value To Default
            self.dialog2.dismiss()#Close The Dialog
        def grammar_check(self):
            try:
                toast('Wait Indexing Grammar....')



                isi = self.ids.screen1.isi.text
                res = GingerIt().parse(isi)


                print(res)
                self.ids.screen1.isi.text = str(res['result'])
            except:
                pass




        def check_data_login(self):


            self.get_permission()


            try:

                toast('Load Module....')





                nama = self.ids.screen1.username.text

                kelas = self.ids.screen1.kelas.text
                font = self.ids.screen1.spinn.text
                kertas = self.ids.screen1.spinn1.text

                isi = self.ids.screen1.isi.text

                prs = nulis.Fung(isi, kertas, font, nama, kelas)

                prs.textNulis()

                self.ids.screen2.image1.source = prs.return_location()
                self.change_screen('screen2')

            except:
                self.dialog2 = MDDialog(title='No Input ', text='Fill Out The Font and Paper Section',
                                       size_hint=(0.5, 1),
                                       buttons=[MDFlatButton(text='Close', on_release=self.close_dialog2)
                                           , MDRaisedButton(text='Default', on_release=self.default)])


                self.dialog2.open()








        def translation(self):
            try:
                self.get_permission()
                try:

                    toast("Translating...")
                    translator = google_translator()
                    translate_text = translator.translate(self.ids.screen1.isi.text, lang_src='id',
                                                          lang_tgt='en')

                    self.ids.screen1.isi.text = translate_text
                except:
                    pass
            except:
                pass

        def see_recent_images(self):

            self.get_permission()

            if platform == 'android':

                self.list_of_files = glob.glob('/sdcard/DCIM/TypeToWrite/*.png')  # * means all if need specific format then *.csv
                self.latest_file = max(self.list_of_files, key=os.path.getctime)
                self.ids.screen2.image1.source = self.latest_file





        def close_dialog2(self, obj):
            try:
                self.dialog2.dismiss()
            except:
                pass

        def get_permission(self):
            try:
                if platform == 'android':
                    from android.permissions import Permission, request_permissions
                    def callback(permission, results):
                        if all([res for res in results]):
                            pass
                        else:
                            pass

                    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE], callback)
            except:
                pass
        def see_kertas10(self):
            try:
                self.change_screen("screen2")
            except:
                pass

        def see_kertas(self):
            try:
                self.change_screen("screen3")
            except:
                pass


        def back(self):
            try:
                self.change_screen("screen1")
            except:
                pass

        def close_dialog(self, obj):
            try:
                self.dialog.dismiss()
            except:
                pass

        def change_screen(self, screen, *args):
            try:
                self.ids.screen_manager.current = screen
            except:
                pass


    except:
        pass