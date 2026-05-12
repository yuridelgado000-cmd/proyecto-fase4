class CalculadoraCostos:

    # Método sobrecargado usando parámetros opcionales
    def calcular_total(self, costo_base=0, impuesto=0, descuento=0):

        if costo_base < 0:
            raise ValueError("El costo base no puede ser negativo")

        if impuesto < 0:
            raise ValueError("El impuesto no puede ser negativo")

        if descuento < 0:
            raise ValueError("El descuento no puede ser negativo")

        total = costo_base + impuesto - descuento

        return round(total, 2)

    # Variante usando múltiples argumentos
    def calcular_multiple(self, *costos):

        if len(costos) == 0:
            raise ValueError("Debe ingresar al menos un costo")

        for costo in costos:
            if costo < 0:
                raise ValueError("No se permiten costos negativos")

        return round(sum(costos), 2)