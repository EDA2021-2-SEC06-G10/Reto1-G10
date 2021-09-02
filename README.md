Integrantes:
 Req. 2 - José Nicolás Cárdenas, 201922006, j.cardenast
 Req. 3 - Andrés Leonardo Beltran, 202014143, al.beltran

Modificaciones realizadas:
 1- Se añadieron las opciones de carga de los cuatro requerimientos a la función printMenu del módulo view.py y la opción de salir. También se añadió la documentación de dicha función.

 2- Se añadieron los datos oficiales del reto a la carpeta Data/MoMA.

 3- Se crearon las sigueintes funciones en model.py:
    > nuevo_catalogo: crea el catálogo que guarda los artistas y las obras. Ambas se crearon como arreglos.
    > agregar_artista: agrega un artista al catálogo.
    > agregar_obra: agrega una obra al catálogo.

 4- Se crearon las sigueintes funciones en controller.py:
    > inicializar_catalogo: inicializa el catálogo.
    > cargar_datos: carga toda la información de los aristas y las obras.
    > cargar_artistas: carga todos los artistas al catálogo.
    > cargar_obras: carga todas las obras al catálogo.

 5- En general, se cambiaron los nombres de las variables y las funciones al español para facilitar su diferenciación de los métodos y las clases de DISClib.

Pendiente:
 1- Funciones creación datos de model.py.
 2- Cambiar addTag por la función correspondiente en las funciones cargar_artistas y cargar_obras en controller.py.
 3- Hacer que la opción de cargar el catálogo funcione.


##---------------------------------------------------------------------------------------------------------##


#ISIS1225 - Librerias de soporte

Este proyecto contiene los Tipos abstractos de datos, estructuras de datos y algoritmos requeridos por el curso ISIS1225-Estructuras de Datos y Algoritmos

-Lib
Este directorio contiene todo el código de base que se entrega para el funcionamiento del curso.  Dentro de este directorio encuentran:
    
    |-- ADT:  Directorio con los Tipos Abstractos de Datos del curso

    |--DataStructures: Directorio con todas las estructuras de datos y archivos auxiliares para su     correcto funcionamiento

    |--Algorithms: Implementación de los algoritmos vistos en el curso (por ejemplo algoritmos de ordenamiento)

    |-- Utils: Funciones auxiliares para el funcionamiento de los TADs y estructuras de datos

-Test
Este directorio contiene las pruebas realizadas a los TADs, Estructuras de Datos y Algoritmos.

