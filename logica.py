from cliente import Cliente
from reserva import Reserva
from servicio import ReservaSala, AlquilerEquipo, Asesoria

from excepciones import (
    ClienteInvalido,
    ErrorReserva,
    ServicioNoDisponible
)


# La clase SistemaReservas se encarga de crear reservas y eliminar reservas

class SistemaReservas:

    def __init__(self):
        self.reserva_actual = None

    # VALIDAR CAMPOS

    def validar_campos(
        self,
        nombre,
        edad,
        correo,
        tipo_servicio,
        nombre_servicio,
        precio,
        duracion
    ):

        # CAMPOS VACÍOS

        if nombre.strip() == "":
            raise ValueError(
                "El nombre no puede estar vacío"
            )

        if str(edad).strip() == "":
            raise ValueError(
                "La edad no puede estar vacía"
            )

        if correo.strip() == "":
            raise ValueError(
                "El correo no puede estar vacío"
            )

        if tipo_servicio.strip() == "":
            raise ValueError(
                "Debe seleccionar un servicio"
            )

        if nombre_servicio.strip() == "":
            raise ValueError(
                "El nombre del servicio no puede estar vacío"
            )

        if str(precio).strip() == "":
            raise ValueError(
                "El precio no puede estar vacío"
            )

        if str(duracion).strip() == "":
            raise ValueError(
                "La duración no puede estar vacía"
            )

        # VALIDAR NOMBRE SOLO TEXTO
    
        if not nombre.replace(" ", "").isalpha():
            raise ValueError(
                "El nombre solo debe contener letras"
            )
        
       
        # VALIDAR SERVICIO SOLO TEXTO
       
        if not nombre_servicio.replace(" ", "").isalpha():
            raise ValueError(
                "El nombre del servicio solo debe contener letras"
            )

        # VALIDAR CAMPOS NUMÉRICOS

        try:
            edad = int(edad)

        except ValueError:
            raise ValueError(
                "La edad debe ser numérica"
            )

        try:
            precio = float(precio)

        except ValueError:
            raise ValueError(
                "El precio debe ser numérico"
            )

        try:
            duracion = int(duracion)

        except ValueError:
            raise ValueError(
                "La duración debe ser numérica"
            )

        # VALIDAR PRECIO
        
        if precio <= 0:
            raise ValueError(
                "El precio debe ser mayor a 0"
            )

        return edad, precio, duracion

    # CREAR RESERVA

    def realizar_reserva(
        self,
        nombre,
        edad,
        correo,
        tipo_servicio,
        nombre_servicio,
        precio,
        duracion
    ):

        # Validar datos
        edad, precio, duracion = self.validar_campos(
            nombre,
            edad,
            correo,
            tipo_servicio,
            nombre_servicio,
            precio,
            duracion
        )

        # Crear cliente
        cliente = Cliente(
            nombre,
            edad,
            correo
        )

        # Crear servicio
        if tipo_servicio == "Reserva Sala":

            servicio = ReservaSala(
                nombre_servicio,
                precio
            )

        elif tipo_servicio == "Alquiler Equipo":

            servicio = AlquilerEquipo(
                nombre_servicio,
                precio
            )

        else:

            servicio = Asesoria(
                nombre_servicio,
                precio
            )

        # Crear reserva
        self.reserva_actual = Reserva(
            cliente,
            servicio,
            duracion
        )

        self.reserva_actual.confirmar()

        total = servicio.calcular_costo()

        resultado = (
            f"===== RESERVA CONFIRMADA =====\n\n"
            f"Cliente: {nombre}\n"
            f"Edad: {edad}\n"
            f"Correo: {correo}\n\n"
            f"Servicio: {servicio.descripcion()}\n"
            f"Duración: {duracion}\n"
            f"Costo total: ${total}\n"
            f"Estado: {self.reserva_actual.estado}"
        )

        return resultado

    # CANCELAR RESERVA

    def cancelar_reserva(self):

        if self.reserva_actual is None:

            raise ErrorReserva(
                "No existe una reserva para cancelar"
            )

        self.reserva_actual.cancelar()

        return "La reserva fue cancelada correctamente."