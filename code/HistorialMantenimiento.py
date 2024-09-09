class HistorialMantenimiento:
    def __init__(self, fecha, descripcion_servicio, kilometraje_en_servicio, costo, nombre_mecanico):
        self._fecha = fecha
        self._descripcion_servicio = descripcion_servicio
        self._kilometraje_en_servicio = kilometraje_en_servicio
        self._costo = costo
        self._nombre_mecanico = nombre_mecanico

    def get_fecha(self):
        return self._fecha

    def get_descripcion_servicio(self):
        return self._descripcion_servicio

    def get_kilometraje_en_servicio(self):
        return self._kilometraje_en_servicio

    def get_costo(self):
        return self._costo

    def get_nombre_mecanico(self):
        return self._nombre_mecanico

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_descripcion_servicio(self, descripcion_servicio):
        self._descripcion_servicio = descripcion_servicio

    def set_kilometraje_en_servicio(self, kilometraje_en_servicio):
        self._kilometraje_en_servicio = kilometraje_en_servicio

    def set_costo(self, costo):
        self._costo = costo

    def set_nombre_mecanico(self, nombre_mecanico):
        self._nombre_mecanico = nombre_mecanico
