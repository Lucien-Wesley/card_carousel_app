import flet as ft

def signup_view(page: ft.Page, navigate_to):
    return ft.View(
        "/signup",
        [
            ft.Text("Sign Up", size=30),
            ft.TextField(label="Name"),
            ft.TextField(label="Email"),
            ft.TextField(label="Password", password=True),
            ft.ElevatedButton(text="Register", on_click=lambda _: navigate_to("/carousel")),
            ft.TextButton(text="Login", on_click=lambda _: navigate_to("/login")),
        ]
    )
