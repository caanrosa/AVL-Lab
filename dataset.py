from TreeUtils import *
import csv
import os

dirname = os.path.dirname(__file__)
file_path = dirname + "/dataset/short_dataset.csv" # uno con menos para poder VISUALIZARLO
tree = AVL("Title")
num = 10

with open(file_path, mode='r') as file:
    lector_csv = csv.DictReader(file)
    for indice, fila in enumerate(lector_csv, start=1):
        if indice == num:  # Procesar solo la fila que el usuario le pida
            #titulo = fila['Title']
            #datos = dict(fila)  # Convertir la fila en un diccionario
            tree.insert(fila)
            break  # Salir del bucle después de insertar la fila 10

with open(file_path, mode='r') as file:
    lector_csv = csv.DictReader(file)
    for fila in lector_csv:
        #titulo = fila['Title']
        #datos = dict(fila)  # Convertir la fila en un diccionario
        tree.insert(fila)

tree.graph("datasetCompleto").view()
tree.Validacion_dataset(1000000,1000000)