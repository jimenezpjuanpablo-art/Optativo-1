class Estudiante:
    #Modela la ficha académica de un estudiante con sus calificaciones.

    def __init__(self, nombre: str, nota_minima_aprobacion: float = 2.0):
        self.nombre = nombre
        self.nota_minima = nota_minima_aprobacion
        # Diccionario interno: {"Materia": Nota}
        self.calificaciones: dict[str, float] = {}

    def registrar_nota(self, materia: str, nota: float) -> None:
        #Asigna o actualiza la nota de una materia.
        self.calificaciones[materia] = nota

    def calcular_promedio(self) -> float:
        #Calcula el promedio aritmético de las materias cargadas.
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

    def esta_aprobado(self) -> bool:
        #Compara el promedio con el puntaje mínimo de aprobación.
        return self.calcular_promedio() >= self.nota_minima

    def __str__(self) -> str:
        lineas = [f"=== Boletín de Calificaciones: {self.nombre} ==="]
        if not self.calificaciones:
            lineas.append("Sin materias registradas.")
        else:
            for materia, nota in self.calificaciones.items():
                lineas.append(f" - {materia}: {nota:.1f}")
            
            promedio = self.calcular_promedio()
            condicion = "APROBADO" if self.esta_aprobado() else "REPROBADO"
            lineas.append("--------------------------------------------")
            lineas.append(f"Promedio General: {promedio:.2f}")
            lineas.append(f"Condición Final: {condicion}")
        return "\n".join(lineas)


if __name__ == "__main__":
    estudiante = Estudiante("Beatriz Vera", nota_minima_aprobacion=2.0)
    estudiante.registrar_nota("POO Python", 4.5)
    estudiante.registrar_nota("Base de Datos", 3.8)
    estudiante.registrar_nota("Matemática Discreta", 2.5)

    print(estudiante)