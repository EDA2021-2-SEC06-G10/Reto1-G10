import config as cf
import model
import controller
import model
import csv

catalogo = controller.inicializar_catalogo()
controller.cargar_datos(catalogo)

print(catalogo["obras"])