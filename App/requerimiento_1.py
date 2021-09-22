import config as cf
import model
import time
from DISClib.ADT import list as lt
import controller as cf

catalogo = cf.inicializar_catalogo("ARRAY_LIST")
cf.cargar_datos(catalogo)


def requerimiento_1(catalog, anio_inicial, anio_final):
    artistas= catalog["artistas"]
    artistas_por_anio= lt.newList()
    contador_de_artistas = 0
    rta= lt.newList()
    primero = 0
    ultimos = 0
    start_time = time.process_time()
    for cat in lt.iterator(catalog["BeginDate"]):
        if anio_final >= cat["BeginDate"] >= anio_inicial:
            artista = lt.getElement(artistas, cat)
            lt.insertElement(artistas_por_anio,artistas,cat)
            contador_de_artistas +=1

    for art in (1,lt.size(artistas_por_anio)):
        if art["BeginDate"] == anio_inicial:
            lt.addFirst(rta,art["DisplayName"]["BeginDate"]["EndDate"]["Nationality"]["Gender"])

        if art["BeginDate"] == anio_final:
            lt.addLast(rta,art["DisplayName"]["BeginDate"]["EndDate"]["Nationality"]["Gender"])
    

    x= ("hay ", contador_de_artistas , " artistas nacidos entre", anio_inicial, "y", anio_final, "adicional a esto los primeros y ultimos 3 artistas del rango son:",rta  )
    

    return x


a = 1938
b = 1945
print(requerimiento_1(catalogo,a,b))




    