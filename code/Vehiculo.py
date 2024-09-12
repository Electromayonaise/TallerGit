class Vehiculo:

    COMBUSTIBLES_PERMITIDOS = {"Gasolina", "Diesel", "Eléctrico"}

    def __init__(self, marca, modelo, año, kilometraje, estado_actual, tipo_combustible, potencia):
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._kilometraje = kilometraje
        self._estado_actual = estado_actual
        self._tipo_combustible = tipo_combustible
        self._potencia = potencia

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_año(self):
        return self._año

    def get_kilometraje(self):
        return self._kilometraje

    def get_estado_actual(self):
        return self._estado_actual

    def get_tipo_combustible(self):
        return self._tipo_combustible
    
    def get_potencia(self):
        return self._potencia 

    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_año(self, año):
        self._año = año

    def set_kilometraje(self, kilometraje):
        self._kilometraje = kilometraje

    def set_estado_actual(self, estado_actual):
        self._estado_actual = estado_actual

    def set_tipo_combustible(self, tipo_combustible):
        self._tipo_combustible = tipo_combustible

    def set_potencia(self, potencia):
        if potencia < 0:
            raise ValueError("La potencia no puede ser negativa")
        self._potencia = potencia

    def tipo_combustible(self, valor: str) -> None:
        if valor not in Vehiculo.COMBUSTIBLES_PERMITIDOS:
            raise ValueError(f"Tipo de combustible no válido. Debe ser uno de: {', '.join(Vehiculo.COMBUSTIBLES_PERMITIDOS)}")
        self._tipo_combustible = valor
