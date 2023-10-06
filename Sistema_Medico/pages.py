import flet as ft
from datetime import datetime
from paciente import Paciente
from registro_pacientes import RegistroPacientes

class PageView:
    def __init__(self, page: ft.Page) -> None:
        self.registro_pacientes = RegistroPacientes()
        self.page = page
        self.inputs_add_patients = {
            "nombre": ft.TextField(label="Nombre"),
            "edad": ft.TextField(label="Edad"),
            "genero": ft.TextField(label="Género: M o F"),
            "telefono": ft.TextField(label="Telefono"),
            "diagnostico": ft.TextField(label="Diagnóstico"),
        }
        self.input_name = ft.TextField(label="Por nombre")
        self.input_diagnostico = ft.TextField(label="Por diagnóstico")
        self.msg_error = ft.Text()
        self.patient = ft.Text()
        self.list_patients = ft.Container()
        self.total_users = ft.Text()
        self.avg_age = ft.Text()

    def print(self, list_print):
        columna = ft.Column(spacing=7)
        for i in range(len(list_print)):
            columna.controls.append(ft.Text(f"El paciente {list_print[i].nombre} de género {list_print[i].genero} con {list_print[i].edad} años de edad. \nTeléfono: {list_print[i].telefono} \nDiagnóstico: {list_print[i].diagnostico}"))

        return columna

    def home_page(self):
        container = ft.Container(ft.Column([
                ft.Text("¡Bienvenido al Sistema Médico!"),
                ft.Text(f"Día {datetime.now().date().day} del mes {datetime.now().date().month} de {datetime.now().date().year}")
            ]),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            # height=584,
            # width=250,
            # bgcolor=ft.colors.BLUE_900,
            alignment=ft.alignment.top_center
        )

        return container
    
    def handle_add_submit(self, e):
        self.msg_error.value = ""
        if self.inputs_add_patients["nombre"].value != "" and self.inputs_add_patients["edad"].value != "" and self.inputs_add_patients["genero"].value != "" and self.inputs_add_patients["telefono"].value != "" and self.inputs_add_patients["diagnostico"].value != "":
            paciente = Paciente(
                self.inputs_add_patients["nombre"].value,
                int(self.inputs_add_patients["edad"].value),
                self.inputs_add_patients["genero"].value,
                self.inputs_add_patients["telefono"].value,
                self.inputs_add_patients["diagnostico"].value
            )
            self.registro_pacientes.agregar_paciente(paciente)
            self.inputs_add_patients["nombre"].value = ""
            self.inputs_add_patients["edad"].value = ""
            self.inputs_add_patients["genero"].value = ""
            self.inputs_add_patients["telefono"].value = ""
            self.inputs_add_patients["diagnostico"].value = ""
        else: self.msg_error.value = "Todos los campos debe ser llenados"
        self.page.update()

    def add_patient_page(self):
        self.msg_error.value = ""
        container = ft.Container(ft.Column([
                ft.Text("Ingreso de Pacientes"),
            ]),
            padding=ft.padding.all(15),
            margin=ft.margin.only(top=15),
            alignment=ft.alignment.top_center
        )

        for index, value in self.inputs_add_patients.items():
            container.content.controls.append(value)
        for i, item in self.inputs_add_patients.items():
            item.value = ""

        btn_submit = ft.ElevatedButton("Enviar", on_click=self.handle_add_submit)
        container.content.controls.append(btn_submit)
        container.content.controls.append(self.msg_error)

        return container
    
    def handle_search_submit(self, e):
        self.msg_error.value = ""
        if self.input_name.value == "" and self.input_diagnostico.value == "":
            patient = 1
        if self.input_name.value != "" and self.input_diagnostico.value == "":
            patient = self.registro_pacientes.buscar_por_nombre(self.input_name.value)
        if self.input_name.value == "" and self.input_diagnostico.value != "":
            patient = self.registro_pacientes.buscar_por_diagnostico(self.input_diagnostico.value)
        if self.input_name.value != "" and self.input_diagnostico.value != "":
            patient = 2

        if patient == 0:
            self.msg_error.value = "El paciente no está registrado"
        elif patient == 1:
            self.msg_error.value = "Ingresa valores en un solo campo"
        elif patient == 2:
            self.msg_error.value = "Usa solo un campo"
        else:
            self.patient.value = f"El paciente {patient.nombre} de género {patient.genero} con {patient.edad} años de edad. \nTeléfono: {patient.telefono} \nDiagnóstico: {patient.diagnostico}"
        self.page.update()

    
    def search_patient_page(self):
        self.msg_error.value = ""
        self.input_name.value = ""
        self.input_diagnostico.value = ""
        container = ft.Text("No hay pacientes registrados")
        btn_submit = ft.ElevatedButton("Enviar", on_click=self.handle_search_submit)
        if bool(self.registro_pacientes.pacientes):
            container = ft.Container(ft.Column([
                    ft.Text("Búsqueda de Pcientes"),
                    self.input_name,
                    self.input_diagnostico,
                    btn_submit,
                    self.msg_error,
                    self.patient
                ]),
                padding=ft.padding.all(15),
                margin=ft.margin.only(top=15),
                alignment=ft.alignment.top_center
            )

        return container
    
    def handle_get_submit(self, e):
        self.list_patients.content = self.print(self.registro_pacientes.pacientes)
        self.page.update()
    
    def get_patients_page(self):
        container = ft.Text("No hay pacientes registrados")
        self.list_patients = ft.Container()
        btn_submit = ft.ElevatedButton("Enviar", on_click=self.handle_get_submit)
        if bool(self.registro_pacientes.pacientes):
            container = ft.Container(ft.Column([
                    ft.Text("Ver todos los pacientes"),
                    btn_submit,
                    self.list_patients
                ]),
                padding=ft.padding.all(15),
                margin=ft.margin.only(top=15)
            )

        return container
    
    def handle_delete(self, e):
        self.msg_error.value = ""
        if self.input_name.value != "":
            self.registro_pacientes.eliminar_paciente(self.input_name.value)
            self.input_name.value = ""
        else:
            self.msg_error.value = "Llena el campo"
        self.page.update()
    
    def delete_patient_page(self):
        self.msg_error.value = ""
        self.input_name.value = ""
        container = ft.Text("No hay pacientes registrados")
        btn_submit = ft.ElevatedButton("Enviar", on_click=self.handle_delete)
        if bool(self.registro_pacientes.pacientes):
            container = ft.Container(ft.Column([
                    ft.Text("Eliminar el paciente"),
                    self.input_name,
                    btn_submit,
                    self.msg_error
                ]),
                padding=ft.padding.all(15),
                margin=ft.margin.only(top=15)
            )

        return container
    
    def handle_btn_total(self, e):
        self.total_users.value = self.registro_pacientes.calcular_numero_total_pacientes()
        self.page.update()
    def handle_btn_avg(self, e):
        self.avg_age.value = self.registro_pacientes.calcular_edad_promedio()
        self.page.update()
    
    def statistics_page(self):
        self.total_users.value = ""
        self.avg_age.value = ""
        container = ft.Text("No hay pacientes registrados")
        btn_total = ft.ElevatedButton("Total usuarios", on_click=self.handle_btn_total)
        btn_avg = ft.ElevatedButton("Edad promedio", on_click=self.handle_btn_avg)
        if bool(self.registro_pacientes.pacientes):
            container = ft.Container(ft.Column([
                    btn_total,
                    self.total_users,
                    btn_avg,
                    self.avg_age
                ]),
                padding=ft.padding.all(15),
                margin=ft.margin.only(top=15)
            )

        return container
        