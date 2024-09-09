
from Vehiculo import Vehiculo
class Main:
    def __init__(self):
        self.vehiculos = []


    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
        else:
            raise TypeError("El objeto debe ser de la clase Vehiculo")


    def buscar_vehiculos_por_año(self, año):
        return [vehiculo for vehiculo in self.vehiculos if vehiculo.get_año() == año]


    def imprimir_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos en la vehiculos.")
            return
        
        for vehiculo in self.vehiculos:
            print(f"Marca: {vehiculo.get_marca()}")
            print(f"Modelo: {vehiculo.get_modelo()}")
            print(f"Año: {vehiculo.get_año()}")
            print(f"Kilometraje: {vehiculo.get_kilometraje()}")
            print(f"Estado actual: {vehiculo.get_estado_actual()}")
            print(f"Tipo de combustible: {vehiculo.get_tipo_combustible()}")
            print(f"Potencia {vehiculo.get_potencia()}")
            print(f"Potencia {vehiculo.get_color()}")
            print("-" * 30)  

if __name__ == "__main__":
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 15000, "Buena", "Gasolina")
    vehiculo2 = Vehiculo("Honda", "Civic", 2018, 30000, "Regular", "Diésel")

    main = Main()
    main.agregar_vehiculo(vehiculo1)
    main.agregar_vehiculo(vehiculo2)

    main.imprimir_vehiculos()


        