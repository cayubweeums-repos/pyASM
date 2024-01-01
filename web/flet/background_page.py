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
# FWG = '#2e2f31' # Dark Grey
ACCENT = '#4CAF50' # Green
ACCENT_DARKER = '#388E3C' # Darker Green for Shadows
ACCENT_LIGHTER = '#8BC34A' # Lighter Green for Highlights 

# Page object for the page under the FG page
class bg_page(UserControl):
    def __init__(self,page, fg_page):
        super().__init__()
        self.page = page
        self.fg_page = fg_page

    def build(self):
        return Container(
        width=self.page.width,
        height=self.page.height,
        bgcolor=SECOND_BG,
        padding=ft.padding.only(
            top=50,bottom=5,
            left=20,right=20
        ),
        content=ft.Column(
            controls=[
                Container(
                    on_click=lambda e: self.grow(e),
                    content=ft.Text('<')
                ),
                Container(
                    width=self.page.width * 0.1,
                    height=self.page.height,
                    bgcolor=SECOND_BG,
                    alignment=ft.alignment.center,
                    content=NavBar(self.page)
                )
            ]
        )
    )

    def grow(self, e):
        self.fg_page.controls[0].width = self.page.width
        self.fg_page.controls[0].scale = ft.transform.Scale(1,alignment=ft.alignment.center_right)
        self.fg_page.controls[0].border_radius = 0
        self.fg_page.update()