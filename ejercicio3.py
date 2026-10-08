class Empleado:
    #Clase que representa a un empleado y calcula su compensación anual.

    def __init__(self, nombre: str, cargo: str, salario_mensual: float):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self, incluir_aguinaldo: bool = True) -> float:
        #Calcula el sueldo anual contemplando 12 o 13 meses (aguinaldo paraguayo).
        meses = 13 if incluir_aguinaldo else 12
        return self.salario_mensual * meses

    def __str__(self) -> str:
        anual = self.calcular_salario_anual()
        return (
            f"Empleado: {self.nombre} | Cargo: {self.cargo}\n"
            f"Salario Mensual: Gs. {self.salario_mensual:,.0f} | "
            f"Ingreso Anual (inc. Aguinaldo): Gs. {anual:,.0f}"
        )


if __name__ == "__main__":
    # Instanciación de empleados
    emp1 = Empleado("Ana Martínez", "Desarrolladora Python", 5500000)
    emp2 = Empleado("Carlos López", "Analista de Sistemas", 4800000)

    print(emp1)
    print()
    print(emp2)