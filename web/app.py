import flet as ft
from flet import UserControl
from web.pages.targets import Targets_Page
from web.pages.dashboard import Dashboard_Page

# TODO
#  Make basic, minimal, exclusivley functional structure and feature set that does not take into account asthetics, or anything else.
#  For a login page it will be two text fields and a button
#  For the targets page it will display all targets in a grid and will allow you to add targets

# I was on time stamp 32:36 of the following vid:
# - https://www.youtube.com/watch?v=RpEoI1an5gA

class Main(UserControl):
    def __init__(self, page: ft.Page,):
        super().__init__()
        self.page = page
        self.init()

    def init(self,):
        self.page.on_route_change = self.on_route_change
        self.page.go('/')

    def on_route_change(self, route):
        new_page = {
            "/": Dashboard_Page,
            "/targets": Targets_Page,
            # "/signup": Signup,
            # "/me": Dashboard,
            # "/forgotpassword": ForgotPassword

        }[self.page.route](self.page)


        self.page.views.clear()
        self.page.views.append(
            ft.View(
                route,
                [new_page]
            )
        )



# if __name__ == '__main__':
#     ft.app(target=Main, view=ft.AppView.WEB_BROWSER)