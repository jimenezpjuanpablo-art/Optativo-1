#Ejercicio 1: Ficha de cliente
class Cliente:
    # se crea una clase que representa a un cliente de un comercio con sus datos personales

    def __init__(self, nombre: str, cedula: str, telefono: str):
        # Inicialización de atributos principales del cliente
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self) -> str:
        # Devuelve la ficha del cliente en un formato legible usando f-strings
        return (
            f"--- Ficha de Cliente ---\n"
            f"Nombre: {self.nombre}\n"
            f"Cédula: {self.cedula}\n"
            f"Teléfono: {self.telefono}\n"
            f"------------------------"
        )



if __name__ == "__main__":
    # Creación de dos instancias independientes
    cliente1 = Cliente("Cristiano Ronaldo", "4.567.890", "0981-123456")
    cliente2 = Cliente("Ricardo Arjona", "3.210.987", "0971-654321")

    # Impresión de fichas
    print(cliente1)
    print()
    print(cliente2)