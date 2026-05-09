from excepciones import ErrorReserva
import datetime
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
    def confirmar(self):
        try:
            if self.duracion <= 0:
                raise ErrorReserva(
                    "La duración debe ser mayor a cero"
                )
            self.estado = "Confirmada"
            with open("logs.txt", "a") as archivo:
                archivo.write(
                    f"{datetime.datetime.now()} - Reserva confirmada\n"
                )
            print("Reserva realizada correctamente")
        except ErrorReserva as e:
            with open("logs.txt", "a") as archivo:
                archivo.write(
                    f"{datetime.datetime.now()} - ERROR: {e}\n"
                )
            print(f"Error: {e}")
        else:
            print("La operación se realizó correctamente")
        finally:
            print("Proceso finalizado")
    def cancelar(self):
        try:
            if self.estado != "Confirmada":
                raise ErrorReserva(
                    "No se puede cancelar una reserva pendiente"
                )
            self.estado = "Cancelada"
            with open("logs.txt", "a") as archivo:
                archivo.write(
                    f"{datetime.datetime.now()} - Reserva cancelada\n"
                )
            print("Reserva cancelada correctamente")
        except ErrorReserva as e:
            with open("logs.txt", "a") as archivo:
                archivo.write(
                    f"{datetime.datetime.now()} - ERROR: {e}\n"
                )
            print(f"Error: {e}")