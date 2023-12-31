import time
import random
import flet as ft
from flet import UserControl, Container, Column, Row
from functools import partial

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

# Sidebar object
class NavBar(UserControl):
    def __init__(self):
        super().__init__()

    def Highlight(self, e):
        if e.data == 'true':
            e.control.bgcolor='white10'
            e.control.update()

            e.control.content.controls[0].icon_color=PRIM_TEXT
            e.control.content.controls[1].color=PRIM_TEXT
            e.control.content.update()

        else:
            e.control.bgcolor=None
            e.control.update()

            e.control.content.controls[0].icon_color="white54"
            e.control.content.controls[1].color="white54"
            e.control.content.update()

    def UserData(self, initials: str, name: str, title: str):
        # first row has user info, name, title, etc
        return Container(
            content=ft.Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor=PRIM_BG,
                        alignment=ft.alignment.center,
                        border_radius=8,
                        content=ft.Text(
                            value=initials, size=20, weight="bold"
                        )
                    ),
                    ft.Column(
                        alignment="center",
                        spacing=1,
                        controls=[
                            ft.Text(
                                value=name,
                                # size=11,
                                weight='bold',

                            ),
                            ft.Text(
                                value=title,
                                # size=9,
                                weight='w400',
                                color=PRIM_TEXT

                            ),
                        ]
                    )
                ]
            )
        )
    
    def ContainedIcon(self, icon_name:str, text:str):
        return Container(
            border_radius=10,
            on_hover=lambda e: self.Highlight(e),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        # icon_size=18,
                        icon_color="white54",
                        style=ft.ButtonStyle(
                            shape={
                                "": ft.RoundedRectangleBorder(radius=7)
                            },
                            overlay_color={"":"transparent"}
                        )
                    ),
                    ft.Text(
                        value=text,
                        color="white54",
                        # size=11,
                    )
                ]
            ),
        )

    def build(self):
        return Container(
            # define dimensions and characteristics of returned container
            padding=ft.padding.only(top=10),
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    self.UserData("CW", 'Cayub Weeums', 'Pro. Weener Licker'),
                    ft.Divider(height=5, color='transparent'),
                    self.ContainedIcon(ft.icons.SEARCH, 'Search'),
                    self.ContainedIcon(ft.icons.DASHBOARD_ROUNDED, 'Dashboard'),
                    self.ContainedIcon(ft.icons.BAR_CHART, 'Stats'),
                    self.ContainedIcon(ft.icons.NOTIFICATIONS, 'Alerts'),
                ]
            ),
        )
