import flet as ft
from flet import Container
from utils.colors import *

class Targets_Page(Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = SECOND_BG
        self.content = ft.Container(
                on_click=lambda _: page.go('/'),
                content=ft.Text('x'),       
            )