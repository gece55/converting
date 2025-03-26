import flet as ft
from flet import *

import sqlite3

# Henri Ndonko - TheEthicalBoy ->üretici

def main(page: ft.Page):
    page.title = "Flet SQLITE FORM"
    page.window.width=375
    page.window.height=500
    page.theme_mode = ThemeMode.LIGHT
    page.vertical_alignment = "center"
    page.horizontal_alignment="center"

    rsm=Icon("cloud_download",size=55)
    id=TextField(label="id",border_radius=ft.border_radius.all(30),filled=True,bgcolor="#F78472",icon="")
    adv=TextField(label="ad",border_radius=ft.border_radius.all(30),filled=True,bgcolor="#F78472",icon="")
    psw=TextField(label="şifre",  password=True, can_reveal_password=True,border_radius=ft.border_radius.all(30),filled=True,bgcolor="#F78472",hint_text="" )
    shr=TextField(label="şehir",border_radius=ft.border_radius.all(30),filled=True,bgcolor="#F78472",icon="")

    def ekle(e):
        vt = sqlite3.connect('deneme.db')
        im = vt.cursor()
        im.execute("insert into person(id,ad,sifre,sehir) VALUES(?,?,?,?)",(id.value,adv.value,psw.value,shr.value))
        vt.commit()

        page.update()

    def sil(e):
        vt = sqlite3.connect('deneme.db')
        im = vt.cursor()
        im.execute("delete from person where id=?",str(id.value))
        vt.commit()

        page.update()

    def güncelle(e):
        vt = sqlite3.connect('deneme.db')
        im = vt.cursor()
        im.execute("update person set ad=?,sifre=?,sehir=? where id=?", (adv.value,psw.value,shr.value,id.value))       
        vt.commit()
        page.update()


    rw=Row(
        [
        ElevatedButton("sil",icon="delete_forever",on_click=sil),
        ElevatedButton("ekle",icon="arrow_forward",on_click=ekle),
        ElevatedButton("güncelle",icon="edit",on_click=güncelle)
        
        ],spacing=15,alignment="center",vertical_alignment="center"
    )
    
    col=Column([rsm,id,adv,psw,shr,rw],alignment="center",horizontal_alignment="center",spacing=20)

    form=Container(
        content=col,expand=1,bgcolor="#84E8E3"
    )
    
    page.add(form)
    page.update()

ft.app(target=main)