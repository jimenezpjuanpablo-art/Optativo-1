class Cancion:
    #Representa una canción con su metadata y duración en segundos.

    def __init__(self, titulo: str, artista: str, duracion_segundos: int):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self) -> str:
        # Convierte segundos a formato MM:SS
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"'{self.titulo}' - {self.artista} ({minutos}:{segundos:02d})"


class ListaReproduccion:
    #Administra una lista compuesta por múltiples objetos de la clase Cancion.

    def __init__(self, nombre: str):
        self.nombre = nombre
        # Lista interna para almacenar los objetos Cancion
        self.canciones: list[Cancion] = []

    def agregar_cancion(self, cancion: Cancion) -> None:
        #Añade un objeto Cancion a la colección.
        self.canciones.append(cancion)

    def calcular_duracion_total_segundos(self) -> int:
        #Recorre la colección y suma la duración total.
        return sum(c.duracion_segundos for c in self.canciones)

    def __str__(self) -> str:
        lineas = [f"=== Lista de Reproducción: {self.nombre} ==="]
        if not self.canciones:
            lineas.append("La lista está vacía.")
        else:
            for idx, c in enumerate(self.canciones, 1):
                lineas.append(f"{idx}. {c}")
            
            total_seg = self.calcular_duracion_total_segundos()
            minutos = total_seg // 60
            segundos = total_seg % 60
            lineas.append(f"----------------------------------------")
            lineas.append(f"Duración Total: {minutos} min {segundos:02d} seg ({len(self.canciones)} canciones)")
        return "\n".join(lineas)


if __name__ == "__main__":
    mi_playlist = ListaReproduccion("Rock Clásico")
    mi_playlist.agregar_cancion(Cancion("Bohemian Rhapsody", "Queen", 354))
    mi_playlist.agregar_cancion(Cancion("Hotel California", "Eagles", 390))
    mi_playlist.agregar_cancion(Cancion("Sweet Child O' Mine", "Guns N' Roses", 356))

    print(mi_playlist)