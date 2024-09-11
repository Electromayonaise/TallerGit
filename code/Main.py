
from Vehiculo import Vehiculo
class Main:
    def __init__(self):
        self.vehiculos = []


    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
        else:
            raise TypeError("El objeto debe ser de la clase Vehiculo")


    def buscar_vehiculo_año_concreto(self, año):
        vehiculos_actuales = []
        for vehicule in self.vehiculos:
            if vehicule.get_año() == año:
                vehiculos_actuales.append(vehicule)
        return vehiculos_actuales


    def imprimir_vehiculos(self, lista_vehiculos):
        if not lista_vehiculos:
            print("No hay vehículos en la vehiculos.")
            return

        for vehicule in lista_vehiculos:
            print(f"Marca: {vehicule.get_marca()}")
            print(f"Modelo: {vehicule.get_modelo()}")
            print(f"Año: {vehicule.get_año()}")
            print(f"Kilometraje: {vehicule.get_kilometraje()}")
            print(f"Estado actual: {vehicule.get_estado_actual()}")
            print(f"Tipo de combustible: {vehicule.get_tipo_combustible()}")
            print("-" * 30)


    def menu(self):
        running = True
        while running:
            print("\n---- Bienvenido ----")
            print("1. Imprimir vehiculos")
            print("2. Filtrar vehiculos por año")
            print("3. Agregar vehiculo")
            print("9. Salir del menu\n")
            opcion = input("Escoja una opcion \n")
            if opcion == '1':
                main.imprimir_vehiculos(self.vehiculos)
            elif opcion == '2':
                main.menu_filtro_año()
            elif opcion == '3':
                main.menu_agregar_vehiculo()
            elif opcion == '9':
                running = False
            else:
                print("\nOpcion invalida")

    def menu_filtro_año(self):
        print("\nEscoja una opcion de filtrado")
        print("1. Año concreto")
        print("2. Rango de años")

        opcion_filtro = input("Escoja una opcion \n")
        if opcion_filtro == '1':
            año_concreto = int(input("Ingrese el año que desea buscar \n"))
            resultado_busqueda = main.buscar_vehiculo_año_concreto(año_concreto)
            if not resultado_busqueda:
                print("No se encontraron vehiculos con ese año")
            else:
                main.imprimir_vehiculos(resultado_busqueda)
        elif opcion_filtro == '2':
            limite_inf = int(input("Ingrese el año desde el cual quiere buscar \n"))
            limite_sup = int(input("Ingrese el año hasta el cual quiere buscar \n"))
            resultado_busqueda = (main.filtrar_vehiculos_rango(limite_inf, limite_sup))
            if not resultado_busqueda:
                print("No se encontraron vehiculos en ese rango")
            else:
                main.imprimir_vehiculos(resultado_busqueda)
        else:
            print("\n Opcion invalida")

    def filtrar_vehiculos_rango(self, limite_inf, limite_sup):
        vehiculos_actuales = []
        for vehicule in self.vehiculos:
            current_year = vehicule.get_año()
            if current_year >= limite_inf and current_year <= limite_sup:
                vehiculos_actuales.append(vehicule)
        return vehiculos_actuales

    def menu_agregar_vehiculo(self):
        print("\n----- Agregar Vehículo -----")

        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        try:
            año = int(input("Ingrese el año del vehículo: "))
        except ValueError:
            print("Año no válido, por favor ingrese un número.")
        try:
            kilometraje = int(input("Ingrese el kilometraje del vehículo: "))
        except ValueError:
            print("Kilometraje no válido, por favor ingrese un número.")

        estado_actual = input("Ingrese el estado actual del vehículo: ")

        print("\nSeleccione el tipo de combustible:")
        print("1. Gasolina")
        print("2. Eléctrico")
        print("3. Diésel")

        tipo_combustible = None
        opcion_combustible = input("Opción (1/2/3): ")
        if opcion_combustible == '1':
            tipo_combustible = "Gasolina"
        elif opcion_combustible == '2':
            tipo_combustible = "Electrico"
        elif opcion_combustible == '3':
            tipo_combustible = "Diésel"
        else:
            print("Opción no válida.")
            return

        vehiculo = Vehiculo(marca, modelo, año, kilometraje, estado_actual, tipo_combustible)
        main.agregar_vehiculo(vehiculo)
        print("\n¡Vehículo agregado con éxito!")
        print(vehiculo)


if __name__ == "__main__":

    main = Main()
    main.menu()

