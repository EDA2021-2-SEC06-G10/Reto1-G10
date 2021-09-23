 
import config as cf
import model
import time
from DISClib.ADT import list as lt
import controller as cf

catalogo = cf.inicializar_catalogo("ARRAY_LIST")
cf.cargar_datos(catalogo)
#print(catalogo["artistas"])

def requerimiento_1(catalog, anio_inicial:int, anio_final: int):
    artistas= catalog["artistas"]
    artistas_por_anio= lt.newList()
    contador_de_artistas = 0
    rta= lt.newList()
    save_equals_as_death = lt.newList()
    start_time = time.process_time()
    for cat in   lt.iterator(catalog["artistas"]):
        if anio_final >= int(cat["nacimiento"]) >= anio_inicial:

            lt.insertElement(artistas_por_anio,cat,1)
           


            contador_de_artistas +=1
    #print(artistas_por_anio)
    for art in lt.iterator(artistas_por_anio):

        if art["nacimiento"] ==  anio_inicial:
            lt.addFirst(rta,art)
        elif art["nacimiento"]  < anio_final:   
            lt.addLast(rta,art)
        elif art["nacimiento"] == anio_final:
            lt.addLast(save_equals_as_death,art)

    for a in lt.iterator(save_equals_as_death):
        lt.addLast(rta,a)




    return (contador_de_artistas, rta)




a = 1938
b = 1945
print(requerimiento_1(catalogo,a,b))




    