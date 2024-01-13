import flet as ft
from flet import Container, TextField
from web.utils.colors import *
from objects import targets


# Init some values to test development
targets.init_test_target_values()

# A final class to handle data between controls
class Controller:
    items: list = targets.pickle_loader('data/objects/target_data.pkl')
    counter: int = len(items)

    print("current items list:")
    print(items)

    @staticmethod
    def get_items():
        return Controller.items
    
    @staticmethod
    def set_items(data: object):
        Controller.items[Controller.counter] = data
        Controller.counter += 1

# A class for the header bar of the text field page
class Header(Container):
    def __init__(self, page: ft.Page, dt: ft.DataTable):
        super().__init__(on_hover=self.toggle_search)
        self.bgcolor = FG
        self.height = 60
        # Create datatable attribute
        self.dt = dt

        # create a textfield for search/filter
        self.search_value: TextField = search_field(self.filter_table)

        # create a searchbox
        self.search: Container = search_bar(self.search_value)

        # define other class attributes
        self.name: Any = ft.Container(
                on_click=lambda _: page.go('/'),
                content=ft.Text('pyASM')
                )
        self.avatar = ft.IconButton("person")

        # Compile the attributes inside the header container
        self.content = ft.Row(
            alignment="spaceBetween",
            controls=[
                self.name,
                self.search,
                self.avatar,
            ]

        )

    # A method that toggles search box visibility
    def toggle_search(self,e: ft.HoverEvent):
        self.search.opacity = 1 if e.data == 'true' else 0
        self.update()

    # TODO A method for filtering data
    def filter_table(self, e):
        ...


# A class for the form that will display the target data
class Form(Container):
    def __init__(self, page: ft.Page, dt: ft.DataTable):
        super().__init__()
        # Create datatable attribute
        self.dt = dt


        # Define 4 row text field?
        self.row1_value: TextField = text_field()
        self.row2_value: TextField = text_field()
        self.row3_value: TextField = text_field()
        self.row4_value: TextField = text_field()

        # define and wrap these in a container
        self.row1: Container = text_field_container(
            True, "Row One", self.row1_value
        )
        self.row2: Container = text_field_container(
            True, "Row Two", self.row2_value
        )
        self.row3: Container = text_field_container(
            True, "Row Three", self.row3_value
        )
        self.row4: Container = text_field_container(
            True, "Row Four", self.row4_value
        )

        # define a button to submit the data
        self.submit = ft.ElevatedButton(
            text = "Add",
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
            on_click=self.submit_data,
        )

        # define a button to clear the data
        self.clear = ft.ElevatedButton(
            text = "Clear",
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
            on_click=self.clear_entries,
        )

        # compile all class attributes into the class container
        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[self.row1]),
                ft.Row(controls=[self.row2, self.row3, self.row4]),
                ft.Row(controls=[self.clear, self.submit], spacing=1, alignment="end"),
            ]
        )



    # TODO a method that writes data from a text field to the targets object file
    def submit_data(self, e: ft.TapEvent):
        ...

    # Method to clear current strings in text field containers
    def clear_entries(self, e: ft.TapEvent):
        self.row1_value.value = ""
        self.row2_value.value = ""
        self.row3_value.value = ""
        self.row4_value.value = ""

        self.content.update()


column_names = ["Friendly Name", "IP"]

data_table_style = {
    "expand": True,
    "border": ft.border.all(2,ACCENT),
    "border_radius": 8,
    "horizontal_lines": ft.border.BorderSide(1,ACCENT),
    "columns": [
        ft.DataColumn(ft.Text(index, size=12, color="white", weight="bold"))
                        for index in column_names
    ]
}

class DataTable(ft.DataTable):
    def __init__(self):
        super().__init__(**data_table_style) 

        # Create attribute to get items
        self.df = Controller.get_items()

    def fill_data_table(self):
        # clear current table for new/updated batch
        self.rows = []

        # split out the target object values into cells
        for value in self.df:
            data = ft.DataRow()
            data.cells = [
                ft.DataCell(
                    ft.Text(value.name, color="black")
                ),
                ft.DataCell(
                    ft.Text(value.value, color="black")
                ) 
            ]

            self.rows.append(data)

        self.update()




class Targets_Page(Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.table = DataTable()
        self.header = Header(page, dt=self.table)
        self.form = Form(page, dt=self.table)
        self.expand = True
        self.bgcolor = SECOND_BG
        self.content = ft.Column(
            expand=True,
            controls=[
                # header ...
                self.header,
                ft.Divider(height=2, color="transparent"),
                # form ...
                self.form,
                ft.Column(
                    scroll="hidden",
                    expand=True,
                    controls=[
                        # table ...
                        ft.Row(controls=[self.table]),
                    ]
                )
            ]
        )
        self.update()
        # TODO fix the below code line from breaking the targets page
        # self.table.fill_data_table()

# A method that creates and returns a textfield
def search_field(function: callable):
    return ft.TextField(
        border_color=ACCENT,
        height=20,
        text_size=14,
        hint_text="Search Targets",
        on_change=function,
    )

# A method that adds a container to the search_field
def search_bar(control: ft.TextField) -> Container:
    return ft.Container(
        width=350,
        animate_opacity=300,
        content=ft.Row(
            spacing=10,
            vertical_alignment="center",
            controls=[
                ft.Icon(
                    name=ft.icons.SEARCH_ROUNDED,
                    size=17,
                ),
                control,
            ]
        )
    )

# A method that creates and returns a textfield
def text_field():
    return TextField(
        color="black",
        cursor_color="black",
        height=20,
        text_size=13,
        border_color="transparent",
    )

# A method that creates a container to place a text field in
def text_field_container(expand: bool | int, name: str, control: ft.TextField ) -> Container:
    return ft.Container(
        expand=expand,
        height=45,
        bgcolor=ACCENT_DARKER,
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(
                    value=name,
                    size=9,
                    weight='bold',
                    color="white"
                ),
                control
            ]
        )

    )

# source
# https://www.youtube.com/watch?v=Xl7BXURZ_HI&list=PLDHA4931gtc4g57ARUkh5AeeSmfdI8WhF&index=1
# at 19:12