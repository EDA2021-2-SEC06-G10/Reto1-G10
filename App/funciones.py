# Función que convierte el str de la lista de artistas en una lista.
def convertir_a_lista(lista_en_cadena: str) -> list:
    """
        Esta función permite convertir la cadena de texto que guarda los id de los artistas que crearon
        una obra en una lista.

        Parámetros:
            -> lista_en_cadena (str): cadena de texto con la lista de los id de los artistas.

        Retorno:
            -> (list): lista con los id de los artistas que crearon la obra.

    """
    # Crear lsta vacía en la que se guardarán los id de los artistas.
    lista_artistas = []

    # Crear sublista que contenga solo los id de los artistas mediante slicing y la función split().
    # Se hace parar borra los caracteres "[" y "]" que se encuentran al final de la cadena.
    lista_artistas = (lista_en_cadena[1 : len(lista_en_cadena) - 1]).split(",")

    # Retornar la lista.
    return lista_artistas