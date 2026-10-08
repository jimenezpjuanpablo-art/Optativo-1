class LineaTelefonica:
    #Controla el consumo de datos de una línea móvil según el plan contratado.

    def __init__(self, titular: str, gigas_plan: float):
        self.titular = titular
        self.gigas_plan = gigas_plan
        self.gigas_consumidos = 0.0

    def registrar_consumo(self, gigas: float) -> None:
        #Suma consumos y detecta el agotamiento del paquete contratado.
        if gigas <= 0:
            print("⚠ El consumo debe ser un valor positivo.")
            return

        disponibles = self.obtener_gigas_disponibles()
        if disponibles == 0:
            print("❌ El paquete de datos ya está agotado. No se puede navegar más.")
            return

        if gigas > disponibles:
            print(f"🚨 ALERTA: Consumo de {gigas:.2f} GB supera el saldo disponible ({disponibles:.2f} GB). Paquete agotado.")
            self.gigas_consumidos = self.gigas_plan
        else:
            self.gigas_consumidos += gigas
            print(f"✓ Consumo registrado: {gigas:.2f} GB.")

    def obtener_gigas_disponibles(self) -> float:
        #Retorna el margen disponible restante.
        return max(0.0, self.gigas_plan - self.gigas_consumidos)

    def __str__(self) -> str:
        disponibles = self.obtener_gigas_disponibles()
        return (
            f"Línea de {self.titular} | Plan: {self.gigas_plan:.1f} GB | "
            f"Consumido: {self.gigas_consumidos:.2f} GB | Disponible: {disponibles:.2f} GB"
        )


if __name__ == "__main__":
    linea = LineaTelefonica("Fernando Ruiz", gigas_plan=10.0)
    print(linea)

    print("\n--- Registrando Consumos ---")
    linea.registrar_consumo(3.5)
    print(linea)

    linea.registrar_consumo(7.0)  # Supera el saldo y agota el plan
    print(linea)

    linea.registrar_consumo(1.0)  # Bloquea el consumo extra