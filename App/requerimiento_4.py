


import config as cf
import model
import time
from  DISClib.ADT import list as lt
import controller as cf

catalogo = cf.inicializar_catalogo("ARRAY_LIST")
cf.cargar_datos(catalogo)


def requerimiento_4(catalog):
    artistas = catalog["artistas"]
    obras= catalog["obras"]
    sublist_obras = lt.newList("ARRAY_LIST")
    nacionalidades= lt.newList()
    cont= 1

    for orb in lt.iterator(catalog["artistas"]):

        for art in lt.iterator(catalog["obras"]):
            lista_id_artistas_obra= art["id"]
            for id in lista_id_artistas_obra:
               # print(orb["id"],int(art["id"]))

                if int(orb["id"]) == int(art["id"]):
                 #   print(True)
            

        
        
    



             
    


        

        






print(requerimiento_4(catalogo))



        #if pays == country.lower():
         #   lt.addLast(sublist_country, lt.getElement(catalog['videos'], x))
   # lt_country = sublist_country