from collections import Counter
class RegistroPacientes:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        self.pacientes.sort(key=lambda x: x.nombre)  # Ordenar la lista por nombre
        print(f'Paciente {paciente.nombre} agregado y lista ordenada correctamente.')

    def __buscar_por_nombre_recursiva(self, nombre, inicio, fin):
        if inicio <= fin:
            medio = (inicio + fin) // 2
            if self.pacientes[medio].nombre.lower() == nombre:
                return self.pacientes[medio]
            elif self.pacientes[medio].nombre.lower() < nombre:
                return self.__buscar_por_nombre_recursiva(nombre, medio + 1, fin)
            else:
                return self.__buscar_por_nombre_recursiva(nombre, inicio, medio - 1)
        else:
            return 0

    def buscar_por_nombre(self, nombre):
        # Llamada inicial
        nombre_minusculas = nombre.lower()
        return self.__buscar_por_nombre_recursiva(nombre_minusculas, 0, len(self.pacientes) - 1)

    def __buscar_por_diagnostico_recursivo(self, lista, diagnostico, inicio, fin):
        if inicio <= fin:
            medio = (inicio + fin) // 2
            if lista[medio].diagnostico.lower() == diagnostico:
                return lista[medio]
            elif lista[medio].diagnostico.lower() < diagnostico:
                return self.__buscar_por_diagnostico_recursivo(lista, diagnostico, medio + 1, fin)
            else:
                return self.__buscar_por_diagnostico_recursivo(lista, diagnostico, inicio, medio - 1)
        else:
            return 0

    def buscar_por_diagnostico(self, diagnostico):
        # Ordenar por diagnóstico antes de la búsqueda
        lista_ordenada = sorted(self.pacientes, key=lambda x: x.diagnostico)
        diagnostico_minusculas = diagnostico.lower()
        return self.__buscar_por_diagnostico_recursivo(lista_ordenada, diagnostico_minusculas, 0, len(lista_ordenada) - 1)

    def mostrar_lista_pacientes(self):
        for paciente in self.pacientes:
            print(f'Nombre: {paciente.nombre}, Edad: {paciente.edad}, Género: {paciente.genero}, Teléfono: {paciente.telefono}, Diagnóstico: {paciente.diagnostico}')

    def eliminar_paciente(self, nombre):
        pacientes_filtrados = [paciente for paciente in self.pacientes if paciente.nombre.lower() != nombre.lower()]
        if len(pacientes_filtrados) < len(self.pacientes):
            print(f'Paciente {nombre} eliminado correctamente.')
            self.pacientes = pacientes_filtrados
        else:
            print(f'No se encontró al paciente {nombre}.')
    
    def calcular_edad_promedio(self):
        if not self.pacientes:
            return 0  # Evitar división por cero si no hay pacientes
        edad_promedio = sum(paciente.edad for paciente in self.pacientes) / len(self.pacientes)
        return edad_promedio

    def calcular_numero_total_pacientes(self):
        return len(self.pacientes)

    def calcular_edad_minima(self):
        if not self.pacientes:
            return None
        return min(paciente.edad for paciente in self.pacientes)

    def calcular_edad_maxima(self):
        if not self.pacientes:
            return None
        return max(paciente.edad for paciente in self.pacientes)

    def calcular_genero_mas_comun(self):
        if not self.pacientes:
            return None
        generos = [paciente.genero for paciente in self.pacientes]
        conteo_generos = Counter(generos)
        genero_mas_comun = conteo_generos.most_common(1)[0][0]
        return genero_mas_comun
