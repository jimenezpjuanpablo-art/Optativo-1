class Libro:
    #Clase para registrar libros y controlar su disponibilidad de préstamo.

    def __init__(self, titulo: str, autor: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        # Atributo booleano de estado: True = Disponible, False = Prestado
        self.disponible = disponible

    def __str__(self) -> str:
        # Conversión del valor booleano a un texto amigable
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: '{self.titulo}' - Autor: {self.autor} | Estado: {estado}"


if __name__ == "__main__":
    # Creación de libros en diferentes estados
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", disponible=True)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", disponible=False)

    print(libro1)
    print(libro2)