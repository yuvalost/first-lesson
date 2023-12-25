import flet as ft

def main(page: ft.Page):
    def button_clicked(event: ft.ControlEvent):
        page.add(ft.Text(value=f"my name is {text_inputer.value}"))
    text = ft.Text(value="Hello yuval", color = "red", size=20)
    button = ft.ElevatedButton(text="click me", on_click=button_clicked)
    text_inputer = ft.TextField(label= "my name is?")
    row = ft.Row(controls=[text_inputer, button])
    page.add(text, row)

ft.app(target=main)#, view=ft.AppView.WEB_BROWSER)