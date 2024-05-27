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

    testo = ft.Text()
    page.add(testo) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(10):
        time.sleep(1)
        testo.value = f"Step {i}"
        page.update()

ft.app(target=main)