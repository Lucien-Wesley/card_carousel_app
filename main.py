import flet as ft
from login import login_view
from sign import signup_view
from carousel import carousel_view

def main(page: ft.Page):

    # Fonction pour basculer entre les fenêtres
    def navigate_to(route):
        page.go(route)

    # Gestion des routes pour les différentes vues
    def route_change(route):
        page.views.clear()
        if page.route == "/login":
            page.views.append(login_view(page, navigate_to))
        elif page.route == "/signup":
            page.views.append(signup_view(page, navigate_to))
        elif page.route == "/carousel":
            page.views.append(carousel_view(page))
        page.update()

    page.on_route_change = route_change
    page.go("/login")

ft.app(target=main)
