class Main:
    def __init__(self):
        self.flota = []

    def agregar_vehiculo(self, vehiculo):
        self.flota.append(vehiculo)

    def imprimir_vehiculos(self):
        if not self.flota:
            print("No hay vehículos en la flota.")
            return
        
        for vehiculo in self.flota:
            print(f"Marca: {vehiculo.get_marca()}")
            print(f"Modelo: {vehiculo.get_modelo()}")
            print(f"Año: {vehiculo.get_año()}")
            print(f"Kilometraje: {vehiculo.get_kilometraje()}")
            print(f"Estado actual: {vehiculo.get_estado_actual()}")
            print(f"Tipo de combustible: {vehiculo.get_tipo_combustible()}")
            print("-" * 30)  # Separador para mejorar la legibilidad

if __name__ == "__main__":
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 15000, "Buena", "Gasolina")
    vehiculo2 = Vehiculo("Honda", "Civic", 2018, 30000, "Regular", "Diésel")

    main = Main()
    main.agregar_vehiculo(vehiculo1)
    main.agregar_vehiculo(vehiculo2)

    main.imprimir_vehiculos()
