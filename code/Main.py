
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


    def print_vehicules(self, list_vehicules):
        if not list_vehicules:
            print("No hay vehículos en la vehiculos.")
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
            print("1. Imprimir vehiculos")
            print("2. Filtrar vehiculos por año")
            print("3. Agregar vehiculo")
	    print("9. Salir del menu\n")
	    opcion = input("Escoja una opcion")
            if opcion == '1':
    	        main().print_vehicules(self.vehiculos)
	    elif opcion == '2':
	        main.menu_year_filter()
	    elif opcion == '3':
		main.menu_add_vehicule()
	    elif opcion == '9':
		running = False
	    else:
		continue

    def menu_year_filter(self):
	print("\nEscoja una opcion de filtrado")
	print("1. Año concreto")
	print("2. Rango de años")

	filter_option = input("Escoja una opcion")
	if filter_option == '1':
	    main().search_vehicule_concrete_year()
	elif filter_option == '2':
	    low_end = int(input("Ingrese el año desde el cual quiere buscar"))
	    high_end = int(input("Ingrese el año hasta el cual quiere buscar"))
	    main.print_vehicules(main.filter_vehicules_range(low_end, high_end))
	else:
	    print("\n Opcion invalida")
	    continue

    def filter_vehicules_range(self, low_end, high_end):
	current_vehicules = []
	vehicule for vehicule in self.vehiculos:
	    current_year = vehicule.get_año()
	    if current_year >= low_end && current_year <= high_end:
		current_vehicules.append(vehicule)
	return current_vehicules

    def menu_add_vehicule(self):
            print("\n----- Agregar Vehículo -----")

            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            try:
                año = int(input("Ingrese el año del vehículo: "))
            except ValueError:
                print("Año no válido, por favor ingrese un número.")
                continue
            try:
                kilometraje = int(input("Ingrese el kilometraje del vehículo: "))
            except ValueError:
                print("Kilometraje no válido, por favor ingrese un número.")
                continue

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
                continue

            vehiculo = Vehiculo(marca, modelo, año, kilometraje, estado_actual, tipo_combustible)
            main.agregar_vehiculo(vehiculo)
            print("\n¡Vehículo agregado con éxito!")
            print(vehiculo)


if __name__ == "__main__":

    main = Main()
    main.menu()

