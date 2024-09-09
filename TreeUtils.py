from typing import Any, Optional, Tuple
import graphviz
from graphviz import nohtml

class Node:
    def __init__(self, data: Any):
        self.info = data
        self.data = data['Title']
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

class BinaryTree:

    def __init__(self, root: Optional["Node"] = None) -> None:
        self.root = root

    def preorder(self) -> None:
        self.__preorder_r(self.root)
        print()

    def __preorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            print(node.data, end = ' ')
            self.__preorder_r(node.left)
            self.__preorder_r(node.right)

    def preorder_nr(self) -> None:
        s = []
        p = self.root
        while p is not None or len(s) > 0:
            if p is not None:
                print(p.data, end = ' ')
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                p = p.right
        print()

    def inorder(self) -> None:
        self.__inorder_r(self.root)
        print()

    def __inorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            self.__inorder_r(node.left)
            print(node.data, end = ' ')
            self.__inorder_r(node.right)

    def inorder_nr(self) -> None:
        s = []
        p = self.root
        while p is not None or len(s) > 0:
            if p is not None:
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                print(p.data, end = ' ')
                p = p.right
        print()

    def postorder(self) -> None:
        self.__postorder_r(self.root)
        print()

    def __postorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            self.__postorder_r(node.left)
            self.__postorder_r(node.right)
            print(node.data, end = ' ')

    def levels_nr(self) -> None:
        q = []
        p = self.root
        q.append(p)
        while len(q) > 0:
            p = q.pop(0)
            print(p.data, end = ' ')
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        print()

    def height(self) -> int:
        return self.height_r(self.root)

    def height_r(self, node: Optional["Node"]) -> int:
        if node is None:
            return 0
        return 1 + max(self.height_r(node.left), self.height_r(node.right))              

    @staticmethod
    def generate_sample_tree() -> "BinaryTree":
        T = BinaryTree(Node('A'))
        T.root.left = Node('B')
        T.root.right = Node('C')
        T.root.left.left = Node('D')
        T.root.left.right = Node('E')
        T.root.right.right = Node('F')
        T.root.left.left.left = Node('G')
        T.root.left.left.right = Node('H')
        T.root.right.right.left = Node('I')
        T.root.right.right.right = Node('J')
        T.root.left.left.right.left = Node('K')

        return T
    
# ABB
class BST(BinaryTree):

    def __init__(self, root: Optional["Node"] = None) -> None:
        super().__init__(root)

    def search(self, data: str) -> Tuple[Optional["Node"], Optional["Node"]]:
        p, pad = self.root, None
        while p is not None:
            if data == p.data:
                return p, pad
            else:
                pad = p
                if data < p.data:
                    p = p.left
                else:
                    p = p.right
        return p, pad

    def insert(self, data: Any) -> bool:
        to_insert = Node(data)
        if self.root is None:
            self.root = to_insert
            return True
        else:
            p, pad = self.search(data)
            if p is not None:
                return False
            else:
                if data < pad.data:
                    pad.left = to_insert
                else:
                    pad.right = to_insert
                return True

    def delete(self, data: Any, mode: bool = True) -> bool:
        p, pad = self.search(data)
        if p is not None:
            if p.left is None and p.right is None:
                if p == pad.left:
                    pad.left = None
                else:
                    pad.right = None
                del p
            elif p.left is None and p.right is not None:
                if p == pad.left:
                    pad.left = p.right
                else:
                    pad.right = p.right
                del p
            elif p.left is not None and p.right is None:
                if p == pad.left:
                    pad.left = p.left
                else:
                    pad.right = p.left
                del p
            else:
                if mode:
                    pred, pad_pred, son_pred = self.pred(p)
                    p.data = pred.data
                    if p == pad_pred:
                        pad_pred.left = son_pred
                    else:
                        pad_pred.right = son_pred
                    del pred
                else:
                    sus, pad_sus, son_sus = self.sus(p)
                    p.data = sus.data
                    if p == pad_sus:
                        pad_sus.right = son_sus
                    else:
                        pad_sus.left = son_sus
                    del sus
            return True
        return False

    def pred(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.left, node
        while p.right is not None:
            p, pad = p.right, p
        return p, pad, p.left

    def sus(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.right, node
        while p.left is not None:
            p, pad = p.left, p
        return p, pad, p.right
    
    def node_height(self, node: Node) -> int:
        return super().height_r(node)
    
class AVL(BST):
    def __init__(self, metric: str, root: Optional["Node"] = None) -> None:
        super().__init__(root)
        self.metric = metric
        
    def delete(self, data: str, mode: bool = True, show: bool = False) -> bool:
        forDeletion = None
        parentDeletion = None
        p, pad = self.search(data)
        if p is not None:
            if p.left is None and p.right is None:
                if(pad is not None):
                    if p == pad.left:
                        pad.left = None
                    else:
                        pad.right = None
                else:
                    self.root = p.left
                
                forDeletion = p
                parentDeletion = pad
            elif p.left is None and p.right is not None:
                if(pad is not None):
                    if p == pad.left:
                        pad.left = p.right
                    else:
                        pad.right = p.right
                else:
                    self.root = p.right
                    
                forDeletion = p
                parentDeletion = pad
            elif p.left is not None and p.right is None:
                if(pad is not None):
                    if p == pad.left:
                        pad.left = p.left
                    else:
                        pad.right = p.left
                else:
                    self.root = None
                    
                forDeletion = p
                parentDeletion = pad
            else:
                if mode:
                    pred, pad_pred, son_pred = self.pred(p)
                    p.data = pred.data
                    p.info = pred.info
                    if p == pad_pred:
                        pad_pred.left = son_pred
                    else:
                        pad_pred.right = son_pred
                    forDeletion = pred
                    parentDeletion = pad_pred
                else:
                    sus, pad_sus, son_sus = self.sus(p)
                    p.data = sus.data
                    p.info = sus.info
                    
                    if p == pad_sus:
                        pad_sus.right = son_sus
                    else:
                        pad_sus.left = son_sus
                    forDeletion = sus
                    parentDeletion = pad_sus
            
            self.root = self.__delete_balance_r(parentDeletion, self.root)
            if(show): self.graph("lastDeletion").view()
            
            del forDeletion
            
            return True
        else:
            return False
    
    def __delete_balance_r(self, parentOfDeletion: Optional[Node], node: Optional[Node] = None):
        if(parentOfDeletion is None): return node
        # El padre del nodo eliminado es aquel que puede tener un balance 2 o -2 !! REVISAR/INVESTIGAR/PROBAR QUE ESTO SEA CIERTO SIEMPRE
        if(node.data == parentOfDeletion.data):
            print("Se llegó al padre del eliminado: {}".format(node.data))
            
            balance = self.getBalance(node)
            print("balance {}".format(balance))
            
            if(balance == 2): # La eliminacion se hizo del lado izquierdo, porque hay más a la derecha
                rightBalance = self.getBalance(node.right)
                if(rightBalance >= 0): # 1 o 0. En caso de ser 1 tambien se hace rotacion izquierda simple
                    node = self.slr(node)
                else: # Si es -1, significa una doble rotacion derecha-izquierda
                    node = self.drlr(node)
            elif(balance == -2): # La eliminacion se hizo del lado derecho, porque hay más a la izquierda
                leftBalance = self.getBalance(node.left)
                if(leftBalance <= 0): # Si es 0 o -1 hacer rotacion simple hacia la derecha
                    node = self.srr(node)
                else: # Si es 1, toca hacer una doble rotacion izquierda-derecha
                    node = self.dlrr(node)                
        else:
            # Si aun no se ha llegado al padre del nodo borrado seguir adentrandose al arbol
            if(parentOfDeletion.data > node.data):
                node.right = self.__delete_balance_r(parentOfDeletion, node.right)
            elif(parentOfDeletion.data < node.data):
                node.left = self.__delete_balance_r(parentOfDeletion, node.left)
        return node
    
    def insert(self, data: Any, show: Optional[bool] = False) -> bool:
        s = self.search(data[self.metric])
        if(s[0] is not None): # Si ya existe, no agregar
            return False
        else: # Si no existe, seguir
            self.root = self.__insert_r(data, self.root) # Insertar recursivamente
            if(show): self.graph("lastInsert").view()
            return True
        
    def __insert_r(self, data: Any, node: Optional[Node] = None):
        # Si el nodo actual está vacío (None), retornarlo (insertarlo)
        if(not node):
            print("✅ Se insertó {data} correctamente".format(data=data))
            return Node(data)
        elif(data[self.metric] < node.data): # Si la informacion a insertar es menor al nodo actual insertarla en la izquieda
            node.left = self.__insert_r(data, node.left)
        elif(data[self.metric] > node.data): # Si la informacion a insertar es mayor al nodo actual insertarla en la derecha
            node.right = self.__insert_r(data, node.right)
        
        # Cuando finalmente se logre insertar, se halla el equilibrio del nodo actual (el padre del que se acaba de insertar) y sigue subiendo 
        # hasta llegar nuevamente a la raiz
        
        balance = self.getBalance(node)
        print("NODE: {node}, balance: {bal}".format(node = node.data, bal = balance))
        # Apenas se encuentra un nodo desbalanceado, se hace la rotacion correspondiente para rebalancearlo
        if(balance == -2):
            # Como el balance es -2 significa que hay más hijos del lado izquierdo que el derecho
            # Por lo tanto está garantizado que existe un hijo directo a la izquierda
            if(data[self.metric] < node.left.data): # Si la información que se insertó es menor que la del hijo izquierdo, significa que el nodo nuevo está a la izquierda de este (ROTACION DERECHA)
                return self.srr(node)
            else: # Si es mayor significa que está a su derecha y hay que hacer una doble rotacion (IZQUIERDA DERECHA)
                return self.dlrr(node)
        if(balance == 2):
            # Como el balance es 2 significa que hay más hijos del lado derecho
            if(data[self.metric] > node.right.data): # Si la información insertada debe estar a la derecha del hijo derecho del nodo actual se hace hace una rotacion simple (de izquierda)
                return self.slr(node)
            else: # Si está a la izquierda se hace una rotacion doble (derecha izquierda)
                return self.drlr(node)
        
        return node
            
        
    def getBalance(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return super().node_height(node.right) - super().node_height(node.left)
                            
    def slr(self, node: Node) -> Node:
        print("IZQUIERDA!")
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux
    
    def srr(self, node: Node) -> Node:
        print("DERECHA!")
        aux = node.left
        node.left = aux.right
        aux.right = node
        return aux
    
    def drlr(self, node: Node) -> Node:
        print("CALLING: DERECHA-IZQUIERDA!")
        node.right = self.srr(node.right)
        return self.slr(node)
    
    def dlrr(self, node: Node) -> Node:
        print("CALLING IZQUIERDA-DERECHA!")
        node.left = self.slr(node.left)
        return self.srr(node)
    
    def graph(self, fileName: Optional[str] = "btree") -> graphviz.Digraph:
        print("GRAFICANDO...")
        g = graphviz.Digraph('g', filename='{name}.gv'.format(name = fileName),
                     node_attr={'shape': 'record', 'height': '.1'})
        s = []
        p = self.root
        while p is not None or len(s) > 0:
            if p is not None:
                g.node('{data}'.format(data = self.normalizeData(p.data)), nohtml("<f0>|<f1> {data}|<f2> {balance}".format(data = p.data, balance = self.getBalance(p))))
                print(p.data, end = ' ')
                s.append(p)
                
                if(p.left is not None):
                    g.edge("{before}:f0".format(before = self.normalizeData(p.data)), "{actual}:f1".format(actual = self.normalizeData(p.left.data)))

                p = p.left
                    
                    
            else:
                p = s.pop()
                
                if(p.right is not None):
                    g.edge("{before}:f2".format(before = self.normalizeData(p.data)), "{actual}:f1".format(actual = self.normalizeData(p.right.data)))
                    
                p = p.right                
                    
        print()
        return g
    
      # Función para encontrar el "tío" de un nodo
    def uncle(self, elem: str) -> Optional["Node"]:
        # Buscar el nodo y su padre
        p, pad = self.search(elem)
        
        # Si el padre no existe, el nodo no tiene tio
        if pad is None:
            return None
        
        # Buscar al abuelo (padre del padre)
        pad, gftr = self.search(pad.data)
        
        # Si el abuelo no existe, tampoco hay tio
        if gftr is None:
            return None
        
        # Buscar el tio
        if pad == gftr.left:
            return gftr.right
        else:
            return gftr.left
        
    def grandfather(self, elem: str) -> Optional["Node"]:
        # Busca el nodo y a su padre
        p, pad = self.search(elem)
        
        # Si no hay padre, no hay abuelo
        if pad is None:
            return None
        
        pad_node, gftr = self.search(pad.data)  # Agarramos al padre del padre (abuelo)
        return gftr
    
    def father(self, elem: str) -> Optional["Node"]:
        node, pad = self.search(elem)  # Buscamos el nodo y su padre, pero retornamos solo al padre
        return pad
    
    def GetLevel(self, elem):
        level = 0  # Contador de niveles 
        node = self.root
        while node is not None:
            if (elem == node.data):
                return level    # Si el nodo es la raiz
            elif (elem < node.data):
                node = node.left    # Nos movemos de derecha a izquierda a derecha sumand
            else:
                node = node.right
            level += 1
        return -1 
    
    def level_order(self) -> None:
        h = self.height()  # Calcula la altura del árbol para saber cuántas veces lo recorre
        for i in range(1, h + 1):
            self.print_current_level(self.root, i)
        print()

    # Imprime TODOS los nodos que están en un nivel específico del árbol 
    def print_current_level(self, node: Optional["Node"], level: int) -> None:
        if node is None:
            return
        if level == 1:
            print("[{}]".format(node.data), end=" ")
        elif level > 1:
            self.print_current_level(node.left, level - 1)
            self.print_current_level(node.right, level - 1)
    def normalizeData(self, string):
        return string.replace(" ", "").replace(":", "")

    def Validacion_dataset(self,year,foreign) -> list[Node]:
        p = self.root
        s = []
        r = []
        while p is not None or len(s) > 0:
                if p is not None:
                    s.append(p)
                    p = p.left
                else:
                    p = s.pop()
                    if((int(p.info['Year']) == year) & (float(p.info['Foreign Percent Earnings']) > float(p.info['Domestic Percent Earnings'])) & (int(p.info['Foreign Earnings']) >= foreign)):                        
                        r.append(p)
                    p = p.right
        return r  
