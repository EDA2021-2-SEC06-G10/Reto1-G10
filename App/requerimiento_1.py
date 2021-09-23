from DISClib.Algorithms.Sorting.quicksort import qui
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
    primeros = 0
    ultimos = 0
    save_equals_as_death = lt.newList()
    start_time = time.process_time()
    for cat in   lt.iterator(catalog["artistas"]):
        if anio_final >= int(cat["nacimiento"]) >= anio_inicial:

            lt.insertElement(artistas_por_anio,cat,1)
           


            contador_de_artistas +=1

    artistas_por_anio= qui.sort(artistas_por_anio,cmp_artistas_por_anio_de_nacimiento)
    #print(artistas_por_anio)
    
    while primeros < 3:
        f= lt.firstElement(artistas_por_anio)
        lt.addFirst(rta,f)
        lt.removeFirst(artistas_por_anio)
        primeros +=1

    while ultimos < 3:
        f= lt.lastElement(artistas_por_anio)
        lt.addLast(rta,f)
        lt.removeLast(artistas_por_anio)
        ultimos +=1    

         




    return (contador_de_artistas, rta)




a = 1938
b = 1945
print(requerimiento_1(catalogo,a,b))



    