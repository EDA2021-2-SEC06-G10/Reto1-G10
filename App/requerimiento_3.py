import controller
from DISClib.ADT import list as lt


catalogo = controller.inicializar_catalogo("ARRAY_LIST")
controller.cargar_datos(catalogo)




# Función que retorna ConstituentID del artista.
def dar_id_artista (catalogo: dict, nombre: str) -> int:
    """
        Dado el nombre de un artista, esta función retorna su "ConstituentID" respectivo.

        Parámetros:
            -> catalogo (dict): catálogo.
            -> nombre (str): nombre del artista.

        Retorno:
            -> (int): ConstituentID del artista.
                      -1 si no hay un ConstituentID para ese nombre.

    """
    # Crear lista que contiene a todos los artistas.
    lista_artistas_original = catalogo["artistas"]
    lista_artistas = lista_artistas_original.copy()

    # Crear variable de retorno. Asignar valor por defecto.
    id = -1

    # Recorrer lista artistas.
    for artista in lt.iterator(lista_artistas):
        # Guardar nombre del artista de la iteración actual.
        nombre_actual = artista["nombre"]

        # Si los nombres coinciden.
        if (nombre_actual == nombre):
            # Guardar el ConstituentID del artista.
            id = artista["id"]

    # Retornar respuesta respectiva.
    return (id)


# Función que determina si un artista es autor de una obra.
def es_autor_obra (obra: dict, id_artista: int) -> bool:
    """
        Dado el diccionario de una obra y el ConstituentID de un artista, esta función
        determina si este artista es autor de dicha obra.

        Parámetros:
            -> obra (dict): diccionario que guarda la información de la obra.
            -> id_artista (int): ConstituentID del artista.

        Retorno:
            -> (bool): True si el artista es autor de la obra.
                       False de lo contrario.

    """
    # Crear variable de retorno y asignarle valor por defecto.
    retorno = False

    # Crear lista que guarda los ConstituentID's de los autores de la obra.
    lista_autores_original = obra["ConstituentID"]
    lista_autores = lista_autores_original.copy()

    # Recorrer lista de ConstituentID's de la obra.
    for id_autor in lista_autores:
        # Si el artista es autor de la obra.
        if (int(id_autor) == id_artista):
            retorno = True

    # Retorno.
    return (retorno)


# Función que retorna lista con obras de un autor.
def devolver_obras_autor (catalogo: dict, id_artista: int) -> list:
    """
        Dado el catálogo y el "ConstituentID" de un artista, esta función retorna una lista con
        todas las obras de las que este es autor.

        Parámetros:
            -> catalogo (dict): catálogo.
            -> id_artista (int): "ConstituentID" del artista.

        Retorno:
            -> (list): lista con las obras de las que el artista es autor.

    """    
    # Crear variable de retorno.
    lista_orbas_autor = []

    # Crear lista de todas las obras del catálogo.
    obras_original = catalogo["obras"]
    obras = obras_original.copy()
    
    # Recorrer lista obras.
    for obra in lt.iterator(obras):
        # Crear variable que determina si el artista es autor de la obra de la iteración actual.
        es_autor = es_autor_obra(obra, id_artista)
        
        # Si el artista sí es autor.
        if es_autor:
            # Agregar la obra a la lista de obras del autor.
            lista_orbas_autor.append(obra)

    # Retorno.
    return (lista_orbas_autor)


# Función que crea diccionario con técnicas del autor. 
def crear_dicc_tecnicas_autor (obras_del_autor: list) -> dict:
    """
        Dada una lista con las obras de un autor, esta función retorna un diccioario cuyas llaves son
        las técnicas de dichas obras, y cuyos valores son la cantidad de obras que fueran creadas mediante
        dicha técnica.        

        Parámetros:
            -> obras_del_autor (list): lista con obras de un autor.

        Retorno:
            -> (dict): diccionario con las características descritas.

    """
    # Crear variable de retorno.
    dicc_tecnicas = {}

    # Recorrer todas las obras en la lista de obras del autor.
    for obra in obras_del_autor:
        # Guardar el medio de la obra.
        tecnica = obra["Medium"]

        # Crear variable proposicional cuyo valor de verdad indica si la técnica de la iteración actual
        # ya está en el diccionario.
        ya_esta_la_tecnica = (tecnica in dicc_tecnicas)

        # Si la técnica ya está en el diccionario.
        if (ya_esta_la_tecnica):
            dicc_tecnicas[tecnica] += 1

        # De lo contrario.
        else: 
            dicc_tecnicas[tecnica] = 1

    # Retorno.
    return (dicc_tecnicas)


# Función dimensiones obra.
def dimensiones_obra (obra: dict) -> str:
    """
        Dada una obra, esta función retorna una cadena con sus dimensiones.

        Parámetros:
            -> obra (list): lista con obras de un autor.

        Retorno:
            -> (str): cadena con las dimensiones de la obra.

    """
    # Determinar dimensiones obra.
    circum = obra["Circumference (cm)"]
    depth = obra["Depth (cm)"]
    diam = obra["Diameter (cm)"]
    altu = obra["Height (cm)"]
    largo = obra["Length (cm)"]
    peso = obra["Weight (kg)"]
    ancho = obra["Width (cm)"]
    base = obra["Seat Height (cm)"]

    # Crear cadena dimensiones.
    dimensiones = ("Circumferencia: " + circum + " cm;" +
                   " Profundidad: " + depth + " cm;" +
                   " Diámetro: " + diam + " cm;" +
                   " Altura: " + altu + " cm;" +
                   " Largo: " + largo + " cm;" +
                   " Peso: " + peso + " kg;" +
                   " Ancho: " + ancho + " cm;" +
                   " Base: " + base + " cm")

    # Retorno.
    return (dimensiones)


# Función que crea una lista con la infomación obras creadas con técnica más usada de un autor. 
def crear_lista_orbas_tecnica_mas_usada (obras_del_autor: list, tecnica_mas_usada: str) -> list:
    """
        Dada una lista con las obras de un autor, esta función retorna una lista que tiene la información
        de las obras de un autor que fueron creadas mediante su técnica más usada. Dicha información se encontrará
        empaquetada en una tupla.

        Parámetros:
            -> obras_del_autor (list): lista con obras de un autor.
            -> tecnica_mas_usada (str): cadena de la técnica más usada por el autor.

        Retorno:
            -> (list): lista de tuplas con la información de las obras creadas con la técnica más usada del autor.

    """
    # Crear variable de retorno.
    lista_tuplas = []

    # Recorrer todas las obras en la lista de obras del autor.
    for obra in obras_del_autor:
        # Guardar el medio de la obra.
        tecnica = obra["Medium"]

        # Si la técnica de la obra de la iteración actual coindice con la técnica más usada.
        if (tecnica == tecnica_mas_usada):
            # Guardar datos obra.
            titulo = obra["Title"]
            fecha = obra["DateAcquired"]
            medio = tecnica
            dimensiones = dimensiones_obra(obra)

            # Empaquetar datos obra y añadir tupla a la lista de tuplas.
            tupla_obra = (titulo, fecha, medio, dimensiones)
            lista_tuplas.append(tupla_obra)

    # Retorno.
    return (lista_tuplas)


# Función que retorna los valores de interés para el requerimiento.
def requerimiento_3 (catalogo: dict, nombre: str) -> tuple:
    """
        Dado el catálogo y el nombre de un artista, esta función retorna una tupla con:
            1- La cantidad de obras de las que este es autor.
            2- El total de técnicas que este ha usado.
            3- La técnica más utilizada.
            4- La lista de las obras de dicha técnica, con:
                >> Título.
                >> Fecha.
                >> Medio.
                >> Dimensiones.

        Parámetros:
            -> catalogo (dict): catálogo.
            -> nombre (str): nombre del autor.

        Retorno:
            -> (tuple): tupla con la información mencionada.
                        Si la tupla resulta ser (-1,-1), entonces el nombre ingresado no es válido.

    """
    # Crear variables de retorno.
    cantidad_obras = 0
    total_tecnicas = 0
    tecnica_mas_usada = ""
    lista_obras_tecnica = []
    tupla_retorno = None

    # Determinar id artista.
    id_artista = dar_id_artista(catalogo, nombre)

    # Si el nombre ingresado es válido.
    if not (id_artista == -1):
        # Crear lista con obras autor.
        lista_obras_autor = devolver_obras_autor(catalogo, id_artista)

        # Determinar cantidad de obras de las que este es autor.
        cantidad_obras = len(lista_obras_autor)

        # Crear diccionario que guarda las técnicas de las obras del autor.
        dicc_tecnicas_autor = crear_dicc_tecnicas_autor(lista_obras_autor)

        # Determinar cantidad de técnicas que ha usado el autor.
        total_tecnicas = len(dicc_tecnicas_autor)


        ##--## Iteración que determina la técnica más usada. ##--##

        # Crear variable que guarda la técnica con mayor número de usos.
        mayor_uso_tecnica = -1

        # Recorrer las llaves del diccionario de técnicas.
        for tecnica in dicc_tecnicas_autor:
            # Crear variable que guarda la cantidad de usos de la técnica de la iteración actual
            # y guardar su valor.
            uso_tecnica_actual = dicc_tecnicas_autor[tecnica]

            # Si la cantidad actual es mayor que el mayor.
            if (uso_tecnica_actual > mayor_uso_tecnica):
                mayor_uso_tecnica = uso_tecnica_actual
                tecnica_mas_usada = tecnica

        # Crear lista obras de las técnica más usada.
        lista_obras_tecnica = crear_lista_orbas_tecnica_mas_usada(lista_obras_autor, tecnica_mas_usada)
        

        # Crear tupla de retorno.
        tupla_retorno = (cantidad_obras, total_tecnicas, tecnica_mas_usada, lista_obras_tecnica)


    # Si el nombre ingresado es inválido.
    else:
        tupla_retorno = (-1,-1)

    # Retorno.
    return (tupla_retorno)


req_3 = requerimiento_3(catalogo, "Louise Bourgeois")
print(req_3)

