import flet as ft
from sidebar import NavBar
from background_page import bg_page
from foreground_page import fg_page
from views import views_handler


# TODO
#  Make basic, minimal, exclusivley functional structure and feature set that does not take into account asthetics, or anything else.
#  For a login page it will be two text fields and a button
#  For the targets page it will display all targets in a grid and will allow you to add targets


"""
Initialize Global App Values
#----------------------------------
"""
# Colors from -> https://m3.material.io/styles/color/system/overview
PRIM_BG = '#121212' # Dark Grey/Black
PRIM_TEXT = '#FFFFFF' # Light Grey/White
SECOND_BG = '#1E1E1E' # Slightly Darker Grey/Black
FG = '#2e2f31' # Lighter Grey
# FWG = '#2e2f31' # Dark Grey
ACCENT = '#4CAF50' # Green
ACCENT_DARKER = '#388E3C' # Darker Green for Shadows
ACCENT_LIGHTER = '#8BC34A' # Lighter Green for Highlights 

def main(page: ft.Page):
    page.title = "Main Functionality App"
    page.on_resize = page_resize
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    pages = {
        '/': ft.View(
            "/",
            [
                container
            ],
        ),
        # '/create_test': ft.View(
        #     "/create_test",
        #     [
        #         create_test_view
        #     ],
        # ),
        # '/targets': ft.View(
        #     "/targets",
        #     [
        #         targets_view
        #     ],
        # ),

    }

    container = ft.Container(
        bgcolor=PRIM_BG,
        content=ft.Stack(
            controls=[
                bg_page(page, fg_page),
                fg_page(page, bg_page)
            ]
        )

    )

    page.on_route_change = route_change
    page.go(page.route)

    page.add(container)

    def page_resize(e):  # <<< new
        # Pops up a message from page bottom side.
        page.snack_bar = ft.SnackBar(ft.Text(f'New page size => width: {page.width}, height: {page.height}'))
        page.snack_bar.open = True

        page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )


if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)