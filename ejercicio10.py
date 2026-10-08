class Producto:
    #Representa los datos básicos de un producto en la tienda.

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio


class ItemCarrito:
    #Relaciona un Producto con una cantidad comprada.

    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self) -> float:
        """Calcula el costo del ítem según su cantidad."""
        return self.producto.precio * self.cantidad


class CarritoCompras:
    #Contiene la lista de ítems agregados y calcula el total general.

    def __init__(self):
        self.items: list[ItemCarrito] = []

    def agregar_item(self, producto: Producto, cantidad: int) -> None:
        #Crea un ItemCarrito y lo añade a la compra.
        if cantidad > 0:
            self.items.append(ItemCarrito(producto, cantidad))

    def calcular_total(self) -> float:
        #Suma los subtotales de todos los ítems del carrito.
        return sum(item.calcular_subtotal() for item in self.items)

    def __str__(self) -> str:
        lineas = ["=== Detalle del Carrito de Compras ==="]
        if not self.items:
            lineas.append("El carrito está vacío.")
        else:
            for item in self.items:
                p = item.producto
                subtotal = item.calcular_subtotal()
                lineas.append(f" - {p.nombre} x{item.cantidad} @ Gs. {p.precio:,.0f} = Gs. {subtotal:,.0f}")
            lineas.append("-------------------------------------")
            lineas.append(f"Total a Pagar: Gs. {self.calcular_total():,.0f}")
        return "\n".join(lineas)


if __name__ == "__main__":
    p1 = Producto("Teclado Mecánico", 350000)
    p2 = Producto("Mouse Óptico", 120000)
    p3 = Producto("Monitor 24''", 1100000)

    carrito = CarritoCompras()
    carrito.agregar_item(p1, 1)
    carrito.agregar_item(p2, 2)
    carrito.agregar_item(p3, 1)

    print(carrito)