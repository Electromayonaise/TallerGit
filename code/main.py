class Main:
    def __init__(self):
        self.vehiculos = []

    # Agregar vehículo a la lista
    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
        else:
            raise TypeError("El objeto debe ser de la clase Vehiculo")

    # Buscar vehículos por año
    def buscar_vehiculos_por_año(self, año):
        return [vehiculo for vehiculo in self.vehiculos if vehiculo.get_año() == año]