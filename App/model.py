"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import datetime
import config as cf
from DISClib.ADT import list as lt
import funciones as fun
assert cf
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as she
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qui
import time
import datetime as date

"""
Se define la estructura de un catálogo del museo, el cual tendrá dos listas:
una para los artistas, otra para las obras.
"""

##-----## Definición modelos. ##-----##

# Función que crea el catálogo.
def nuevo_catalogo(tipo_representacion: str):
    """
        Esta función permite inicializar el catálogo. Este guarda dos listas de elementos:
         1- Los artistas.
         2- Las obras.

        Permite indicar el tipo de representación de la lista del catálogo.

        Parámetro:
            -> tipo_representacion (str): cadena que indica la representación que se desea
                                          que tenga la lista del catálogo.

        Retorno:
            -> El catálogo del museo.

    """
    # Crear variable que guarda la lista del catálogo.
    catalogo = {'artistas': None,
                'obras': None}

    # Crear listas vacías de los artistas y las obras al catálogo.
    catalogo['artistas'] = lt.newList(tipo_representacion,cmpfunction=cmp_obras_por_fecha_adquisicion)         # Pendiente añadir función de comparación.
    catalogo['obras'] = lt.newList(tipo_representacion,cmpfunction=cmp_obras_por_fecha_adquisicion)            # Pendiente añadir función de comparación.
    
    # Retornar el catálogo.
    return catalogo



###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###


##-----## Definición de operaciones sobre el catálogo. ##-----##


# Función que agrega un artista al catálogo.
def agregar_artista(catalogo, artista: dict) -> None:
    """
        Esta función permite agregar un artista al catálogo, guardándolo en el arreglo 'artistas'.

        Parámetros:
            -> catalogo: catálogo.
            -> artista (dict): artista que se quiere adicionar.  

        No tiene retorno.

    """
    # Crear un artista con los datos ingresados por parámetro.
    artista_nuevo = nuevo_artista(artista)

    # Agregar al artista a la última posición de la lista "artistas".
    lt.addLast(catalogo['artistas'], artista_nuevo)


# Función que agrega una obra al catálogo.
def agregar_obra(catalogo, obra: dict):
    """
        Esta función permite agregar una obra al catálogo, guardándolo en el arreglo 'obras'.

        Parámetros:
            -> catalogo: catálogo.
            -> obra (dict): obra que se quiere adicionar. 

        No tiene retorno.

    """
    # Crear una obra con los datos ingresados por parámetro.
    obra_nueva = nueva_obra(obra)

    # Agregar la obra a la última posición de la lista "obras".
    lt.addLast(catalogo['obras'], obra_nueva)


##-----## Definición de funciones para la creación de datos. ##-----##


# Función que crea un artista.
def nuevo_artista (info_artista: dict) -> dict:
    """
        Esta función permite crear un artista. Estos se representarán mediante 
        el tipo de dato dict de Python.

        Parámetros:
            -> info_artista (dict): diccionario que tiene toda la información del artista
                                    que se encuentra en la base de datos.

        Retorno:
            -> (dict): diccionario que representa al artista.

    """
    # Crear variable que guarda el diccionario con la información de interés del artista.
    artista = {"nombre": "",
               "id": "",
               "nacionalidad": "",
               "nacimiento": None,
               "fallecimiento": None}

    # Añadir datos.
    artista["nombre"] = info_artista["DisplayName"]
    artista["id"] = int(info_artista["ConstituentID"])
    artista["nacionalidad"] = info_artista["Nationality"]
    artista["nacimiento"] = int(info_artista["BeginDate"])
    artista["fallecimiento"] = int(info_artista["EndDate"])
    
    # Retornar al artista.
    return artista

# Función que crea una obra.
def nueva_obra (info_obra: str) -> dict:
    """
        Esta función permite crear una obra. Estas se representarán mediante 
        el tipo de dato dict de Python.

        Parámetros:
            -> info_obra (dict): diccionario que tiene toda la información de la obra que
                                 se encuentra en la base de datos.

        Retorno:
            -> (dict): diccionario que representa a la obra.

    """
    # Crear variable que guarda el diccionario con la información de interés de la obra.
    obra = {"Title": "",
            "ObjectID": "",
            "ConstituentID": None,
            "Medium": "",
            "Classification": "",
            "DateAcquired": "",
            "Circumference (cm)": "",
            "Depth (cm)": "",
            "Diameter (cm)": "",
            "Height (cm)": "",
            "Length (cm)": "",
            "Weight (kg)": "",
            "Width (cm)": "",
            "Seat Height (cm)": ""}

    # Crear variable que guarda la lista de los id de los atistas que crearon la obra y asignarle la lista
    # que contiene dichos datos.
    lista_id_artistas = []
    lista_id_artistas = fun.convertir_a_lista(info_obra["ConstituentID"])

    # Iteración que añade la información de la obra.
    for propiedad in info_obra.keys():
        # Determinar si la propiedad actual es "ConstituentID".
        es_ConstituentID = (propiedad == "ConstituentID")

        # Si la obra no tiene la propiedad actual.
        if (info_obra[propiedad] == ""):
            # Asignar el valor de la propiedad como "".
            obra[propiedad] = ""
        # De lo contrario
        else:            
            # Añadir propiedad.
            if not(es_ConstituentID):
                obra[propiedad] = info_obra[propiedad]
            else:
                obra[propiedad] = lista_id_artistas

    # Retornar obra.
    return obra



###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###



##-----## Definición de funciones para la comparación de datos. ##-----##


# Función para comparación de obras de arte.
def cmp_obras_por_fecha_adquisicion(obra_1, obra_2) -> bool:  # Pendiente especificar tipo obra_1 y obra_2.
    """
        Esta función determina si la fecha de adquisición de obra_1 es menor que
        la de obra_2.

        Parámetros:
            -> obra_1: información de la primera obra.
            -> obra_2: información de la segunda obra.
        
        Retorno:
            -> (bool): True si la fecha de adquisición de obra_1 es menor que la de obra_2.
                       False de lo contrario.
    
    """
    # Crear variable de retorno.
    es_menor = False

    # Crear variables que guardan las fechas.
    fecha_obra_1 = obra_1["DateAcquired"]
    fecha_obra_2 = obra_2["DateAcquired"]

    # Si la obra 1 no tiene fecha de adquisición.
    if fecha_obra_1 == "":
        fecha_obra_1 = "0001-01-01"

    # Si la obra 2 no tiene fecha de adquisición.
    if fecha_obra_2 == "":
        fecha_obra_2 = "0001-01-01"

    # Crear variables con fechas modificadas.
    mod_fecha_obra_1 = date.datetime.strptime(fecha_obra_1, '%Y-%m-%d')
    mod_fecha_obra_2 = date.datetime.strptime(fecha_obra_2, '%Y-%m-%d')

    # Determinar si es menor.
    if mod_fecha_obra_1 < mod_fecha_obra_2:
        es_menor = True
    
    # Retornar respuesta.
    return (es_menor)
    


# Funciones utilizadas para comparar elementos dentro de una lista



###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###



##-----## Definición de funciones de ordenamiento. ##-----##


# Función ordenamiento obras con base en su fecha de adquisión.
def ordenar_obras(catalogo, tamanio: int, algor_orden: str) -> tuple:
    """
        Esta función ordena una sublista de tamaño especificado que contiene obras
        con base en la fecha de adquicisión y determina el tiempo que se demora en hacerlo.

        Parámetros:
            -> catalogo: catálogo del museo.
            -> tamanio (int): tamaño de la sublista.
            -> algor_orden (str): cadena que especifica el algoritmo de ordenamiento
                                  que se quiere usar.
        
        Retorno:
            -> Tupla con sublista ordenada y tiempo de ejecución del algoritmo de 
               ordenamiento en milisegundos.

    """
    # Crear variable de retorno.
    lista_ordenada = None

    # Crear sublista.
    sublista = lt.subList(catalogo["obras"], 0, tamanio)
    sublista = sublista.copy

    # Inicializar medición.
    start_time = time.process_time()

    # Ordenar la sublista dependiendo del algoritmo especificado.
    if (algor_orden == "Insertion Sort"):
        lista_ordenada = ins.sort(sublista, cmp_obras_por_fecha_adquisicion)
    elif (algor_orden == "Shell Sort"):
        lista_ordenada = she.sort(sublista, cmp_obras_por_fecha_adquisicion)
    elif (algor_orden == "Merge Sort"):
        lista_ordenada = mer.sort(sublista, cmp_obras_por_fecha_adquisicion)
    elif (algor_orden == "Quick Sort"):
        lista_ordenada = qui.sort(sublista, cmp_obras_por_fecha_adquisicion)
    
    # Parar medición.
    stop_time = time.process_time()

    # Calcular tiempo de ejeución.
    elapsed_time_mseg = (stop_time - start_time)*1000

    # Crear tupla con lista ordenada y tiempo de ejecución y retornarla.
    tupla_retorno = (elapsed_time_mseg, lista_ordenada)
    return (lista_ordenada)