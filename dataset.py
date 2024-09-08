from TreeUtils import *
import csv
import os

dirname = os.path.dirname(__file__)
file_path = dirname + "/dataset/short_dataset.csv" # uno con menos para poder VISUALIZARLO
tree = AVL("Title")


with open(file_path, mode='r') as file:
    lector_csv = csv.DictReader(file)
    for fila in lector_csv:
        #titulo = fila['Title']
        #datos = dict(fila)  # Convertir la fila en un diccionario
        tree.insert(fila)

tree.graph("datasetCompleto").view()