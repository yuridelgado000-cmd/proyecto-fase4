from excepciones import ErrorCliente
class Cliente:
    def __init__(self, nombre, edad, correo):
        if not nombre.strip():
            raise ErrorCliente(
                "El nombre no puede estar vacío"
            )
        if edad < 18:
            raise ErrorCliente(
                "El cliente debe ser mayor de edad"
            )
        if "@" not in correo:
            raise ErrorCliente(
                "Correo electrónico inválido"
            )
        self.__nombre = nombre
        self.__edad = edad
        self.__correo = correo
    def mostrar_datos(self):
        print(f"Cliente: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Correo: {self.__correo}")