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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
import funciones as fun
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

##-----## Definición modelos. ##-----##

# Función que crea el catálogo.
def nuevo_catalogo():
    """
        Esta función permite inicializar el catálogo. Este guarda dos listas de elementos:
         1- Los artistas.
         2- Las obras.

        No tiene parámetros.

        Retorna el catálogo.

    """
    # Crear variable que guarda la lista del catálogo.
    catalogo = {'artistas': None,
                'obras': None}

    # Añadir listas vacías de los artistas y las obras al catálogo.
    catalogo['artistas'] = lt.newList('ARRAY_LIST')         # Pendiente añadir función de comparación.
    catalogo['obras'] = lt.newList('ARRAY_LIST')            # Pendiente añadir función de comparación.
    
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
            "Medium": str,
            "Classification": str,
            "DateAcquired": str,
            "Circumference (cm)": None,
            "Depth (cm)": None,
            "Diameter (cm)": None,
            "Height (cm)": None,
            "Length (cm)": None,
            "Weight (kg)": None,
            "Width (cm)": None,
            "Seat Height (cm)": None}

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


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento