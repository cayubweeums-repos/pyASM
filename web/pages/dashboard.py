import flet as ft
from flet import Container
from utils.colors import *

class Dashboard_Page(Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = PRIM_BG
        self.content = ft.Column(
                alignment = 'center',
                horizontal_alignment = 'center',
                controls=[
                    Container(
                        bgcolor='white',
                        content=ft.FloatingActionButton(
                            icon= ft.icons.ADD,on_click=lambda _: self.page.go('/targets')
                            )
                    )
                ]
            )