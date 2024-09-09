class Main:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los vehículos
        self.flota = []

    def agregar_vehiculo(self, vehiculo):
        # Agrega un vehículo a la flota
        self.flota.append(vehiculo)

    def imprimir_vehiculos(self):
        # Imprime las características de todos los vehículos en la flota
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

# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos vehículos
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 15000, "Buena", "Gasolina")
    vehiculo2 = Vehiculo("Honda", "Civic", 2018, 30000, "Regular", "Diésel")

    # Crear una instancia de Main y agregar vehículos
    main = Main()
    main.agregar_vehiculo(vehiculo1)
    main.agregar_vehiculo(vehiculo2)

    # Imprimir los vehículos
    main.imprimir_vehiculos()
