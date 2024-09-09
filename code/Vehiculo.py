class Vehiculo:
    
    COMBUSTIBLES_PERMITIDOS = {"Gasolina", "Diesel", "Eléctrico"}

    def __init__(self, marca, modelo, año, kilometraje, estado_actual, tipo_combustible, color):
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._kilometraje = kilometraje
        self._estado_actual = estado_actual
        self._color = color
        self.tipo_combustible(tipo_combustible)  # Validar tipo de combustible al inicializar

    # Getters
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

    def get_color(self):
        return self._color

    # Setters
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
        self.tipo_combustible(tipo_combustible)  # Usar el método de validación

    def set_color(self, color):
        self._color = color

    # Método para validar tipo de combustible
    def tipo_combustible(self, valor: str) -> None:
        if valor not in Vehiculo.COMBUSTIBLES_PERMITIDOS:
            raise ValueError(f"Tipo de combustible no válido. Debe ser uno de: {', '.join(Vehiculo.COMBUSTIBLES_PERMITIDOS)}")
        self._tipo_combustible = valor
