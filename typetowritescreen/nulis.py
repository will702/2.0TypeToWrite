
import string,random

from PIL import Image, ImageDraw, ImageFont
import os

from kivy.utils import platform
def randoming_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(random.randint(3, 12)))

    return result_str
bhn = {
    'gambar':{
                1:{'nama':'bahan_1.jpg', 'baris': 25, 'perEnter':92, 'samping':347, 'atas':527, "dari":{"atas":320, "samping":170}, "kelas":{"atas":390, "samping":170}}, #succes
                2:{'nama':'bahan_2(1).jpg', 'baris': 25, 'perEnter':104, 'samping':322, 'atas':570, "dari":{"atas":320, "samping":170}, "kelas":{"atas":390, "samping":170}}, #succes
                3:{'nama':'bahan_3.jpg', 'baris': 31, 'perEnter':92, 'samping':280, 'atas':505, "dari":{"atas":270, "samping":130}, "kelas":{"atas":340, "samping":130}}, #succes
                4:{'nama':'bahan_4(3).jpg', 'baris': 31, 'perEnter':95, 'samping':313, 'atas':515, "dari":{"atas":300, "samping":140}, "kelas":{"atas":370, "samping":140}}, #succes
                5:{'nama':'bahan_5.jpg', 'baris': 31, 'perEnter':95, 'samping':325, 'atas':555, "dari":{"atas":320, "samping":150}, "kelas":{"atas":390, "samping":150}} #succes
            },

    'font':{
            1:{'nama':'font1.ttf', 'ukuran':48, 'warna':(49, 50, 50), 'autoEnter':{1:80,2:87,3:88,4:89,5:88}},  #succes
            2:{'nama':'font2.ttf', 'ukuran':67, 'warna':(42, 43, 43), 'autoEnter':{1:74,2:82,3:83,4:83,5:83}},  #succes
            3:{'nama':'font3.ttf', 'ukuran':115, 'warna':(42, 43, 43), 'autoEnter':{1:69,2:74,3:75,4:74,5:74}}  #succes (Premium)
           }
    }


class Fung:


    def __init__(self, fullText, kertas='1', font='1', nama=False, kelas=False):

        self.fullText = fullText
        self.NomorKertas = int(kertas)
        self.NomorFont = int(font)
        self.nama = nama
        self.kelas = kelas



    def textNulis(self): #Proses awal nulis (mengambil font dan kertas)
        self.pilihKertas = bhn['gambar'][self.NomorKertas] #mengambil data kertas dari dictionary bhn
        self.tulisan =  bhn['font'][self.NomorFont] #mengambil data font dari dictionary bhn
        try:

            self.kertas = Image.open('bahan/'+self.pilihKertas['nama'])
            self.d1 = ImageDraw.Draw(self.kertas)
            ukuranFont = self.tulisan['ukuran']

            self.myfont = ImageFont.truetype('bahan/'+self.tulisan['nama'], ukuranFont)

            if self.nama: # jika nama dimasukkan maka tulis nama diatas kertas
                self.d1.text((self.pilihKertas['dari']['samping'],self.pilihKertas['dari']['atas']), 'Nama : '+str(self.nama), font=self.myfont, fill = self.tulisan['warna'])
            if self.kelas: # jika kelas dimasukkan maka tulis kelas diatas kertas
                self.d1.text((self.pilihKertas['kelas']['samping'],self.pilihKertas['kelas']['atas']), 'Kelas : '+str(self.kelas), font=self.myfont, fill = self.tulisan['warna'])

            proces = self.prosesText()
            return proces
        except:
            pass

    def prosesText(self): #proses analisa teks (otamatis enter jika berlebih, dan memecah ke list)
        enter = self.fullText.split('\n') # Membagi text setiap baris (enter)
        jumlahEnter = len(enter)
        if jumlahEnter > self.pilihKertas['baris']: # jika panjang baris melebihi maximal baris pada kertas
            kirim = {'error':True, 'pesan':f"JUMLAH BARIS BERLEBIH\nJumlah Baris anda = {jumlahEnter}\nkami telah memotong secara otomatis \nMaximal Baris pada kertas ini adalah {self.pilihKertas['baris']} baris"}
            return kirim
        else:
            self.textHasil = []
            maxKarakter = self.tulisan['autoEnter'][int(self.NomorKertas)]
            for tt in enter:
                panjangKarakter = len(str(tt))

                while panjangKarakter > maxKarakter: # Jika text melebihi ujung kertas, potong dan letakkan di baris baru
                    self.textHasil.append(tt[:maxKarakter])
                    tt = tt[maxKarakter:]
                    panjangKarakter -= maxKarakter
                else:
                    self.textHasil.append(tt)

            if len(self.textHasil) > self.pilihKertas['baris']:
                kirim = {'error':True, 'pesan':f"JUMLAH BARIS BERLEBIH\nJumlah Baris anda = {len(self.textHasil)}\nMaximal Baris pada kertas ini adalah {self.pilihKertas['baris']} baris"}
                return kirim

            return self.prosesNulis()

    def prosesNulis(self): #proses menempelkan teks ke kertas

        posisiAtas = self.pilihKertas['atas'] # Posisi paling atas untuk menulis di kertas
        awalSamping = self.pilihKertas['samping'] # Posisi samping untuk menulis di kertas

        for num, tt in enumerate(self.textHasil):

            self.d1.text((awalSamping, posisiAtas), tt, font=self.myfont, fill = self.tulisan['warna']) #Menulis Per baris
            posisiAtas += self.pilihKertas['perEnter']


        if platform == 'android':
            self.lokasi = f"/sdcard/DCIM/TypeToWrite/{randoming_string()}typetowrite.png"
            while os.path.exists(self.lokasi) == True:
                self.lokasi = f"/sdcard/DCIM/TypeToWrite/{randoming_string()}typetowrite.png"





            if os.path.exists(f'/sdcard/DCIM/TypeToWrite/') == False:


                os.mkdir('/sdcard/DCIM/TypeToWrite')
                self.kertas.save(self.lokasi)



            if os.path.exists(f'/sdcard/DCIM/TypeToWrite/') == True:
                self.kertas.save(self.lokasi)
        if platform != 'android':
            self.lokasi = f"{randoming_string()}typetowrite.png"
            while os.path.exists(self.lokasi) == True:
                self.lokasi = f"{randoming_string()}typetowrite.png"
            if os.path.exists(self.lokasi) == False:
                self.kertas.save(self.lokasi)







    def return_location(self):
        return self.lokasi










