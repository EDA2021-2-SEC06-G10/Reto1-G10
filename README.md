Integrantes:
 -> José Nicolás Cárdenas, 201922006, j.cardenast
 -> Andrés Leonardo Beltran, 202014143, al.beltran

MODIFICACIONES REALIZADAS:

 1- En view.py(), se crearon las siguientes funciones:
    > inicializar_catalogo(): inicializa el catálogo.
    > cargar_datos(): carga los datos.

 2- Se modificaron las siguientes funciones de tal forma que reciban como parámetro una cadena que indica la representación que se desea que tenga la lista del catálogo.
    > view.inicializar_catalogo().
    > controller.inicializar_catalogo().
    > model.nuevo_catalogo().

 3- En view.py, se cambió el menú principal para que, al escoger la opción 1, se le permitiera al usuario escoger el tipo de representación de la lista del catálogo.

 4- En model.py, se definió la función cmp_obras_por_fecha_adquisicion(), la cual cumple dicho propósito.

 5- En model.py, se importaron los módulos referentes a los cuatro algoritmos de ordenamiento requeridos.

 6- Se definieron las siguientes funciones, las cuales ordenan las obras con base en su fecha de adquisión:
    > ordenar_obras() en model.py.
    > ordenar_obras() en controller.py.

 7- En view.py, se definió la función deter_algor_orden(), la cual retorna una cadena con el algoritmo de ordenamiento que desea usar el usuario.

 En general, se añadieron comentarios de varias línea de código.


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

