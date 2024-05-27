import flet as ft

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("hello, world!!!")))
    page.add(ft.SafeArea(ft.Text("olá mundo!!!!")))

ft.app(main)