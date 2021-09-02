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
    # Crear variable que guarda el diccionario que hace referencia al catálogo.
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
def agregar_artista(catalogo, artista):
    """
        Esta función permite agregar un atista al catálogo, guardándolo en el arreglo 'artistas'.

        Parámetros:
            -> catalogo: catálogo.
            -> artista: artista que se quiere adicionar. 

        No tiene retorno.

    """
    # Agregar al artista a la última posición de la lista "artistas".
    lt.addLast(catalogo['artistas'], artista)


# Función que agrega una obra al catálogo.
def agregar_obra(catalogo, obra):
    """
        Esta función permite agregar una obra al catálogo, guardándolo en el arreglo 'obras'.

        Parámetros:
            -> catalogo: catálogo.
            -> obra: obra que se quiere adicionar. 

        No tiene retorno.

    """
    # Agregar la obra a la última posición de la lista "obras".
    lt.addLast(catalogo['obras'], obra)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento