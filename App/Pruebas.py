import config as cf
import csv

def prueba () -> None:
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    var = None
    contador = 0
    archivo = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(archivo, encoding='utf-8'))
    for obra in input_file:
        contador +=1
        var = obra["ConstituentID"]
        if contador== 2:
            break

    lista = (var[1:len(var) - 1]).split(",")
    print(type(lista))
    print(lista[0])

prueba()