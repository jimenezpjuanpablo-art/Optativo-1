class ProductoStock:
    #Controla el flujo de inventario y emite alertas cuando baja del nivel mínimo.

    def __init__(self, nombre: str, precio: float, stock_inicial: int, stock_minimo: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_inicial
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad: int) -> None:
        """Incrementa las unidades disponibles."""
        if cantidad > 0:
            self.stock += cantidad
            print(f"✓ Reposición: Se ingresaron {cantidad} unidades de {self.nombre}.")
            self._verificar_alerta()
        else:
            print("⚠ Cantidad inválida para ingresar.")

    def registrar_venta(self, cantidad: int) -> bool:
        #Descuenta del stock validando que no quede en negativo.
        if cantidad <= 0:
            print("⚠ Cantidad inválida para la venta.")
            return False

        if cantidad > self.stock:
            print(f"❌ Venta cancelada: Stock insuficiente ({self.stock} disponibles vs {cantidad} solicitadas).")
            return False

        self.stock -= cantidad
        print(f"✓ Venta realizada: {cantidad} unidades de {self.nombre}.")
        self._verificar_alerta()
        return True

    def _verificar_alerta(self) -> None:
        #Método privado auxiliar para notificar sobre stock crítico.
        if self.stock < self.stock_minimo:
            print(f"🚨 ALERTA DE REPOSICIÓN: El stock de '{self.nombre}' ({self.stock} uds.) es inferior al mínimo ({self.stock_minimo} uds.).")

    def __str__(self) -> str:
        return f"Producto: {self.nombre} | Stock Actual: {self.stock} | Stock Mínimo: {self.stock_minimo}"


if __name__ == "__main__":
    prod = ProductoStock("Detergente 500ml", 8500, stock_inicial=10, stock_minimo=5)
    print(prod)

    print("\n--- Simulando Ventas y Reposición ---")
    prod.registrar_venta(6)  # Provoca alerta al bajar a 4 unidades
    print(prod)

    prod.registrar_venta(5)  # Se rechaza por superar las 4 disponibles
    prod.ingresar_mercaderia(10)  # Reabastece el stock
    print(prod)