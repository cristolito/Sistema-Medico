import flet as ft

class NavigationBar:
    def __init__(self, page: ft.Page, routes) -> None:
        self.page = page
        self.routes = routes
        self.top_nav_items = [
            ft.NavigationRailDestination(
                label_content=ft.Text("Inicio"),
                label="Boards",
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME_OUTLINED
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Registrar paciente"),
                label="Boards",
                icon=ft.icons.BOOK_OUTLINED,
                selected_icon=ft.icons.BOOK_OUTLINED
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Buscar pacientes"),
                label="Boards",
                icon=ft.icons.PERSON,
                selected_icon=ft.icons.PERSON
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Ver pacientes"),
                label="Boards",
                icon=ft.icons.LIST_ALT_OUTLINED,
                selected_icon=ft.icons.LIST_ALT_OUTLINED
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Eliminar pacientes"),
                label="Boards",
                icon=ft.icons.DELETE_OUTLINE,
                selected_icon=ft.icons.DELETE_OUTLINE
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Estadísticas"),
                label="Boards",
                icon=ft.icons.BAR_CHART,
                selected_icon=ft.icons.BAR_CHART
            )
        ]
    
        self.top_nav_rail = ft.NavigationRail(
                                    selected_index=None,
                                    label_type="all",
                                    on_change=self.top_nav_change,
                                    destinations=self.top_nav_items,
                                    bgcolor=ft.colors.BLUE_GREY,
                                    extended=True,
                                    expand=True,)
        
    def build_navigation_bar(self):
        navigation_bar = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Secciones"),
                ]),
                # divider
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                ft.Container(
                    content=self.top_nav_rail,
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    alignment=ft.alignment.center_right,
                    width=220,
                    height=520
                ),
                # divider
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
            ], tight=True),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=250,
            bgcolor=ft.colors.BLUE_GREY,
        )
        return navigation_bar
                    

    def top_nav_change(self,e):
        self.top_nav_rail.selected_index = e.control.selected_index
        self.page.go(self.routes[e.control.selected_index])
        self.page.update()
        
    