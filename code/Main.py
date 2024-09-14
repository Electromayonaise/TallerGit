from Vehiculo import Vehiculo

class Main:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
        else:
            raise TypeError("El objeto debe ser de la clase Vehiculo")


    def buscar_vehiculo_anio_concreto(self, anio):
        vehiculos_actuales = []
        for vehicule in self.vehiculos:
            if vehicule.get_anio() == anio:
                vehiculos_actuales.append(vehicule)
        return vehiculos_actuales

    def filtrar_vehiculos_rango(self, limite_inf, limite_sup):
        vehiculos_actuales = []
        for vehiculo in self.vehiculos:
            current_year = vehiculo.get_año()
            if limite_inf <= current_year <= limite_sup:
                vehiculos_actuales.append(vehiculo)
        return vehiculos_actuales

    def filtrar_vehiculos_por_comparacion(self, anio, criterio):
        vehiculos_actuales = []
        for vehiculo in self.vehiculos:
            current_year = vehiculo.get_anio()
            if criterio == 'mayor':
                if current_year > anio:
                    vehiculos_actuales.append(vehiculo)
            elif criterio == 'mayor_igual':
                if current_year >= anio:
                    vehiculos_actuales.append(vehiculo)
            elif criterio == 'menor':
                if current_year < anio:
                    vehiculos_actuales.append(vehiculo)
            elif criterio == 'menor_igual':
                if current_year <= anio:
                    vehiculos_actuales.append(vehiculo)
            else:
                raise ValueError("Criterio no válido. Debe ser 'mayor', 'menor', 'mayor_igual' o 'menor_igual'.")
        return vehiculos_actuales

    def imprimir_vehiculos(self, lista_vehiculos):
        if not lista_vehiculos:
            print("No hay vehículos para mostrar.")
            return

        for vehicule in lista_vehiculos:
            print(f"Marca: {vehicule.get_marca()}")
            print(f"Modelo: {vehicule.get_modelo()}")
            print(f"Año: {vehicule.get_anio()}")
            print(f"Kilometraje: {vehicule.get_kilometraje()}")
            print(f"Estado actual: {vehicule.get_estado_actual()}")
            print(f"Tipo de combustible: {vehicule.get_tipo_combustible()}")
            print(f"Color: {vehicule.get_color()}")
            print(f"Potencia: {vehicule.get_potencia()}")
            print("-" * 30)

    def menu(self):
        running = True
        while running:
            print("\n---- Bienvenido ----")
            print("1. Imprimir vehículos")
            print("2. Filtrar vehículos por año")
            print("3. Agregar vehículo")
            print("4. Salir del menú\n")
            opcion = input("Escoja una opción: ")

            if opcion == '1':
                self.imprimir_vehiculos(self.vehiculos)
            elif opcion == '2':
                main.menu_filtro_anio()
            elif opcion == '3':
                self.menu_agregar_vehiculo()
            elif opcion == '9':
                running = False
            else:
                print("Opción no válida, intente de nuevo.")

    def menu_filtro_anio(self):
        print("\nEscoja una opcion de filtrado")
        print("1. Año concreto")
        print("2. Rango de años")
        print("3. Mayor a un año")
        print("4. Menor a un año")
        print("5. Mayor o igual a un año")
        print("6. Menor o igual a un año")

        opcion_filtro = input("Escoja una opción: ")

        if opcion_filtro == '1':
            anio_concreto = int(input("Ingrese el año que desea buscar \n"))
            resultado_busqueda = main.buscar_vehiculo_anio_concreto(anio_concreto)
            if not resultado_busqueda:
                print("No se encontraron vehiculos con ese año")
            else:
                main.imprimir_vehiculos(resultado_busqueda)
        elif opcion_filtro == '2':
            try:
                limite_inf = int(input("Ingrese el año desde el cual quiere buscar: "))
                limite_sup = int(input("Ingrese el año hasta el cual quiere buscar: "))
                vehiculos_filtrados = self.filtrar_vehiculos_rango(limite_inf, limite_sup)
                self.imprimir_vehiculos(vehiculos_filtrados)
            except ValueError:
                print("Años no válidos, por favor ingrese números.")
        
        elif opcion_filtro == '3':
            try:
                año = int(input("Ingrese el año de referencia: "))
                vehiculos_filtrados = self.filtrar_vehiculos_por_comparacion(año, 'mayor')
                self.imprimir_vehiculos(vehiculos_filtrados)
            except ValueError:
                print("Año no válido, por favor ingrese un número.")
        
        elif opcion_filtro == '4':
            try:
                año = int(input("Ingrese el año de referencia: "))
                vehiculos_filtrados = self.filtrar_vehiculos_por_comparacion(año, 'menor')
                self.imprimir_vehiculos(vehiculos_filtrados)
            except ValueError:
                print("Año no válido, por favor ingrese un número.")
        
        elif opcion_filtro == '5':
            try:
                año = int(input("Ingrese el año de referencia: "))
                vehiculos_filtrados = self.filtrar_vehiculos_por_comparacion(año, 'mayor_igual')
                self.imprimir_vehiculos(vehiculos_filtrados)
            except ValueError:
                print("Año no válido, por favor ingrese un número.")
        
        elif opcion_filtro == '6':
            try:
                año = int(input("Ingrese el año de referencia: "))
                vehiculos_filtrados = self.filtrar_vehiculos_por_comparacion(año, 'menor_igual')
                self.imprimir_vehiculos(vehiculos_filtrados)
            except ValueError:
                print("Año no válido, por favor ingrese un número.")
        
        else:
            print("\n Opcion invalida")

    def filtrar_vehiculos_rango(self, limite_inf, limite_sup):
        vehiculos_actuales = []
        for vehicule in self.vehiculos:
            current_year = vehicule.get_anio()
            if current_year >= limite_inf and current_year <= limite_sup:
                vehiculos_actuales.append(vehicule)
        return vehiculos_actuales

    def menu_agregar_vehiculo(self):
        print("\n----- Agregar Vehículo -----")

        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        
        try:
            anio = int(input("Ingrese el año del vehículo: "))
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

        color = input("Ingrese el color del vehículo: ")

        potencia = input("Ingrese la potencia del vehículo: ")

        vehiculo = Vehiculo(marca, modelo, anio, kilometraje, estado_actual, tipo_combustible, color, potencia)
        self.agregar_vehiculo(vehiculo)
        print("\n¡Vehículo agregado con éxito!")

if __name__ == "__main__":
    main = Main()
    main.menu()
