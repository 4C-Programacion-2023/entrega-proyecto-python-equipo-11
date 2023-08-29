from clases import Vuelo
#funcion para agregar vuelos a la lista
def agregar_vuelo(numero_vuelo, origen, destino, fechasalida, fechallegada, list_vuelos):
    vuelo = Vuelo(numero_vuelo, origen, destino, fechasalida, fechallegada)
    list_vuelos.append(vuelo)
    print("Vuelo agregaddo exitosamente")



#funcion para eliminar vuelos de la lista
def eliminar_vuelo(numero_vuelo, list_vuelos):
    for vuelo in list_vuelos:
        if vuelo.numero_vuelo == numero_vuelo:
            list_vuelos.remove(vuelo)
            print("Vuelo eliminado exitosamente")
            return
    print("No se encontró el vuelo con el número especificado")