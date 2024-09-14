class Vehiculo:

    COMBUSTIBLES_PERMITIDOS = {"Gasolina", "Diesel", "Electrico"}

    def __init__(self, marca, modelo, anio, kilometraje, estado_actual, tipo_combustible, color, potencia):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._kilometraje = kilometraje
        self._estado_actual = estado_actual
        self._color = color
        self.tipo_combustible(tipo_combustible)  # Validar tipo de combustible al inicializar
        self._potencia = potencia

    # Getters
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_anio(self):
        return self._anio

    def get_kilometraje(self):
        return self._kilometraje

    def get_estado_actual(self):
        return self._estado_actual

    def get_tipo_combustible(self):
        return self._tipo_combustible
    
    def get_potencia(self):
        return self._potencia 

    def get_color(self):
        return self._color

    # Setters
    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_anio(self, anio):
        self._anio = anio

    def set_kilometraje(self, kilometraje):
        self._kilometraje = kilometraje

    def set_estado_actual(self, estado_actual):
        self._estado_actual = estado_actual

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible(tipo_combustible)  # Usar el método de validación

    def set_color(self, color):
        self._color = color

    def set_potencia(self, potencia):
        if potencia < 0:
            raise ValueError("La potencia no puede ser negativa")
        self._potencia = potencia

    # Método para validar tipo de combustible
    def tipo_combustible(self, valor: str) -> None:
        if valor not in Vehiculo.COMBUSTIBLES_PERMITIDOS:
            raise ValueError(f"Tipo de combustible no válido. Debe ser uno de: {', '.join(Vehiculo.COMBUSTIBLES_PERMITIDOS)}")
        self._tipo_combustible = valor
