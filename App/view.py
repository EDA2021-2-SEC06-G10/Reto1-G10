"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

##-----## Importación módulos. ##-----##

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import model
import requerimiento_3 as req_3


###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###
###---###---------------------------------------------------------------------------------------------------------------------------###---###


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada.

"""


##-----## Definición de funciones de view.py. ##-----##


# Función que imprime el menú de opciones de la herramienta.
def imprimir_menu() -> None:
    """
        Esta función imprime el menú de interacción con el usuario.

        No tiene ni parámetros ni retornos.

    """
    print("\n\nBienvenido.")
    print("  1- Cargar información en el catálogo.")
    print("  2- Cargar requerimiento 1.")
    print("  3- Cargar requerimiento 2.")
    print("  4- Cargar requerimiento 3.")
    #print("  3- Cargar requerimiento 2.")
    #print("  4- Cargar requerimiento 3.")
    #print("  5- Cargar requerimiento 4.")
    print("  0- Salir.")


# Función que inicializa el catálogo del museo.
def inicializar_catalogo(tipo_representacion: str) -> dict:
    """
        Inicializa el catálogo del museo.

        Parámetro:
            -> tipo_representacion (str): cadena que indica la representación que se desea
                                          que tenga la lista del catálogo.
        
        Retorno:
            -> (dict): el catálogo del museo.

    """
    # Crear variable que guarda el catálogo y retornarlo.
    # Este se crea mediante la función homónima de controller.py.
    catalogo = controller.inicializar_catalogo(tipo_representacion)
    return catalogo 


# Función que carga todos los datos del catálogo.
def cargar_datos(catalogo) -> None:
    """
        Esta función carga todos los datos de interés de la carpeta
        Data/MoMA.

        Parámetro:
            -> catalogo: catálogo.

        No tiene retorno.

    """
    # Cargar los datos mediante la función homónima de controller.py.
    controller.cargar_datos(catalogo)


# Función que determina el algoritmo de ordenamiento que se quiere usar para
# ordenar las obras.
def deter_algor_orden(opcion_escogida: int) -> str:
    """
        Esta función determina el algoritmo de ordenamiento que se quiere usar
        para ordenar las obras.

        Parámetro:
            -> algor_escogido (int): opción escogida por el usuario.

        Retorno:
            -> (str): "Insertion Sort" en caso de escoger este algoritmo.
                      "Shell Sort" en caso de escoger este algoritmo.
                      "Merge Sort" en caso de escoger este algoritmo.
                      "Quick Sort" en caso de escoger este algoritmo.

    """
    # Variable de retorno.
    algor_orden = ""

    # Determinar algoritmo.
    if opcion_escogida == 1:
        algor_orden = "Insertion Sort"
    elif opcion_escogida == 2:
        algor_orden = "Shell Sort"
    elif opcion_escogida == 3:
        algor_orden = "Merge Sort"
    elif opcion_escogida == 4:
        algor_orden = "Quick Sort"
    
    # Retornar.
    return (algor_orden)

# Crear variable que guardará el catálogo.
catalogo = None

"""
Menú principal.

"""
# Ciclo que permite mostrar el menú tantas veces como necesite el usuario.
while True:
    # Imprmir el menú.
    imprimir_menu()

    # Crear variable que guarda la respuesta del usuario.
    respuesta = int(input('Por favor, seleccione una opción para continuar:\n -> '))

    # Si escoge la opción 1.
    if (respuesta == 1):
        # Crear variables que guardan el texto instructivo para la escogencia del tipo
        # de representación de la lista del catálogo.
        texto_general = "\nOpciones:"
        texto_opcion_1 = """ 1- Arreglo."""
        texto_opcion_2 = """ 2- Lista Enlazada."""

        # Impresión opciones.
        print(texto_general)
        print(texto_opcion_1)
        print(texto_opcion_2)

        # Variable que guarda la respuesta.
        respuesta_repres = int(input("""Indique el número del tipo de representación de la lista del catálogo:\n -> """))

        # Si se escoge la opción 1.
        if (respuesta_repres == 1):
            tipo_repres = "ARRAY_LIST"

        # Si se escoge la opción 2.
        elif (respuesta_repres == 2):
            tipo_repres = "LINKED_LIST"

        # Si se escoge una opción errónea.
        else:
            print("Error: debe escoger una opción válida.")
            sys.exit(0)

        # Inicializar catálogo.
        catalogo = inicializar_catalogo(tipo_repres)

        # Imprimir mensaje de carga.
        print("Cargando información de los archivos ....")

        # Cargar datos con las especificaciones indicadas.
        cargar_datos(catalogo)

        # Imprimir mensaje de éxito.
        print("\n<> Información cargada con éxito <>")

        ###
        obra_1 = lt.getElement(catalogo["obras"],1)
        obra_2 = lt.getElement(catalogo["obras"],2)

        print(model.cmp_obras_por_fecha_adquisicion(obra_1, obra_2))

        ###
    # Si escoge la opcion 2
    elif (respuesta == 2):
        # Inicializar catálogo.
        catalogo = inicializar_catalogo(tipo_repres)
        cargar_datos(catalogo)
        anio_inicial = int(input("\nIndique el año incial.:\n -> "))
        anio_final = int(input("\nIndique el año final.:\n -> "))
        rta = model.requerimiento_1(catalogo,anio_inicial,anio_final)
        print("\nRepuesta:")
        print("\n la cantidad de artistas del rango", anio_inicial, "a", anio_final, "son", rta)
    # Si escoge la opción 3.
    elif (respuesta == 3):
        # Inicializar catálogo.
        catalogo = inicializar_catalogo(tipo_repres)
        cargar_datos(catalogo)
        
        intervalo_inferior = int(input("\nIndique la fecha incial.:\n -> "))
        

        # Si se escogió una opción inválida.
        if (opcion_algor_orden < 1) or (opcion_algor_orden > 4):
            print("\nError: debe escoger una opción válida.")
            sys.exit(0)

        # De lo contrario.
        else:
            # Determinar algor. de orden. escogido.
            algor_orden = deter_algor_orden(opcion_algor_orden)
        
        # Pedir al usuario tamaño sublista.
        tamanio = int(input("""Indique el tamaño de la muestra:\n -> """))


        resultados = controller.ordenar_obras(catalogo, 100, algor_orden)

        print(" Ejecutando algoritmo. Espere . . .")
        print("\n El tiempo de ejecución del ordenamiento fue de", resultados[1], "milisegndos.")



    # Si escoge la opción 4.
    elif (respuesta == 4):
        # Inicializar catálogo.
        catalogo = inicializar_catalogo(tipo_repres)
        cargar_datos(catalogo)

        # Pedir al usuario el nombre del artista.
        nombre = input("""\nPor favor, indique el nombre del artista:\n -> """)

        # Invocar función del requeirmiento 3.
        if not(type(nombre) == str):
            print("\n>< Debe ingresar un nombre válido ><\n")
            sys.exit(0)
        else:
            # Llamar a la función requerimiento_3().
            respuesta_req_3 = req_3.requerimiento_3(catalogo, nombre)
            
            # Si el nombre ingresado fue válido.
            if not(respuesta_req_3 == (-1,-1)):
                # Desempaquetar los datos.
                (cantidad_obras, total_tecnicas, tecnica_mas_usada, lista_obras_tecnica) = respuesta_req_3

                # Crear variables con respuestas de interés.
                id_artista = req_3.dar_id_artista(catalogo, nombre)

                # Crear variables que guardan el texto de la respuesta.
                print("\nRepuesta:")
                print("\n -> El/la artista", nombre, "con MoMA ID", id_artista, "tiene", cantidad_obras, "a su nombre en el museo." )
                print("\n -> Ha usado", total_tecnicas, "técnicas diferentes en sus obras.")
                print("\n -> Su técnica más usada es", str(tecnica_mas_usada) + ".")
                print("\n -> El listado de las obras de dicha ténica es el siguiente:\n")
                cantdad_obras_de_tecnica = len(lista_obras_tecnica)
                contador = 1
                for tupla in lista_obras_tecnica:
                    print("\nObra número", str(contador) + ":")
                    print("  -Título", tupla[0])
                    print("  -Fecha:", tupla[1])
                    print("  -Medio:", tupla[2])
                    print("  -Dimensiones: ", "(" + str(tupla[3]) + ")")
                    contador += 1
            
            # De lo contrario.
            else:
                print("\n>< Debe ingresar un nombre válido ><\n") 

        

    # Si escoge la opción 0.
    else:
        sys.exit(0)



sys.exit(0)

