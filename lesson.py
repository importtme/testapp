import datetime
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from kivymd.uix.card import MDCard

from kivymd.uix.snackbar import Snackbar

from kivymd.uix.picker import MDDatePicker

import smtplib as slib
import random

import requests
import sqlite3 as s3

from kivy.uix.image import AsyncImage
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem

from functools import partial
from kivymd.uix.label import MDLabel

import os
from kivy.uix.gridlayout import GridLayout

from kivymd.toast import toast
from kivy.uix.image import Image
import json

Window.softinput_mode = 'pan'

girish = []


class QabSecimi(Screen):
    pass


class ParfumePage(Screen):
    pass


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class SifreDeyis(Screen):
    pass


class ForgetAuthenticationCode(Screen):
    pass


class ForgetPassword(Screen):
    pass


class Profile(Screen):
    pass


class ErrorScreen(Screen):
    pass


class LoadingScreen(Screen):
    pass


class NewName(Screen):
    pass


class QeydiyyatNumEmailPassword(Screen):
    pass


class QeydiyyatAuthenticator(Screen):
    pass


class QabKodu(Screen):
    pass


class Giris(Screen):
    pass


class Qeydiyyat(Screen):
    pass


class GirisVeQeydiyyat(Screen):
    pass


class Etirler(Screen):
    pass


class Axtaris(Screen):
    pass


class Huquqlar(Screen):
    pass


class TestEtir(Screen):
    pass


class BizimBrendimiz(Screen):
    pass


class BizimleElaqe(Screen):
    pass


class MenuScreen(Screen):
    pass


class MarketinqVeQaydalar(Screen):
    pass


class EtirMelumat(Screen):
    pass


class Content(GridLayout):
    pass


class SifarisSehifesi(Screen):
    pass


class IdIste(Screen):
    pass


class IscidiYaYox(Screen):
    pass


class SonSifaris(Screen):
    pass


class CoronaParfumApp(MDApp):
    birinci_miqdar = '10ML'
    ikinci_miqdar = '20ML'
    ucuncu_miqdar = '30ML'
    dorduncu_miqdar = '50ML'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('lesson.kv')
        Window.bind(on_keyboard=self.on_key)
        self.milli = ''
        self.profile = False
        self.ml = 'ML'
        self.idd = ''
        self.dictt = {}
        self.siyahi9 = []
        self.get = requests.get('http://167.86.115.50/product/')
        self.new = json.loads(self.get.text)
        self.qiymet10_son = ''
        self.qiymet20_son = ''
        self.qiymet30_son = ''
        self.qiymet50_son = ''
        for i in self.new:
            self.siyahi9.append(str(i["name"]).lower().capitalize())
        """
        for d in self.new:
            self.dictt["name"] = str(d["name"]).lower().capitalize()
            self.dictt["image"] = d["image"]
            self.dictt["descrption"] = d["descrption"]
            self.dictt["gender"] = d["gender"]
            self.dictt["price_10_ml"] = d["price_10_ml"]
            self.dictt["price_20_ml"] = d["price_20_ml"]
            self.dictt["price_30_ml"] = d["price_30_ml"]
            self.dictt["price_50_ml"] = d["price_50_ml"]
            self.siyahi9.append(str(self.dictt))
            self.dictt.clear()
        """

        self.deyishken = True
        self.adi = ''
        self.cinsi = ''
        self.terkibi = ''
        self.qiymet10 = ''
        self.qiymet20 = ''
        self.qiymet30 = ''
        self.qiymet50 = ''

        for i in self.new:
            self.card = MDCard(orientation='horizontal')

            self.image = AsyncImage(source=f'{i["image"]}')
            self.label1 = MDLabel(text=f'{str(i["name"]).lower().capitalize()}')
            self.label2 = MDLabel(text=f'{str(i["gender"]).capitalize()}', font_size='14sp')
            self.desc = str(i["descrption"])
            self.label3 = MDLabel(
                text=f'10ml-{i["price_10_ml"][:3] if len(i["price_10_ml"]) == 5 else i["price_10_ml"][:2]}₼\n20ml-{i["price_20_ml"][:3] if len(i["price_20_ml"]) == 5 else i["price_20_ml"][:2]}₼\n30ml-{i["price_30_ml"][:3] if len(i["price_30_ml"]) == 5 else i["price_30_ml"][:2]}₼\n50ml-{i["price_50_ml"][:3] if len(i["price_50_ml"]) == 5 else i["price_50_ml"][:2]}₼')

            self.qiymet10 = f'{i["price_10_ml"][:3] if len(i["price_10_ml"]) == 5 else i["price_10_ml"][:2]}'
            self.qiymet20 = f'{i["price_20_ml"][:3] if len(i["price_20_ml"]) == 5 else i["price_20_ml"][:2]}'
            self.qiymet30 = f'{i["price_30_ml"][:3] if len(i["price_30_ml"]) == 5 else i["price_30_ml"][:2]}'
            self.qiymet50 = f'{i["price_50_ml"][:3] if len(i["price_50_ml"]) == 5 else i["price_50_ml"][:2]}'

            self.card.add_widget(self.image)
            self.card.add_widget(self.label1)
            self.card.add_widget(self.label2)
            self.card.add_widget(self.label3)
            self.screen.get_screen('etirler').ids.crsl9.add_widget(self.card)
            self.card.bind(
                on_release=partial(self.etrin_seklin_ve_adin_goster, self.label1.text, self.label2.text, self.desc,
                                   self.image.source))

    def yeniden(self):
        self.root.current = 'loadingscreen'
        self.on_start()

    def etrin_seklin_ve_adin_goster(self, etrinadi, etrincinsi, etrinterkibi, etrinsekli, value):
        self.deyishken = False
        if self.deyishken == False:
            self.screen.get_screen('parfumepage').ids.geriduymesi.on_release = self.rtetirler
            self.screen.get_screen('parfumepage').ids.etiretrafli.on_press = self.etrafli
            self.screen.get_screen('sifaris').ids.sifariset.on_release = self.sonsifaris
        self.root.current = 'parfumepage'
        self.screen.get_screen('parfumepage').ids.parfumephoto.source = etrinsekli
        self.screen.get_screen('parfumepage').ids.etrinadiyazilacaqlabel.text = str(etrinadi)
        self.adi = etrinadi
        self.cinsi = etrincinsi
        self.terkibi = etrinterkibi

    def sonsifaris(self):
        self.root.current = 'sonsifaris'

    def etrafli(self):
        self.root.current = 'etirmelumat'
        self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text = self.adi
        self.screen.get_screen('etirmelumat').ids.terkibi.text = self.terkibi
        self.screen.get_screen('etirmelumat').ids.cinsi.text = self.cinsi

    def rtetirler(self):
        self.root.current = 'etirler'

    def on_start(self):
        self.net = False
        try:
            requests.get('https://www.google.com')
            self.net = True
            self.root.current = 'menu'



        except ConnectionError:
            self.root.current = 'errorscreen'

    def on_key(self, window, key, *args):
        if key == 27:
            if self.root.current_screen.name != 'menu':
                self.root.current = 'menu'
                return True
            elif self.root.current_screen.name == 'menu':
                return False

    def profile_kecid(self):
        self.root.current = 'profil'

    def build(self):
        self.connect = s3.connect('user.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(ad,soyad,dogum_tarixi,mail,nomre,sifre,istifadeci_adi,id INTEGER primary key autoincrement)""")
        self.connect.commit()
        self.connect.close()
        self.sm = ScreenManager()
        self.sm.add_widget(QabSecimi(name='qabsecimi'))
        self.sm.add_widget(IdIste(name='idiste'))
        self.sm.add_widget(SonSifaris(name='sonsifaris'))
        self.sm.add_widget(SifarisSehifesi(name='sifaris'))
        self.sm.add_widget(EtirMelumat(name='etirmelumat'))
        self.sm.add_widget(ParfumePage(name='parfumepage'))
        self.sm.add_widget(Profile(name='profil'))
        self.sm.add_widget(NewName(name='newname'))
        self.sm.add_widget(IscidiYaYox(name='iscidiyayox'))
        self.sm.add_widget(QabKodu(name='qabkodu'))
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(Etirler(name='etirler'))
        self.sm.add_widget(Axtaris(name='axtaris'))
        self.sm.add_widget(Huquqlar(name='huquqlar'))
        self.sm.add_widget(BizimBrendimiz(name='bizimbrendimiz'))
        self.sm.add_widget(BizimleElaqe(name='bizimleelaqe'))
        self.sm.add_widget(MarketinqVeQaydalar(name='marketinqveqaydalar'))
        self.sm.add_widget(GirisVeQeydiyyat(name='girisveqeydiyyat'))
        self.sm.add_widget(Giris(name='giris'))
        self.sm.add_widget(Qeydiyyat(name='qeydiyyat'))
        self.sm.add_widget(QeydiyyatNumEmailPassword(name='qnmp'))
        self.sm.add_widget(QeydiyyatAuthenticator(name='qa'))
        self.sm.add_widget(ErrorScreen(name='errorscreen'))
        self.sm.add_widget(LoadingScreen(name='loadingscreen'))
        self.sm.add_widget(ForgetPassword(name='forgetpassword'))
        self.sm.add_widget(ForgetAuthenticationCode(name='forgetauthenticationcode'))
        self.sm.add_widget(SifreDeyis(name='sifredeyismeyeri'))
        self.title = 'Korona Parfum'
        self.image_name_list = []
        self.parfume_name_list = []
        self.dict2 = {}
        self.s1 = 0

        # ####################################################################################################################### #######################################################################################################################
        return self.screen

    def axtar_goster(self):
        self.root.current = 'axtaris'
        self.dialog2 = MDDialog(
            text="Axtardığınız ətri tapmadığınız halda baş hərfini böyük hərflə yazın.",
            size_hint=(.7, .5),
            buttons=[
                MDFlatButton(
                    text="Ok",
                    on_release=self.dialogu_dagit2
                )
            ]
        )
        self.dialog2.open()

    def back_from_forget(self):
        self.root.current = 'forgetpassword'

    def qeydiyyatdan_kec(self):

        self.number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '+']
        self.mail = self.screen.get_screen('qnmp').ids.email.text
        self.number = self.screen.get_screen('qnmp').ids.number.text
        self.password_new = self.screen.get_screen('qnmp').ids.password_new.text
        self.password_new2 = self.screen.get_screen('qnmp').ids.password_new2.text
        self.username = self.screen.get_screen('qnmp').ids.username.text
        self.a = True

        if not self.mail:
            self.sn = Snackbar(text='Email boş ola bilməz.')
            self.sn.show()
            self.a = False
        elif not self.number:
            self.sn = Snackbar(text='Nömrə boş ola bilməz.')
            self.sn.show()
            self.a = False
        elif not self.password_new:
            self.sn = Snackbar(text='Şifrə boş ola bilməz.')
            self.sn.show()
            self.a = False
        elif not self.password_new2:
            self.sn = Snackbar(text='Şifrəni təkrarlayın.')
            self.sn.show()
            self.a = False
        elif not self.username:
            self.sn = Snackbar(text='İstifadəçi adı boşdur')
            self.sn.show()
            self.a = False
        elif '@' not in self.mail:
            self.sn = Snackbar(text='Email düzgün yazılmayıb.')
            self.sn.show()
            self.a = False
        elif '.' not in self.mail:
            self.sn = Snackbar(text='Email düzgün yazılmayıb.')
            self.sn.show()
            self.a = False
        elif len(self.password_new) < 8:
            self.sn = Snackbar(text='Şifrə uzunluğu 8 deyil.')
            self.sn.show()
            self.a = False
        elif self.password_new != self.password_new2:
            self.sn = Snackbar(text='Şifrələr eyni deyil.')
            self.sn.show()
            self.a = False
        else:
            if self.a == True:
                self.root.current = 'qa'
                self.authentication_code = random.randint(111111, 999999)
                self.mail_content = str(self.authentication_code)
                self.server = slib.SMTP('64.233.184.108', 587)
                self.server.ehlo()
                self.server.starttls()
                self.server.login("koronaparfume@gmail.com", "10bk572275")
                try:
                    self.server.sendmail("koronaparfume@gmail.com",
                                         str(self.mail), self.mail_content)
                except:
                    pass

    def forget_check_username(self):
        self.forget_username = str(self.screen.get_screen('forgetpassword').ids.forgetusername.text)
        if not self.forget_username:
            self.sn = Snackbar(text='İstifadəçi adınzı yazın').show()
        self.connect = s3.connect('user.db')
        self.cursor = self.connect.cursor()
        self.username_for_check = self.screen.get_screen('forgetpassword').ids.forgetusername.text
        self.cursor.execute(f"""SELECT istifadeci_adi FROM users WHERE istifadeci_adi='{self.username_for_check}'""")
        self.connect.commit()
        if not self.cursor.fetchone():
            self.sn = Snackbar(text="Profil mövcud deyil").show()
            self.connect.close()
        else:
            self.authentication_code = random.randint(111111, 999999)
            self.mail_content000 = str(self.authentication_code)
            self.connect = s3.connect('user.db')
            self.cursor = self.connect.cursor()
            self.cursor.execute(f"""SELECT mail FROM users WHERE istifadeci_adi='{self.username_for_check}' """)

            self.server = slib.SMTP('64.233.184.108', 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.login("harleyquinn5722@gmail.com", "harley572275")
            try:
                for i in self.cursor.fetchone():
                    self.server.sendmail("harleyquinn5722@gmail.com",
                                         str(i), self.mail_content000)
                    break
                self.dialog = MDDialog(
                    text=("Mail adresinizə identifikasiya kodu göndərildi."),
                    size_hint_x='.7',
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.forget_authentication_code_sehifesine_kecid,
                        )
                    ]
                )
                self.dialog.open()
                self.connect.commit()
                self.connect.close()
            except:
                self.dialog = MDDialog(
                    text=("Mail adresinizə identifikasiya kodu göndərildi."),
                    size_hint_x='.7',
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.forget_authentication_code_sehifesine_kecid,
                        )
                    ]
                )

                self.dialog.open()
                self.connect.commit()
                self.connect.close()

    def forget_authentication_code_sehifesine_kecid(self, value):
        self.dialog.dismiss()
        self.root.current = 'forgetauthenticationcode'

    def forget_password(self):
        self.root.current = 'forgetpassword'

    def etirlerkechid(self):
        self.root.current = 'etirler'

    def resend_code(self):
        self.authentication_code = random.randint(111111, 999999)
        self.mail_content = str(self.authentication_code)
        self.server = slib.SMTP('64.233.184.108', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login("harleyquinn5722@gmail.com", "harley572275")
        try:
            self.server.sendmail("harleyquinn5722@gmail.com",
                                 str(self.mail), self.mail_content)
            self.sn5 = Snackbar(
                text='Kod göndərildi.'
            )
            self.sn5.show()
        except:
            self.sn5 = Snackbar(
                text='Kod göndərildi.'
            )
            self.sn5.show()

    def idyoxla(self):
        self.idfield = self.screen.get_screen('idiste').ids.sifarisciidsi.text
        if not self.idfield:
            toast("Zəhmət olmasa İD yazın")
        else:
            self.id = self.screen.get_screen('idiste').ids.sifarisciidsi.text
            url = 'http://167.86.115.50/api/register/'
            data = {
                "username": f"{str(self.username1.strip())}",
                "password": f"{self.password_new1}",
                "last_name": f"{str(self.soyad.strip())}",
                "first_name": f"{str(self.ad1.strip())}",
                "invite_id": f"{self.id}",
                "email": f"{self.email1.strip()}"
            }
            post = requests.post(url, data)
            self.new = json.loads(post.text)
            with open('username.txt', 'w+', encoding='utf-8') as file1:
                file1.write(str(self.new['username']))
            with open('email.txt', 'w+', encoding='utf-8') as file2:
                file2.write(str(self.new['email']))
            with open('id.txt', 'w+', encoding='utf-8') as file3:
                file3.write(str(self.new['id']))
            if self.new['username'] == ["A user with that username already exists."]:
                toast('İstifadəçi adını dəyişin')
                self.root.current = 'qnmp'
            elif self.new['email'] == ['Enter a valid email address.']:
                toast('Email düzgün yazılmayıb')
                self.root.current = 'qnmp'
            else:
                toast('Qeydiyyat tamamlandı.Giriş edin.')
                self.root.current = 'giris'

    def LogIn(self):
        self.istifadechi_adi = self.screen.get_screen('giris').ids.istifadeciadi.text
        self.password = self.screen.get_screen('giris').ids.sifre.text
        if not self.istifadechi_adi:
            toast('Məlumatlar boş ola bilməz')
        if not self.password:
            toast('Məlumatlar boş ola bilməz')
        data = {
            "username": f"{str(self.istifadechi_adi).strip()}",
            "password": f"{str(self.password).strip()}"
        }
        post = requests.post('http://167.86.115.50/auth/token/login', data=data)
        new = json.loads(post.text)
        if 'auth_token' in str(post.text):
            self.profile = True
            self.root.current = 'menu'
            girish.append("entered")
            with open('username.txt', 'r+') as file1:
                self.screen.get_screen('profil').ids.labelforusername.text = file1.read()
            with open('email.txt', 'r+') as file2:
                self.screen.get_screen('profil').ids.labelformail.text = file2.read()
            with open('id.txt', 'r+') as file3:
                self.screen.get_screen('profil').ids.labelforid.text = file3.read()
            self.deyismeli_button = self.screen.get_screen('menu').ids.button_for_login_and_signup
            self.deyismeli_button.text = 'Profil'

        else:
            toast('İstifadəçi adı yaxud parol səhvdir')

    def qacmenuya(self):
        url = 'http://167.86.115.50/api/register/'
        data = {
            "username": f"{str(self.username1.strip())}",
            "password": f"{self.password_new1}",
            "last_name": f"{str(self.soyad.strip())}",
            "first_name": f"{str(self.ad1.strip())}",
            "invite_id": "0",
            "email": f"{self.email1.strip()}"
        }
        post = requests.post(url, data)
        self.new = json.loads(post.text)
        with open('username.txt', 'w+', encoding='utf-8') as file1:
            file1.write(str(self.new['username']))
        with open('email.txt', 'w+', encoding='utf-8') as file2:
            file2.write(str(self.new['email']))
        with open('id.txt', 'w+', encoding='utf-8') as file3:
            file3.write(str(self.new['id']))
        if self.new['username'] == ["A user with that username already exists."]:
            toast('İstifadəçi adını dəyişin')
            self.root.current = 'qnmp'
        elif self.new['email'] == ['Enter a valid email address.']:
            toast('Email düzgün yazılmayıb')
            self.root.current = 'qnmp'
        else:
            toast('Qeydiyyat tamamlandı.Giriş edin.')
            self.root.current = 'giris'

    def check_authentication_code(self):
        self.authentication_text = self.screen.get_screen('qa').ids.authcode.text
        if str(self.authentication_text) == str(self.authentication_code):
            self.root.current = 'idiste'

            girish.append("entered")
            self.ad1 = self.screen.get_screen('qeydiyyat').ids.ad.text
            self.soyad1 = self.screen.get_screen('qeydiyyat').ids.soyad.text
            self.email1 = self.screen.get_screen('qnmp').ids.email.text
            self.number1 = self.screen.get_screen('qnmp').ids.number.text
            self.password_new1 = self.screen.get_screen('qnmp').ids.password_new.text
            self.username1 = self.screen.get_screen('qnmp').ids.username.text
            self.ad1 = str(self.ad1.strip())
            self.soyad1 = str(self.soyad1.strip())
            self.email1 = str(self.email1.strip())
            self.number1 = str(self.number1.strip())
            self.password_new1 = str(self.password_new1.strip())
            self.username1 = str(self.username1.strip())
        else:
            toast('Kod düzgün deyil')

    def forget_check_authentication_code(self):
        self.forget_authentication_code_textfield_text = self.screen.get_screen(
            'forgetauthenticationcode').ids.forgetauthenticationcode.text
        if not self.forget_authentication_code_textfield_text:
            self.sn = Snackbar(
                text='Kodu daxil edin.'
            ).show()
        elif str(self.forget_authentication_code_textfield_text) != self.mail_content000:
            self.sn = Snackbar(
                text='Kod düzgün deyil.'
            ).show()
        elif str(self.forget_authentication_code_textfield_text) == self.mail_content000:
            self.root.current = 'sifredeyismeyeri'

    def check_new_password(self):
        self.new_password = str(self.screen.get_screen('sifredeyismeyeri').ids.newpassword.text)
        self.new_password2 = str(self.screen.get_screen('sifredeyismeyeri').ids.newpasswordagain.text)
        self.pass_text_list = []
        for i in str(self.new_password):
            self.pass_text_list.append(i)
        if len(self.pass_text_list) < 8:
            self.sn = Snackbar(
                text="Şifrə uzunluğu 8 deyil."
            )
            self.sn.show()
        if not self.new_password:
            self.sn = Snackbar(
                text="Şifrəni daxil edin."
            ).show()
        if not self.new_password2:
            self.sn = Snackbar(
                text="Şifrəni təkrarlayın."
            ).show()
        if self.new_password != self.new_password2:
            self.sn = Snackbar(
                text="Şifrələr eyni deyil."
            ).show()

        self.connect = s3.connect('user.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            f"""UPDATE users SET sifre='{self.new_password}' WHERE istifadeci_adi='{self.forget_username}'""")
        self.dialog2 = MDDialog(
            text='Şifrəniz dəyişdirildi.',
            size_hint_x='.7',
            buttons=[MDRaisedButton(text='OK', on_release=self.kecmenyuya2)]
        ).open()
        self.connect.commit()
        self.connect.close()

    def forget_resend_authentication_code(self):
        self.authentication_code = random.randint(111111, 999999)
        self.mail_content000 = str(self.authentication_code)
        self.connect = s3.connect('user.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute(f"""SELECT mail FROM users WHERE istifadeci_adi='{self.username_for_check}' """)

        self.server = slib.SMTP('64.233.184.108', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login("harleyquinn5722@gmail.com", "harley572275")
        try:
            for i in self.cursor.fetchone():
                self.server.sendmail("harleyquinn5722@gmail.com",
                                     str(i), self.mail_content000)
            self.dialog = MDDialog(
                size_hint_x='.7',
                text=("Mail adresinizə identifikasiya kodu göndərildi."),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.forget_authentication_code_sehifesine_kecid,
                    )
                ]
            )
            self.dialog.open()
            self.connect.commit()
            self.connect.close()
        except:
            self.dialog = MDDialog(
                text=("Mail adresinizə identifikasiya kodu göndərildi."),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.forget_authentication_code_sehifesine_kecid,
                    )
                ]
            )
            self.dialog.open()
            self.connect.commit()
            self.connect.close()

    def first_sign_check(self):
        self.ad = self.screen.get_screen('qeydiyyat').ids.ad.text
        self.soyad = self.screen.get_screen('qeydiyyat').ids.soyad.text
        self.dtarixi_text = self.screen.get_screen('qeydiyyat').ids.dogumbutton.text
        if self.dtarixi_text == 'Doğum tarixi' or not self.ad or not self.soyad:
            toast('Məlumatlarınızı düzgün qeyd edin')
        else:
            self.root.current = 'qnmp'

    def show_date(self):
        self.picker = MDDatePicker(callback=self.got_date,
                                   year=2000,
                                   month=1,
                                   day=1)
        self.picker.open()

    def got_date(self, the_date):
        self.screen.get_screen('qeydiyyat').ids.dogumbutton.text = str(the_date)
        self.birthday = str(the_date)

    def deyismeli(self):
        if str(self.screen.get_screen('menu').ids.button_for_login_and_signup.text) == 'Profil':
            self.root.current = 'profil'
        else:
            self.root.current = 'girisveqeydiyyat'

    def sqy10(self):
        self.milli = '10ML'
        for i in self.new:
            if i["name"] == str(self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text):
                self.qiymet10_son = str(i["price_10_ml"])
                self.qiymet20_son = str(i["price_20_ml"])
                self.qiymet30_son = str(i["price_30_ml"])
                self.qiymet50_son = str(i["price_50_ml"])

        self.ad_sifaris = self.screen.get_screen('sonsifaris').ids['adsoyadsifaris'].text
        self.nomre_sifaris = str(self.screen.get_screen('sonsifaris').ids.nomresifaris.text)
        self.unvan_sifaris = str(self.screen.get_screen('sonsifaris').ids.unvansifaris.text)
        self.content1 = f"{self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text}\n" \
                        "10ML\n" \
                        f"{self.ad_sifaris}\n" \
                        f"{self.nomre_sifaris}\n" \
                        f"{self.unvan_sifaris}"

        if not self.ad_sifaris:
            toast('Məlumatları düzgün qeyd edin')
        elif not self.nomre_sifaris:
            toast('Məlumatları düzgün qeyd edin')
        elif not self.unvan_sifaris:
            toast('Məlumatları düzgün qeyd edin')
        else:
            self.root.current = 'iscidiyayox'
            self.milli = '10ML'
        self.qiymet = f'{self.qiymet10_son}'

    def sqy20(self):

        self.milli = '20ML'
        for i in self.new:
            if i["name"] == str(self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text):
                self.qiymet10_son = str(i["price_10_ml"])
                self.qiymet20_son = str(i["price_20_ml"])
                self.qiymet30_son = str(i["price_30_ml"])
                self.qiymet50_son = str(i["price_50_ml"])
        self.ad_field = str(self.screen.get_screen('sonsifaris').ids.adsoyadsifaris.text)
        self.nomre_field = str(self.screen.get_screen('sonsifaris').ids.nomresifaris.text)
        self.unvan_field = str(self.screen.get_screen('sonsifaris').ids.unvansifaris.text)
        self.content1 = f"{self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text}\n" \
                        "20ML\n" \
                        f"{self.ad_field}\n" \
                        f"{self.nomre_field}\n" \
                        f"{self.unvan_field}"

        if not self.ad_field:
            toast('Məlumatları düzgün qeyd edin')
        elif not self.nomre_field:
            toast('Məlumatları düzgün qeyd edin')
        elif not self.unvan_field:
            toast('Məlumatları düzgün qeyd edin')
        else:
            self.root.current = 'iscidiyayox'
            self.milli = '20ML'
        self.qiymet = f'{self.qiymet20_son}'

    def sqy30(self):
        self.milli = '30ML'
        for i in self.new:
            if i["name"] == str(self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text):
                self.qiymet10_son = str(i["price_10_ml"])
                self.qiymet20_son = str(i["price_20_ml"])
                self.qiymet30_son = str(i["price_30_ml"])
                self.qiymet50_son = str(i["price_50_ml"])
        self.ad_field = str(self.screen.get_screen('sonsifaris').ids.adsoyadsifaris.text)
        self.nomre_field = str(self.screen.get_screen('sonsifaris').ids.nomresifaris.text)
        self.unvan_field = str(self.screen.get_screen('sonsifaris').ids.unvansifaris.text)
        self.content1 = f"{self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text}\n" \
                        "30ML\n" \
                        f"{self.ad_field}\n" \
                        f"{self.nomre_field}\n" \
                        f"{self.unvan_field}"

        if not self.ad_field:
            toast('Məlumatları düzgün qeyd edin')
        elif not self.nomre_field:
            toast('Məlumatları düzgün qeyd edin')
        elif not self.unvan_field:
            toast('Məlumatları düzgün qeyd edin')
        else:
            self.root.current = 'iscidiyayox'
            self.milli = '30ML'
        self.qiymet = f'{self.qiymet30_son}'

    def sqy50(self):
        self.milli = '50ML'
        for i in self.new:
            if i["name"] == str(self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text):
                self.qiymet10_son = str(i["price_10_ml"])
                self.qiymet20_son = str(i["price_20_ml"])
                self.qiymet30_son = str(i["price_30_ml"])
                self.qiymet50_son = str(i["price_50_ml"])
        self.ad_field = str(self.screen.get_screen('sonsifaris').ids.adsoyadsifaris.text)
        self.nomre_field = str(self.screen.get_screen('sonsifaris').ids.nomresifaris.text)
        self.unvan_field = str(self.screen.get_screen('sonsifaris').ids.unvansifaris.text)
        self.content1 = f"{self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text}\n" \
                        "MIQDAR: 50ML\n" \
                        f"AD VE SOYAD: {self.ad_field}\n" \
                        f"ELAQE NOMRESI: {self.nomre_field}\n" \
                        f"UNVAN: {self.unvan_field}"

        if not self.ad_field:
            toast('Məlumatları düzgün qeyd edin')
        elif not self.nomre_field:
            toast('Məlumatları düzgün qeyd edin')
        elif not self.unvan_field:
            toast('Məlumatları düzgün qeyd edin')
        else:
            self.root.current = 'iscidiyayox'
            self.milli = '50ML'
        self.qiymet = f'{self.qiymet50_son}'

    def gonder(self):
        self.server = slib.SMTP('64.233.184.108', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login("harleyquinn5722@gmail.com", "harley572275")
        self.server.sendmail("harleyquinn5722@gmail.com", "harleyquinn5722@gmail.com", self.content1)
        self.root.current = 'menu'
        self.dialog56 = MDDialog(
            text="Sifarişiniz üçün təşəkkürlər.Sizinlə 24 saat ərzində əlaqə saxlanılacaq.",
            size_hint_y=.7,
            buttons=[
                MDFlatButton(text="Ok", on_release=self.dismis56)
            ]
        )
        self.dialog56.open()

    def sifariset(self):
        for i in self.new:
            if i["name"] == str(self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text):
                self.screen.get_screen('sifaris').ids.ml10.text = str(i["price_10_ml"])
                self.screen.get_screen('sifaris').ids.ml20.text = str(i["price_20_ml"])
                self.screen.get_screen('sifaris').ids.ml30.text = str(i["price_30_ml"])
                self.screen.get_screen('sifaris').ids.ml50.text = str(i["price_50_ml"])
        self.root.current = 'sonsifaris'

    def dismis56(self, value):
        self.dialog56.dismiss()

    def sifarisekecid(self):
        self.sonsifaris()

    def etir_haqqinda_melumat(self):
        for i in self.new:
            if i["name"] == self.adad.upper():
                self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text = str(
                    i["name"]).lower().capitalize()
                self.screen.get_screen('etirmelumat').ids.terkibi.text = str(i["descrption"])
                self.screen.get_screen('etirmelumat').ids.cinsi.text = str(i["gender"]).capitalize()
        self.root.current = 'etirmelumat'
        """
        self.screen.get_screen('etirmelumat').ids.qiymet10ml.text = f'{self.lazimli_list[2]}{self.lazimli_list[3]}AZN'
        self.screen.get_screen('etirmelumat').ids.qiymet20ml.text = f'{self.lazimli_list[6]}{self.lazimli_list[7]}AZN'
        self.screen.get_screen('etirmelumat').ids.qiymet30ml.text = f'{self.lazimli_list[10]}{self.lazimli_list[11]}AZN'
        if len(self.lazimli_list) == 17:
            self.screen.get_screen('etirmelumat').ids.qiymet50ml.text = f'{self.lazimli_list[14]}{self.lazimli_list[15]}{self.lazimli_list[16]}AZN'
        else:
            self.screen.get_screen(
                'etirmelumat').ids.qiymet50ml.text = f'{self.lazimli_list[14]}{self.lazimli_list[15]}AZN'
        self.root.current = 'etirmelumat'
        """

    #######################################################################################################################################################
    def on_stop(self):
        girish.clear()

    def sifre_deyisme_legv_et(self):
        self.dialog = MDDialog(
            text=("Ləğv etmək istədiyinizdən əminsinizmi?"),
            size_hint_x='.7',
            buttons=[
                MDFlatButton(
                    text="Geri",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.dialogu_dagit,
                ),
                MDRaisedButton(
                    text="OK",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.kecmenyuya
                )
            ]
        )
        self.dialog.open()

    def kecmenyuya(self, value):
        self.dialog.dismiss()
        self.root.current = 'menu'

    def kecmenyuya2(self, value):
        self.root.current = 'menu'

    def dialogu_dagit2(self, value):
        self.dialog2.dismiss(force=True)

    def dialogu_dagit(self, value):
        self.dialog.dismiss()

    def yazdir(self, name):
        self.adad = str(name)
        self.screen.get_screen('parfumepage').ids.etrinadiyazilacaqlabel.text = str(name)
        for i in self.new:
            if i["name"] == str(name).upper():
                self.screen.get_screen('parfumepage').ids.parfumephoto.source = i["image"]
            else:
                pass
        self.root.current = 'parfumepage'

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''
        """
        self.current = os.getcwd()
        self.dict1 = {}
        try:
            self.book = load_workbook('duxusiyahi.xlsx')
        except:
            os.chdir('..')
            self.book = load_workbook('duxusiyahi.xlsx')
        self.duxu_adlari = []
        self.sheet = self.book['sheet']
        for row in self.sheet.rows:
            if str(row[1].value) == 'None':
                pass
            else:
                self.duxu_adlari.append(str(row[1].value).lower().capitalize())

        self.sekil_adlari = []

        try:
            if os.getcwd().endswith('_files'):
                os.chdir('..')
                for i in os.listdir(os.chdir('allimages_files')):
                    self.sekil_adlari.append(str(i))
            else:
                for i in os.listdir(os.chdir('allimages_files')):
                    self.sekil_adlari.append(str(i))
        except:
            os.chdir('..')
            for i in os.listdir(os.chdir('allimages_files')):
                self.sekil_adlari.append(str(i))
        self.s = 0
        for t in self.duxu_adlari:
            self.dict1[f'{t}'] = self.sekil_adlari[self.s]
            self.s += 1
        """

        def add_icon_item(name_icon):
            self.screen.get_screen('axtaris').ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": 'atom',
                    "text": name_icon,
                    "on_press": partial(self.yazdir, name_icon)
                }
            )

        self.screen.get_screen('axtaris').ids.rv.data = []
        for name_icon in self.siyahi9:
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

    def idyazildi(self):
        self.idd = str(self.screen.get_screen('iscidiyayox').ids.sifarisbitdiid.text)
        self.qabsecimi()

    def qabsecimi(self):
        self.nm = ''
        self.root.current = 'qabsecimi'
        self.siyahi = {'eight.jpg30': '#101',
                       'eleven.jpg50': '#102',
                       'fifteen.jpg50': '#103',
                       'five.jpg30': '#104',
                       'four.jpg50': '#105',
                       'fourteen.jpg10': '#106',
                       'nine.jpg50': '#107',
                       'nineteen.jpg50': '#108',
                       'seven.jpg50': '#109',
                       'six.jpg30': '#110',
                       'sixteen.jpg30': '#111',
                       'ten.jpg30': "#112",
                       'thirteen.jpg50': "#113",
                       'three.jpg50': "#114",
                       'twelve.jpg30': "#115",
                       'twenty.jpg30': "#116",
                       'twentyeight.jpg20': "#117",
                       'twentyfive.jpg50': "#118",
                       'twentyfour.jpg30': "#119",
                       'twentynine.jpg30': "#120",
                       'twentyone.jpg30': "#121",
                       'twentyseven.jpg50': "#122",
                       'twentysix.jpg50': "#123",
                       'twentythree.jpg20': "#124",
                       'twentytwo.jpg50': "#125",
                       'two.jpg10': "#126"
                       }
        for qab in self.siyahi.keys():
            a, b = os.path.splitext(qab)
            self.label = MDLabel(text=f'{b[4:]} ML Kod-{self.siyahi[f"{qab}"]}', halign='center', size_hint_y=.1)
            self.image = Image(source=f'{a}.jpg', size_hint_y=.9)
            self.card = MDCard(orientation='vertical', on_release=self.yaz)

            self.card.add_widget(self.label
                                 )
            self.card.add_widget(
                self.image
            )
            self.screen.get_screen('qabsecimi').ids.crsl1.add_widget(self.card)

    def qabsecimioldu(self):
        self.qiymet = ''

        self.kod_field = self.screen.get_screen('qabkodu').ids.kod.text
        if not self.kod_field:
            toast('Zəhmət olmasa qabın kodunu yazın')
        else:
            for i in self.new:
                if i["name"] == str(self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text).upper():
                    self.qiymet10_son = str(i["price_10_ml"])
                    self.qiymet20_son = str(i["price_20_ml"])
                    self.qiymet30_son = str(i["price_30_ml"])
                    self.qiymet50_son = str(i["price_50_ml"])
                    if self.milli == '10ML':
                        self.qiymet = self.qiymet10_son
                    elif self.milli == '20ML':
                        self.qiymet = self.qiymet20_son
                    elif self.milli == '30ML':
                        self.qiymet = self.qiymet30_son
                    elif self.milli == '50ML':
                        self.qiymet = self.qiymet50_son
            for i in self.siyahi.keys():
                if self.siyahi[str(i)] == str(self.kod_field):
                    toast('Sifarişiniz qəbul olundu.')
                    a, b = os.path.splitext(f'{i}')
                    msg = MIMEMultipart()
                    msg['Subject'] = "Yeni Sifariş"
                    msg['From'] = 'harleyquinn5722@gmail.com'
                    msg['To'] = 'koronaparfume@gmail.com'
                    self.ad_str = self.screen.get_screen('sonsifaris').ids.adsoyadsifaris.text
                    self.nomre_str = self.screen.get_screen('sonsifaris').ids.nomresifaris.text
                    self.unvan_str = self.screen.get_screen('sonsifaris').ids.unvansifaris.text
                    self.etrin_adi = self.screen.get_screen('etirmelumat').ids.etrinadisifarissehifesi.text

                    try:
                        self.content999 = MIMEText(
                            f'SIFARİŞ HAQQINDA MƏLUMAT\n{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}\nƏTRİN ADI - {self.etrin_adi}\nQİYMƏTİ - {self.qiymet} AZN\nMİQDARI - {self.milli}\n'
                            f'QABIN KODU - {self.kod_field}\n\nSİFARİŞÇİ HAQQINDA MƏLUMAT\nADI - {self.ad_str}\n'
                            f'TELEFON NÖMRƏSİ - {self.nomre_str}\nÜNVANI - {self.unvan_str}\n'
                            f'SİFARİŞÇİNİN İD KODU - {self.idd}')
                        msg.attach(self.content999)
                        server = smtplib.SMTP('64.233.184.108', 587)
                        server.ehlo()
                        server.starttls()
                        server.login('harleyquinn5722@gmail.com', password='10bk572275')
                        server.sendmail('harleyquinn5722@gmail.com', 'koronaparfume@gmail.com', msg.as_string())
                        server.quit()
                        self.root.current = 'menu'
                    except:
                        self.content999 = MIMEText(
                            f'SIFARİŞ HAQQINDA MƏLUMAT\n{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}\nƏTRİN ADI - {self.etrin_adi}\nQİYMƏTİ - {self.qiymet} AZN\nMİQDARI - {self.milli}\n'
                            f'QABIN KODU - {self.kod_field}\n\nSİFARİŞÇİ HAQQINDA MƏLUMAT\nADI - {self.ad_str}\n'
                            f'TELEFON NÖMRƏSİ - {self.nomre_str}\nÜNVANI - {self.unvan_str}\n')
                        msg.attach(self.content999)
                        server = smtplib.SMTP('64.233.184.108', 587)
                        server.ehlo()
                        server.starttls()
                        server.login('harleyquinn5722@gmail.com', password='10bk572275')
                        server.sendmail('harleyquinn5722@gmail.com', 'koronaparfume@gmail.com', msg.as_string())
                        server.quit()
                        self.root.current = 'menu'
                else:
                    toast('Sifarişiniz qəbul olundu.')

    def yaz(self, value):
        self.root.current = 'qabkodu'

if __name__ == "__main__":
    CoronaParfumApp().run()