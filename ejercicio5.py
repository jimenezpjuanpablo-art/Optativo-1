class Vehiculo:
    #Clase para representar un vehículo a la venta en una agencia automotriz.

    def __init__(self, marca: str, modelo: str, anio: int, precio: float):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def obtener_descripcion_comercial(self) -> str:
        #Genera el texto promocional formateado para publicación.
        return f"{self.marca} {self.modelo} {self.anio} - {self.precio:,.0f} Gs."

    def __str__(self) -> str:
        return self.obtener_descripcion_comercial()


if __name__ == "__main__":
    # Creación de dos vehículos
    v1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
    v2 = Vehiculo("Hyundai", "HB20", 2022, 78000000)

    print(v1)
    print(v2)