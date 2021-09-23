from io import DEFAULT_BUFFER_SIZE
import controller
import model
from DISClib.ADT import list as lt
import datetime as date
from DISClib.Algorithms.Sorting import quicksort as qui

catalogo = controller.inicializar_catalogo("ARRAY_LIST")
controller.cargar_datos(catalogo)





def fecha_adqu_es_menor (fecha_1: str, fecha_2: str):
    es_menor = False

    # Si la obra 1 no tiene fecha de adquisición.
    if fecha_1 == "":
        fecha_1 = "0001-01-01"

    # Si la obra 2 no tiene fecha de adquisición.
    if fecha_2 == "":
        fecha_2 = "0001-01-01"

    # Crear variables con fechas modificadas.
    mod_fecha_obra_1 = date.datetime.strptime(fecha_1, '%Y-%m-%d')
    mod_fecha_obra_2 = date.datetime.strptime(fecha_2, '%Y-%m-%d')

    # Determinar si es menor.
    if mod_fecha_obra_1 < mod_fecha_obra_2:
        es_menor = True
    
    # Retornar respuesta.
    return (es_menor)


def requerimiento_2 (catalogo: dict, intervalo_inferior: str, intervalo_superior: str) -> dict:

    total_obras_rango = 0
    lista_obras = []


    nueva_lista = lt.newList(datastructure="ARRAY_LIST")

    for obra in lt.iterator(catalogo["obras"]):
        fecha_adqu_obra = obra["DateAcquired"]
        menor_que_int_inferior = (fecha_adqu_es_menor(fecha_adqu_obra, intervalo_inferior))
        mayor_que_int_superior = (fecha_adqu_es_menor(intervalo_superior, fecha_adqu_obra))

        if not menor_que_int_inferior and  not mayor_que_int_superior:
            lt.addLast(nueva_lista, obra)

    
    qui.sort(nueva_lista, model.cmp_obras_por_fecha_adquisicion)

    lista_obras.append(lt.getElement(nueva_lista, 1))
    lista_obras.append(lt.getElement(nueva_lista, 2))
    lista_obras.append(lt.getElement(nueva_lista, 3))
    lista_obras.append(lt.getElement(nueva_lista, lt.size(nueva_lista)))
    lista_obras.append(lt.getElement(nueva_lista, lt.size(nueva_lista) - 1))
    lista_obras.append(lt.getElement(nueva_lista, lt.size(nueva_lista) - 2))

    total_obras_rango = lt.size(nueva_lista)


    tupla_retorno = (total_obras_rango, lista_obras)

    return(tupla_retorno)

        

print(requerimiento_2(catalogo, "1944-06-06", "1989-11-09"))

#for obra in lt.iterator(lista_prueba):
    #print(obra["Credit Line"])



"""
for obra in lt.iterator(lista_prueba):
    
    fecha_adqu_obra = obra["DateAcquired"]
    menor_que_int_inferior = (fecha_adqu_es_menor(obra["DateAcquired"], "2022-01-01"))
    print(menor_que_int_inferior)
    '''
        mayor_que_int_superior = (model.cmp_obras_por_fecha_adquisicion(intervalo_superior, fecha_adqu_obra))

        if not(menor_que_int_inferior and mayor_que_int_superior):
            lt.addLast(nueva_lista, obra)
   '''
"""