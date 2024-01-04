import random
import flet as ft
from flet import UserControl, Container
from sidebar import NavBar

"""
Initialize Global App Values
#----------------------------------
"""
# Colors from -> https://m3.material.io/styles/color/system/overview
PRIM_BG = '#121212' # Dark Grey/Black
PRIM_TEXT = '#FFFFFF' # Light Grey/White
SECOND_BG = '#1E1E1E' # Slightly Darker Grey/Black
FG = '#2e2f31' # Lighter Grey
ACCENT = '#4CAF50' # Green
ACCENT_DARKER = '#388E3C' # Darker Green for Shadows
ACCENT_LIGHTER = '#8BC34A' # Lighter Green for Highlights 

# Page object for the page over the BG page
class fg_page(UserControl):
    def __init__(self,page, bg_page):
        super().__init__()
        self.page = page
        self.bg_page = bg_page

    def shrink(self, e):
        self.controls[0].width = self.page.width * 0.9
        self.controls[0].scale = ft.transform.Scale(0.9,alignment=ft.alignment.center_right)
        self.controls[0].border_radius = 30
        self.update()

    def build(self):

        categories = ['Reconnaissance', 'Initial Access', 'Execution', 'Persistence', 'Privilege Escalation', 'Defense Evasion', 'Credential Access', 'Discovery', 'Lateral Movement', 'Command and Control', 'Exfiltration']


        categories_card = ft.Row(
            scroll='auto'
        )
        for category in categories:
            percentage = random.randint(1, 249)
            categories_card.controls.append(
                ft.Container(
                    bgcolor=SECOND_BG,
                    border_radius=20,
                    padding=15,
                    height=210,
                    width=270,
                    content=ft.Column(
                        controls=[
                            ft.Text(category),
                            ft.Text('Coverage'),
                            ft.Container(
                                height=100,
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                width=250,
                                height=5,
                                bgcolor=FG,
                                border_radius=20,
                                padding=ft.padding.only(right=percentage),
                                content=ft.Container(
                                    bgcolor=ACCENT,
                                    border_radius=20
                                )
                            )
                        ]
                    )
                )
            )

        tasks = ft.Column(
            height=(self.page.height * 0.55),
            width=(self.page.width * 0.9),
            alignment=ft.alignment.center,
            scroll='auto',
        )

        for i in range(10):
            tasks.controls.append(
                ft.Container(
                    bgcolor=ACCENT,
                    height=(tasks.height * 0.1),
                    width=(tasks.width * 0.8),
                    border_radius=20,
                    padding=ft.padding.only(
                        left=tasks.width * 0.02,
                        top=tasks.height * 0.037,
                    ),
                    content=ft.Column(
                        controls=[
                            ft.Text("this is a test?")
                        ]
                    )
                )
            )


        landing_page_contents = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment='spaceBetween',
                        controls=[
                            ft.Container(
                                on_click=lambda e: self.shrink(e),
                                content=ft.Icon(
                                    ft.icons.MENU
                                )
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.SEARCH),
                                    ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED),
                                ]
                            )
                        ]
                    ),
                    ft.Container(
                        height=20
                    ),
                    ft.Text(
                        value='What\'s up, Cayub'
                    ),
                    ft.Container(
                        padding=ft.padding.only(top=10,bottom=20),
                        content=categories_card
                    ),
                    ft.Container(
                        height=100,
                    ),
                    ft.Text(
                        "Weener"
                    ),
                    ft.Stack(
                        controls=[
                            tasks,
                            ft.FloatingActionButton(
                                bottom=2, 
                                right=20,
                                icon= ft.icons.ADD,on_click=lambda _: self.page.go('/create_test')
                            )
                        ]
                    )
                ]
            )
        )


        return ft.Row(
        alignment='end',
        controls=[
            ft.Container(
            width=self.page.width,
            height=self.page.height,
            bgcolor=PRIM_BG,
            animate=ft.animation.Animation(600,curve='decelerate'),
            animate_scale=ft.animation.Animation(400,ft.AnimationCurve.DECELERATE),
            padding=ft.padding.only(
                top=50,bottom=5,
                left=20,right=20
            ),
            content=ft.Column(
                controls=[
                    landing_page_contents
                ]
            )
        )
        ]
    )