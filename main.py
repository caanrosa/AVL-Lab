from TreeUtils import *
from ConsoleUtils import *
import csv
import os

def evaluateNode(node: Node):
  evaluating = True
  while(evaluating):
      printTitle("Evaluando")
      
      printOption(1, "Obtener el nivel del nodo")
      printOption(2, "Obtener el factor de balanceo del nodo")
      printOption(3, "Encontrar el padre del nodo")
      printOption(4, "Encontrar el abuelo del nodo")
      printOption(5, "Encontrar un tío del nodo")
      
      printOption(0, "ATRÁS")
      
      op = getInputInt()
      
      match op:
            case 1:
                level = tree.GetLevel(node.data)
                
                if(level != -1):
                    printSubtitle("El nivel del nodo {node} es {lvl}".format(node = node.data, lvl = level))
                else:
                    printSubtitle("No se pudo determinar el nivel del nodo") # Esto nunca debería ocurrir

            case 2:
                balance = tree.getBalance(node)
                printSubtitle("El factor de balanceo del nodo {node} es {balance}".format(node = node.data, balance = balance))                
            
            case 3:
                father = tree.father(node.data)
                
                if(father is None):
                    printSubtitle("El nodo {node} no tiene padre".format(node = node.data))
                else:
                    printSubtitle("El padre de {node} es {f}".format(node = node.data, f = father.data))
                    
            case 4:
                grandfather = tree.grandfather(node.data)
                
                if(grandfather is None):
                    printSubtitle("El nodo {node} no tiene abuelo".format(node = node.data))
                else:
                    printSubtitle("El abuelo de {node} es {gf}".format(node = node.data, gf = grandfather.data))
                    
            case 5:
                uncle = tree.uncle(node.data)
                
                if(uncle is None):
                    printSubtitle("El nodo {node} no tiene tío".format(node = node.data))
                else:
                    printSubtitle("Un tío de {node} es {un}".format(node = node.data, un = uncle.data))
                    
            case 0:
                evaluating = False

tree = AVL("Title")

dirname = os.path.dirname(__file__)
file_path = dirname + "/dataset/dataset_movies.csv"

running = True

while(running): 
    printTitle("MENU PRINCIPAL")
    printOption(1, "Insertar un dato del CSV")
    printOption(2, "Eliminar un nodo del árbol")
    printOption(3, "Buscar un nodo y evaluar...")
    printOption(4, "Filtrar y evaluar...")
    printOption(5, "Recorrido por niveles")
    printOption(0, "SALIR")
    
    option = getInputInt()
    printBottom()
    
    match option:
        case 0:
            running = False
            
        case 1:
            printSubtitle("Escriba el numero de fila a agregar")
            num = getInputInt()
            correct = False
            with open(file_path, mode='r') as file:
                lector_csv = csv.DictReader(file)
                for indice, fila in enumerate(lector_csv, start=1):
                    if indice == num:  # Procesar solo la fila que el usuario le pida
                        #titulo = fila['Title']
                        #datos = dict(fila)  # Convertir la fila en un diccionario
                        correct = tree.insert(fila, show=True)
                        break  # Salir del bucle después de insertar la fila 10                    
                
                if(not correct):
                    printSubtitle("Hubo un error insertando esa fila")
                    printSubtitle("Revise que exista y que no esté ya agregada")
        case 2:
            printSubtitle("Escriba el título de la película a eliminar")
            name = getInput()
            
            correct = tree.delete(name, show=True)
            if(not correct):
                printSubtitle("Hubo un error eliminado ese nodo")
                printSubtitle("Puede que este no exista o su nombre esté mal escrito")                    
        case 3:
            printTitle("Búsqueda de un nodo")
            printSubtitle("Escriba el título de la película a buscar")
            
            name = getInput()
            node, parent = tree.search(name)
            
            if(node):
                printMovieInfo(node)                      
                evaluateNode(node)
            else:
                printSubtitle("No se encontró es película en el árbol")
                
        case 4:
            printTitle("Filtrar nodos")
            printSubtitle("Películas estrenadas en el año...")
            
            year = getInputInt()
            
            printSubtitle("... con porcentaje extranjero mayor al nacional.")
            printSubtitle("Y con ingresos del extranjero superiores o iguales a...")
            
            foreign = getInputInt()
            
            found = tree.Validacion_dataset(year, foreign)
            
            if(len(found) == 0):
                printSubtitle("No se encontraron películas que cumplan con esos filtros")
            elif(len(found) == 1):
                printSubtitle("Se encontró una película que cumple con los filtros")
                printMovieInfo(found[0])
                evaluateNode(found[0])
            else:
                printSubtitle("Se encontraron {c} películas que cumplen con los filtros:".format(c = len(found)))
                for i, node in enumerate(found, start=1):
                    printOption(i, node.data)
                
                printOption(0, "CANCELAR")
                printBottom()
                
                printSubtitle("Seleccione la película que quiere evaluar")
                
                selection = -1
                
                while(selection < 0 or selection > len(found)):                
                    selection = getInputInt()
                    
                if(selection != 0):
                    printMovieInfo(found[selection - 1])
                    evaluateNode(found[selection - 1])
                else:
                    printSubtitle("Cancelando...")
  
        case 5:
            printSubtitle("Recorrido por niveles del árbol actual")
            tree.level_order()
            printBottom()