class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje, estado_actual, tipo_combustible):
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._kilometraje = kilometraje
        self._estado_actual = estado_actual
        self._tipo_combustible = tipo_combustible

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
