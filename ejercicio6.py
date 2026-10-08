class CuentaCorriente:
    #Gestiona el saldo de un cliente asegurando que no gaste más de lo disponible.

    def __init__(self, cliente: str, saldo_inicial: float = 0.0):
        self.cliente = cliente
        # Validación inicial para evitar saldos negativos al construir
        self.saldo = max(0.0, saldo_inicial)

    def acreditar(self, monto: float) -> None:
        #Suma dinero al saldo actual si el monto es mayor a cero.
        if monto > 0:
            self.saldo += monto
            print(f"✓ Acreditados Gs. {monto:,.0f} exitosamente.")
        else:
            print("⚠ Error: El monto a acreditar debe ser mayor a cero.")

    def registrar_consumo(self, monto: float) -> bool:
        #Descuenta un consumo si existen fondos suficientes; de lo contrario lo rechaza.
        if monto <= 0:
            print("⚠ Error: El monto del consumo debe ser positivo.")
            return False
        
        # Validación de fondos
        if monto > self.saldo:
            print(f"❌ Rechazado: Saldo insuficiente para gastar Gs. {monto:,.0f}.")
            return False
        
        self.saldo -= monto
        print(f"✓ Consumo de Gs. {monto:,.0f} registrado.")
        return True

    def __str__(self) -> str:
        return f"Cuenta de {self.cliente} | Saldo Actual: Gs. {self.saldo:,.0f}"


if __name__ == "__main__":
    cuenta = CuentaCorriente("Lucas Ramírez", 100000)
    print(cuenta)

    print("\n--- Secuencia de operaciones ---")
    cuenta.acreditar(150000)
    print(cuenta)

    cuenta.registrar_consumo(80000)
    print(cuenta)

    # Intento de consumo que debe ser rechazado por falta de saldo
    cuenta.registrar_consumo(200000)
    print(cuenta)