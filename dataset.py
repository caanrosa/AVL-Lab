from TreeUtils import *
import csv

file_path = "/dataset/dataset_movies.csv"
tree = AVL()


with open(file_path, mode='r') as file:
    lector_csv = csv.DictReader(file)
    for fila in lector_csv:
        titulo = fila['Title']
        datos = dict(fila)  # Convertir la fila en un diccionario
        tree.insert(titulo, datos)

