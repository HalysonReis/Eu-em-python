import flet as ft
import time


def main(page: ft.Page):
    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
        ])
    )

    texto = ft.Text()
    page.add(texto) # it's a shortcut for page.controls.append(t) and then page.update()
    
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        texto.value = f"step {i}"
        page.update()
        time.sleep(0.3)

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))
    page.add(ft.ElevatedButton(text="registar", on_click=button_clicked))
ft.app(target=main)