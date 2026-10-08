#Ejercicio 2: Producto de almacén
class Producto:
    #Clase para representar un producto en el stock de un almacén.

    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_valor_total_stock(self) -> float:
        #Calcula el valor monetario total sumando todas las unidades en stock.
        return self.precio * self.stock

    def __str__(self) -> str:
        # Formateo con comas para separar miles en guaraníes
        total = self.calcular_valor_total_stock()
        return (
            f"Producto: {self.nombre} | Precio: Gs. {self.precio:,.0f} | "
            f"Stock: {self.stock} uds. | Valor en Stock: Gs. {total:,.0f}"
        )


if __name__ == "__main__":
    # Creación de productos de almacén
    prod1 = Producto("Yerba Mate 1kg", 18000, 25)
    prod2 = Producto("Aceite de Girasol 1L", 12500, 40)

    print(prod1)
    print(prod2)