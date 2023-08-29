
#clase de vuelo con sus argumentos
import gestion
class Vuelo:
    def _init_(self, numero_vuelo: int, origen: str, destino: str, fecha_salida, fecha_vuelta):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_salida = hora_salida
        self.fecha_vuelta = fecha_vuelta

    #str para que cuando printee salga bien
    def _str_(self):
        return f"{self.numero_vuelo} {self.origen} {self.destino} {self.fecha_salida} {self.fecha_vuelta}"
