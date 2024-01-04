import flet as ft



def views_handler(page):
    return{
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
    }