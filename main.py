from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva


try:

    cliente1 = Cliente("Yuri", 22, "yuri@gmail.com")

    servicio1 = ReservaSala("Sala Premium", 100)

    reserva1 = Reserva(cliente1, servicio1, 2)

    cliente1.mostrar_datos()

    print(servicio1.descripcion())

    print(f"Costo total: {servicio1.calcular_costo()}")

    reserva1.confirmar()

except Exception as e:
    print(f"Ocurrió un error: {e}")