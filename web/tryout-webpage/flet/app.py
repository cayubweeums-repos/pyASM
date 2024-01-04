import random
import flet as ft
from sidebar import NavBar
from background_page import bg_page
from foreground_page import fg_page
from views import views_handler


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
    page.title = "Flet example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # def shrink(e):
    #     page_2.controls[0].width = page.width * 0.9
    #     page_2.controls[0].scale = ft.transform.Scale(0.9,alignment=ft.alignment.center_right)
    #     page_2.controls[0].border_radius = 30
    #     page_2.update()

    # def grow(e):
    #     page_2.controls[0].width = page.width
    #     page_2.controls[0].scale = ft.transform.Scale(1,alignment=ft.alignment.center_right)
    #     page_2.controls[0].border_radius = 0
    #     page_2.update()

    def page_resize(e):  # <<< new
        # Pops up a message from page bottom side.
        page.snack_bar = ft.SnackBar(ft.Text(f'New page size => width: {page.width}, height: {page.height}'))
        page.snack_bar.open = True

        page.update()

    page.on_resize = page_resize

    create_test_view = ft.Container(
        content=ft.Container(
            width=40,
            height=40,
            on_click=lambda _: page.go('/'),
            content=ft.Text('x'),       
        )
    )

    targets_view = ft.Container(
        content=ft.Container(
            width=200,
            height=200,
            on_click=lambda _: page.go('/'),
            content=ft.Text('click me this is the targets page'),       
        )
    )

    # tasks = ft.Column(
    #     height=(page.height * 0.55),
    #     width=(page.width * 0.9),
    #     alignment=ft.alignment.center,
    #     scroll='auto',
    # )

    # for i in range(10):
    #     tasks.controls.append(
    #         ft.Container(
    #             bgcolor=ACCENT,
    #             height=(tasks.height * 0.1),
    #             width=(tasks.width * 0.8),
    #             border_radius=20,
    #             padding=ft.padding.only(
    #                 left=tasks.width * 0.02,
    #                 top=tasks.height * 0.037,
    #             ),
    #             content=ft.Column(
    #                 controls=[
    #                     ft.Text("this is a test?")
    #                 ]
    #             )
    #         )
    #     )


    # categories = ['Reconnaissance', 'Initial Access', 'Execution', 'Persistence', 'Privilege Escalation', 'Defense Evasion', 'Credential Access', 'Discovery', 'Lateral Movement', 'Command and Control', 'Exfiltration']


    # categories_card = ft.Row(
    #     scroll='auto'
    # )
    # for category in categories:
    #     percentage = random.randint(1, 249)
    #     categories_card.controls.append(
    #         ft.Container(
    #             bgcolor=SECOND_BG,
    #             border_radius=20,
    #             padding=15,
    #             height=210,
    #             width=270,
    #             content=ft.Column(
    #                 controls=[
    #                     ft.Text(category),
    #                     ft.Text('Coverage'),
    #                     ft.Container(
    #                         height=100,
    #                     ),
    #                     ft.Container(
    #                         alignment=ft.alignment.center,
    #                         width=250,
    #                         height=5,
    #                         bgcolor=FG,
    #                         border_radius=20,
    #                         padding=ft.padding.only(right=percentage),
    #                         content=ft.Container(
    #                             bgcolor=ACCENT,
    #                             border_radius=20
    #                         )
    #                     )
    #                 ]
    #             )
    #         )
    #     )

    # landing_page_contents = ft.Container(
    #     content=ft.Column(
    #         controls=[
    #             ft.Row(
    #                 alignment='spaceBetween',
    #                 controls=[
    #                     ft.Container(
    #                         on_click=lambda e: shrink(e),
    #                         content=ft.Icon(
    #                             ft.icons.MENU
    #                         )
    #                     ),
    #                     ft.Row(
    #                         controls=[
    #                             ft.Icon(ft.icons.SEARCH),
    #                             ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED),
    #                         ]
    #                     )
    #                 ]
    #             ),
    #             ft.Container(
    #                 height=20
    #             ),
    #             ft.Text(
    #                 value='What\'s up, Cayub'
    #             ),
    #             ft.Container(
    #                 padding=ft.padding.only(top=10,bottom=20),
    #                 content=categories_card
    #             ),
    #             ft.Container(
    #                 height=100,
    #             ),
    #             ft.Text(
    #                 "Weener"
    #             ),
    #             ft.Stack(
    #                 controls=[
    #                     tasks,
    #                     ft.FloatingActionButton(
    #                         bottom=2, 
    #                         right=20,
    #                         icon= ft.icons.ADD,on_click=lambda _: page.go('/create_test')
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    # )

    # page_2 = ft.Row(
    #     alignment='end',
    #     controls=[
    #         ft.Container(
    #         width=page.width,
    #         height=page.height,
    #         bgcolor=PRIM_BG,
    #         animate=ft.animation.Animation(600,curve='decelerate'),
    #         animate_scale=ft.animation.Animation(400,ft.AnimationCurve.DECELERATE),
    #         padding=ft.padding.only(
    #             top=50,bottom=5,
    #             left=20,right=20
    #         ),
    #         content=ft.Column(
    #             controls=[
    #                 landing_page_contents
    #             ]
    #         )
    #     )
    #     ]
    # )


    container = ft.Container(
        # expand=True,
        bgcolor=PRIM_BG,
        content=ft.Stack(
            controls=[
                bg_page(page, fg_page),
                fg_page(page, bg_page)
            ]
        )

    )

    pages = {
        '/': ft.View(
            "/",
            [
                container
            ],
        ),
        '/create_test': ft.View(
            "/create_test",
            [
                create_test_view
            ],
        ),
        '/targets': ft.View(
            "/targets",
            [
                targets_view
            ],
        ),

    }

    # def route_change(route):
    #     page.views.clear()
    #     page.views.append(
    #         views_handler(page)
    #     )

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.on_route_change = route_change
    page.go(page.route)

    page.add(container)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)