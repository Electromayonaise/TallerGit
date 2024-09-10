from Vehiculo import Vehiculo

class Main:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
        else:
            raise TypeError("El objeto debe ser de la clase Vehiculo")

    def search_vehicule_concrete_year(self, año):
        return [vehiculo for vehiculo in self.vehiculos if vehiculo.get_año() == año]

    def filter_vehicules_range(self, low_end, high_end):
        return [vehiculo for vehiculo in self.vehiculos if low_end <= vehiculo.get_año() <= high_end]

    def filter_vehicules_by_comparison(self, año, criterio):
        if criterio == 'mayor':
            return [vehiculo for vehiculo in self.vehiculos if vehiculo.get_año() > año]
        elif criterio == 'menor':
            return [vehiculo for vehiculo in self.vehiculos if vehiculo.get_año() < año]
        else:
            raise ValueError("Criterio no válido. Debe ser 'mayor' o 'menor'.")

    def print_vehicules(self, list_vehicules):
        if not list_vehicules:
            print("No hay vehículos para mostrar.")
            return

        for vehicule in list_vehicules:
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
            print("1. Imprimir vehículos")
            print("2. Filtrar vehículos por año")
            print("3. Agregar vehículo")
            print("9. Salir del menú\n")
            opcion = input("Escoja una opción: ")

            if opcion == '1':
                self.print_vehicules(self.vehiculos)
            elif opcion == '2':
                self.menu_year_filter()
            elif opcion == '3':
                self.menu_add_vehicule()
            elif opcion == '9':
                running = False
            else:
                print("Opción no válida, intente de nuevo.")

    def menu_year_filter(self):
        print("\nEscoja una opción de filtrado")
        print("1. Año concreto")
        print("2. Rango de años")
        print("3. Mayor a un año")
        print("4. Menor a un año")

        filter_option = input("Escoja una opción: ")

        if filter_option == '1':
            try:
                año = int(input("Ingrese el año concreto: "))
                vehiculos_filtrados = self.search_vehicule_concrete_year(año)
                self.print_vehicules(vehiculos_filtrados)
            except ValueError:
                print("Año no válido, por favor ingrese un número.")
        
        elif filter_option == '2':
            try:
                low_end = int(input("Ingrese el año desde el cual quiere buscar: "))
                high_end = int(input("Ingrese el año hasta el cual quiere buscar: "))
                vehiculos_filtrados = self.filter_vehicules_range(low_end, high_end)
                self.print_vehicules(vehiculos_filtrados)
            except ValueError:
                print("Año no válido, por favor ingrese números válidos.")

        elif filter_option == '3':
            try:
                año = int(input("Ingrese el año de referencia: "))
                vehiculos_filtrados = self.filter_vehicules_by_comparison(año, 'mayor')
                self.print_vehicules(vehiculos_filtrados)
            except ValueError:
                print("Año no válido, por favor ingrese un número.")
        
        elif filter_option == '4':
            try:
                año = int(input("Ingrese el año de referencia: "))
                vehiculos_filtrados = self.filter_vehicules_by_comparison(año, 'menor')
                self.print_vehicules(vehiculos_filtrados)
            except ValueError:
                print("Año no válido, por favor ingrese un número.")
        
        else:
            print("\nOpción inválida. Intente de nuevo.")

    def menu_add_vehicule(self):
        print("\n----- Agregar Vehículo -----")

        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")

        try:
            año = int(input("Ingrese el año del vehículo: "))
        except ValueError:
            print("Año no válido, por favor ingrese un número.")
            return

        try:
            kilometraje = int(input("Ingrese el kilometraje del vehículo: "))
        except ValueError:
            print("Kilometraje no válido, por favor ingrese un número.")
            return

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
            tipo_combustible = "Eléctrico"
        elif opcion_combustible == '3':
            tipo_combustible = "Diésel"
        else:
            print("Opción no válida.")
            return

        vehiculo = Vehiculo(marca, modelo, año, kilometraje, estado_actual, tipo_combustible)
        self.agregar_vehiculo(vehiculo)
        print("\n¡Vehículo agregado con éxito!")

if __name__ == "__main__":
    main = Main()
    main.menu()
