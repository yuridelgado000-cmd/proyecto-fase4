from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponible


class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self):
        return self.precio * 2

    def descripcion(self):
        return f"Servicio de reserva de sala - ${self.precio}"


class AlquilerEquipo(Servicio):

    def calcular_costo(self):
        return self.precio * 3

    def descripcion(self):
        return f"Servicio de alquiler de equipos - ${self.precio}"


class Asesoria(Servicio):

    def calcular_costo(self):
        return self.precio * 4

    def descripcion(self):
        return f"Servicio de asesoría especializada - ${self.precio}"