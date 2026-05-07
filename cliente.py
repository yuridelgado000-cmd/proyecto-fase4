from excepciones import ClienteInvalido


class Cliente:

    def __init__(self, nombre, edad, correo):
        self.__nombre = nombre
        self.__edad = edad
        self.__correo = correo

        self.validar_datos()

    def validar_datos(self):

        if self.__nombre == "":
            raise ClienteInvalido("El nombre no puede estar vacío")

        if self.__edad < 18:
            raise ClienteInvalido("El cliente debe ser mayor de edad")

        if "@" not in self.__correo:
            raise ClienteInvalido("Correo inválido")

    def mostrar_datos(self):
        print(f"Cliente: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Correo: {self.__correo}")