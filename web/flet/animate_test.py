import flet as ft

"""
Initialize Global App Values
#----------------------------------
"""
# Colors from -> https://m2.material.io/design/color/the-color-system.html#tools-for-picking-colors
BG = '#37474F' #Blue Grey 50 800
FWG = '#90A4AE' #Blue Grey 50 300
FG = '#607D8B' #Blue Grey 50 500
ACCENT = '#00C853' #Green50 A700

def main(page: ft.Page):
    page.title = "Flet example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def shrink(e):
        # page_2.controls[0].width = page.width * 0.7
        # page_2.controls[0].height = page.height * 0.8
        page_2.scale = ft.transform.Scale(0.8,alignment=ft.alignment.center_right)
        page_2.update()

    landing_page_contents = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment='spaceBetween',
                    controls=[
                        ft.Container(
                            on_click=lambda e: shrink(e),
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
            ]
        )
    )

    page_1 = ft.Container()
    page_2 = ft.Container(
        width=page.width,
        height=page.height,
        bgcolor=FG,
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


    container = ft.Container(
        expand=True,
        bgcolor=BG,
        content=ft.Stack(
            controls=[
                page_1,
                page_2
            ]
        )

    )

    page.add(container)


if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)