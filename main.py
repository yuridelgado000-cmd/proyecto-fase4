from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva

print("----- OPERACIÓN 1 -----")
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
print("\n----- OPERACIÓN 2 -----")
try:
    cliente2 = Cliente("", 17, "correoincorrecto")
except Exception as e:
    print(f"Error detectado: {e}")
print("\n----- OPERACIÓN 3 -----")
try:
    servicio2 = AlquilerEquipo("Computadores", 200)
    reserva2 = Reserva(cliente1, servicio2, -5)
    reserva2.confirmar()
except Exception as e:
    print(f"Error detectado: {e}")
print("\n----- OPERACIÓN 4 -----")
try:
    servicio3 = Asesoria("Asesoría Python", 300)
    reserva3 = Reserva(cliente1, servicio3, 3)
    reserva3.confirmar()
    reserva3.cancelar()
except Exception as e:
    print(f"Error detectado: {e}")