import flet as ft

def login_view(page: ft.Page, navigate_to):
    return ft.View(
        "/login",
        [
            ft.Text("Login", size=30),
            ft.TextField(label="Email"),
            ft.TextField(label="Password", password=True),
            ft.ElevatedButton(text="Login", on_click=lambda _: navigate_to("/carousel")),
            ft.TextButton(text="Sign Up", on_click=lambda _: navigate_to("/signup")),
        ]
    )
