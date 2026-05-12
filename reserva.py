from excepciones import ErrorReserva
import datetime
# Clase que representa una reserva
class Reserva:
    # Constructor de la clase Reserva
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
    # Método para confirmar la reserva
    def confirmar(self):
        # Validación de duración
        if self.duracion <= 0:
            with open("logs.txt", "a") as archivo:
                archivo.write(
                    f"{datetime.datetime.now()} - ERROR: La duración debe ser mayor a cero\n"
                )
            raise ErrorReserva(
                "La duración debe ser mayor a cero"
            )
        self.estado = "Confirmada"
        # Cálculo del costo total
        costo_total = self.servicio.precio * self.duracion
        # Registro en archivo de logs
        with open("logs.txt", "a") as archivo:
            archivo.write(
                f"{datetime.datetime.now()} - Reserva confirmada\n"
            )
        print("Reserva realizada correctamente")
        print(f"Costo total: ${costo_total}")
        print("Proceso finalizado")
    # Método para cancelar una reserva
    def cancelar(self):
        # Verifica si la reserva ya fue confirmada
        if self.estado != "Confirmada":
            raise ErrorReserva(
                "No se puede cancelar una reserva pendiente"
            )
        self.estado = "Cancelada"
        # Registro de cancelación en logs
        with open("logs.txt", "a") as archivo:
            archivo.write(
                f"{datetime.datetime.now()} - Reserva cancelada\n"
            )
        print("Reserva cancelada correctamente")