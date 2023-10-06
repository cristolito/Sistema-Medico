import flet as ft
from pages import PageView
from navigation_bar import NavigationBar

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Sistema Médico"),
                            center_title=False,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.Row([
                            navigation_bar,
                            ft.Column([page_view.home_page()],expand=True)
                        ])
                    ],
                )
            )
        if page.route == "/addpatient":
            page.views.append(
                ft.View(
                    "/addpatient",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Registro de Pacientes"),
                            center_title=False,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.Row([
                            navigation_bar,
                            ft.Column([page_view.add_patient_page()],expand=True)
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/searchpatient":
            page.views.append(
                ft.View(
                    "/searchpatient",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Buscar un Paciente"),
                            center_title=False,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.Row([
                            navigation_bar,
                            ft.Column([page_view.search_patient_page()],expand=True)
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/getpatients":
            page.views.append(
                ft.View(
                    "/getpatients",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Ver Todos Los Pacientes"),
                            center_title=False,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.Row([
                            navigation_bar,
                            ft.Column([page_view.get_patients_page()],expand=True)
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/deletepatient":
            page.views.append(
                ft.View(
                    "/deletepatient",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Elminar Un Paciente"),
                            center_title=False,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.Row([
                            navigation_bar,
                            ft.Column([page_view.delete_patient_page()],expand=True)
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/statistics":
            page.views.append(
                ft.View(
                    "/statistics",
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text("Estadísticas Sobre Los Pacientes"),
                            center_title=False,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.Row([
                            navigation_bar,
                            ft.Column([page_view.statistics_page()],expand=True)
                        ],expand=True)
                    ],
                )
            )
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    routes = [
        "/",
        "/addpatient",
        "/searchpatient",
        "/getpatients",
        "/deletepatient",
        "/statistics"
    ]

    navigation_bar = NavigationBar(page, routes).build_navigation_bar()
    page_view = PageView(page)
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(target=main)