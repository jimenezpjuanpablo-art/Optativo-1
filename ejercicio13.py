class Habitacion:
    #Gestiona el estado y cobro de estadías para una habitación de hotel.

    def __init__(self, numero: int, tipo: str, tarifa_por_noche: float):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.ocupada = False  # Estado inicial libre

    def ocupar(self) -> bool:
        #Ocupa la habitación verificando previamente su estado actual.
        if self.ocupada:
            print(f"❌ La habitación {self.numero} ya se encuentra ocupada.")
            return False
        
        self.ocupada = True
        print(f"✓ Habitación {self.numero} ha sido ocupada.")
        return True

    def liberar(self) -> bool:
        #Libera la habitación para nuevos huéspedes.
        if not self.ocupada:
            print(f"⚠ La habitación {self.numero} ya estaba libre.")
            return False
        
        self.ocupada = False
        print(f"✓ Habitación {self.numero} ha sido liberada.")
        return True

    def calcular_costo_estadia(self, noches: int) -> float:
        #Multiplica la tarifa por el total de noches hospedadas.
        if noches <= 0:
            return 0.0
        return self.tarifa_por_noche * noches

    def __str__(self) -> str:
        estado = "Ocupada" if self.ocupada else "Libre"
        return (
            f"Habitación #{self.numero} ({self.tipo}) | "
            f"Tarifa: Gs. {self.tarifa_por_noche:,.0f}/noche | Estado: {estado}"
        )


if __name__ == "__main__":
    hab = Habitacion(104, "Matrimonial VIP", tarifa_por_noche=350000)
    print(hab)

    print("\n--- Ciclo de Estancia ---")
    hab.ocupar()
    hab.ocupar()  # Validación de ocupación duplicada

    # Cálculo de liquidación
    noches = 3
    costo = hab.calcular_costo_estadia(noches)
    print(f"Costo total por {noches} noches: Gs. {costo:,.0f}")

    hab.liberar()
    print(hab)