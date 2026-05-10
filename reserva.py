from excepciones import ErrorReserva
import datetime


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.duracion <= 0:
            with open("logs.txt", "a") as archivo:
                archivo.write(
                    f"{datetime.datetime.now()} - ERROR: La duración debe ser mayor a cero\n"
                )

            raise ErrorReserva(
                "La duración debe ser mayor a cero"
            )

        self.estado = "Confirmada"

        with open("logs.txt", "a") as archivo:
            archivo.write(
                f"{datetime.datetime.now()} - Reserva confirmada\n"
            )

        print("Reserva realizada correctamente")
        print("Proceso finalizado")

    def cancelar(self):

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