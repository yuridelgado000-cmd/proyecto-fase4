from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponible

from calculadora_costos import CalculadoraCostos

calculadora = CalculadoraCostos()

# Solo costo base
print(calculadora.calcular_total(100))

# Costo + impuesto
print(calculadora.calcular_total(100, 15))

# Costo + impuesto + descuento
print(calculadora.calcular_total(100, 15, 10))

# Múltiples costos
print(calculadora.calcular_multiple(50, 70, 30))

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