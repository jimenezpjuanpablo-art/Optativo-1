class Turno:
    #Representa la cita médica de un paciente en una hora específica.

    def __init__(self, paciente: str, hora: str):
        self.paciente = paciente
        self.hora = hora
        self.atendido = False  # Estado inicial por defecto

    def marcar_como_atendido(self) -> None:
        """Cambia el estado del turno a atendido."""
        self.atendido = True

    def __str__(self) -> str:
        estado = "Atendido" if self.atendido else "Pendiente"
        return f"[{self.hora}] Paciente: {self.paciente} | Estado: {estado}"


class Agenda:
    #Gestiona la colección de turnos de una jornada.

    def __init__(self, fecha: str):
        self.fecha = fecha
        self.turnos: list[Turno] = []

    def agendar_turno(self, turno: Turno) -> None:
        #Agrega un objeto Turno a la lista diaria.
        self.turnos.append(turno)

    def listar_pendientes(self) -> list[Turno]:
        #Filtra y devuelve únicamente los turnos con estado atendido = False.
        return [t for t in self.turnos if not t.atendido]

    def __str__(self) -> str:
        lineas = [f"=== Agenda del Día: {self.fecha} ==="]
        pendientes = self.listar_pendientes()
        if not pendientes:
            lineas.append("No hay turnos pendientes.")
        else:
            lineas.append("Turnos Pendientes:")
            for t in pendientes:
                lineas.append(f" - {t}")
        return "\n".join(lineas)


if __name__ == "__main__":
    agenda = Agenda("15/10/2026")

    # Creación y agendamiento de turnos
    t1 = Turno("Roberto Gómez", "08:00")
    t2 = Turno("Laura Insfrán", "08:30")
    t3 = Turno("Sonia Benítez", "09:00")

    agenda.agendar_turno(t1)
    agenda.agendar_turno(t2)
    agenda.agendar_turno(t3)

    print(agenda)

    # Cambio de estado de un turno
    print("\n--- Atendiendo turno de las 08:00 ---")
    t1.marcar_como_atendido()

    print("\n" + str(agenda))