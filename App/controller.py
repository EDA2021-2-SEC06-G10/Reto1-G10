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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


##-----## Definición de función de inialización del catálogo. ##-----##

# Función que retorna el catálogo.
def inicializar_catalogo(tipo_representacion: str):
    """
        Esta función invoca a la función nuevo_catalogo de model.py y retorna al catálogo.

        Parámetro:
            -> tipo_representacion (str): cadena que indica la representación que se desea
                                          que tenga la lista del catálogo.

        Retorno:
            -> El catálogo. 

    """
    # Invocar función nuevo_catalogo, guardar su retorno en la variable catalogo y retornar.
    catalogo = model.nuevo_catalogo(tipo_representacion)
    return catalogo



###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###


##-----## Definición de funciones para cargar datos. ##-----##


# Función que carga toda la información al catálogo.
def cargar_datos(catalogo) -> None:
    """
        Esta función carga toda la información tanto de los artistas como de las obras
        al catálogo. Lo hace invocando a las funciones cargar_artistas y cargar_obras.

        Parámetro:
            -> catalogo (dict): catálogo.

        No tiene retorno.

    """
    # Cargar artistas.
    cargar_artistas(catalogo)

    # Cargar obras.
    cargar_obras(catalogo)


# Función que carga todos los artistas.
def cargar_artistas(catalogo) -> None:
    """
        Función que carga todos los artistas.

        Parámetro:
            -> catalogo: catálogo.

        No tiene retorno.
        
    """
    # Crear variable que guarda la referencia al archivo de los artistas.
    archivo_artistas = cf.data_dir + 'Artists-utf8-5pct.csv'

    # Crear variable que guarda todos los artistas.
    input_file = csv.DictReader(open(archivo_artistas, encoding='utf-8'))

    # Añadir cada artista al catálogo.
    for artista in input_file:
        model.agregar_artista(catalogo, artista)


# Función que carga todas las obras.
def cargar_obras(catalogo) -> None:
    """
        Función que carga todas las obras.

        Parámetro:
            -> catalogo: catálogo.

        No tiene retorno.
        
    """
    # Crear variable que guarda la referencia al archivo de las obras.
    archivo_obras = cf.data_dir + 'Artworks-utf8-small.csv'

    # Crear variable que guarda todas las obras.
    input_file = csv.DictReader(open(archivo_obras, encoding='utf-8'))

    # Añadir cada obra al catálogo.
    for obra in input_file:
        model.agregar_obra(catalogo, obra)




# Funciones de ordenamiento

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
        
        +.-33.
        Retorno:
            -> Tupla con sublista ordenada y tiempo de ejecución del algoritmo de 
               ordenamiento en milisegundos.

    """
    # Crear tupla de retorno y retornarla.
    tupla_retorno = model.ordenar_obras(catalogo, tamanio, algor_orden)
    return (tupla_retorno)

# Funciones de consulta sobre el catálogo
