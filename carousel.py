import flet as ft

def carousel_view(page: ft.Page):
    current_index = 0

    cards = [
        ft.Card(content=ft.Text("Card 1", size=20)),
        ft.Card(content=ft.Text("Card 2", size=20)),
        ft.Card(content=ft.Text("Card 3", size=20)),
    ]

    def update_carousel():
        carousel_view.controls[1].content = cards[current_index]
        page.update()

    def previous_card(e):
        nonlocal current_index
        if current_index > 0:
            current_index -= 1
            update_carousel()

    def next_card(e):
        nonlocal current_index
        if current_index < len(cards) - 1:
            current_index += 1
            update_carousel()

    carousel_view = ft.View(
        "/carousel",
        [
            ft.Text("Carousel", size=30),
            ft.Container(content=cards[current_index], expand=True),
            ft.Row(
                [
                    ft.ElevatedButton("Previous", on_click=previous_card),
                    ft.ElevatedButton("Next", on_click=next_card),
                ],
                alignment="center",
            )
        ]
    )
    return carousel_view
