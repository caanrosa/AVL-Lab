from typing import Any, Optional, Tuple
import graphviz
from graphviz import nohtml

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.balance: Optional["int"] = 0

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
        
    def graph(self):
        g = graphviz.Digraph('g', filename='btree.gv',
                     node_attr={'shape': 'record', 'height': '.1'})
        s = []
        p = self.root
        while p is not None or len(s) > 0:
            if p is not None:
                g.node('{data}'.format(data = p.data), nohtml("<f0>|<f1> {data}|<f2>".format(data = p.data)))
                print(p.data, end = ' ')
                s.append(p)
                
                if(p.left is not None):
                    g.edge("{before}:f0".format(before = p.data), "{actual}:f1".format(actual = p.left.data))

                p = p.left
                    
                    
            else:
                p = s.pop()
                
                if(p.right is not None):
                    g.edge("{before}:f2".format(before = p.data), "{actual}:f1".format(actual = p.right.data))
                    
                p = p.right                
                    
                    
        g.view()
        
            

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

    def search(self, data: Any) -> Tuple[Optional["Node"], Optional["Node"]]:
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
                    pred, pad_pred, son_pred = self.__pred(p)
                    p.data = pred.data
                    if p == pad_pred:
                        pad_pred.left = son_pred
                    else:
                        pad_pred.right = son_pred
                    del pred
                else:
                    sus, pad_sus, son_sus = self.__sus(p)
                    p.data = sus.data
                    if p == pad_sus:
                        pad_sus.right = son_sus
                    else:
                        pad_sus.left = son_sus
                    del sus
            return True
        return False

    def __pred(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.left, node
        while p.right is not None:
            p, pad = p.right, p
        return p, pad, p.left

    def __sus(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.right, node
        while p.left is not None:
            p, pad = p.left, p
        return p, pad, p.right
    
    def node_height(self, node: Node) -> int:
        return super().height_r(node)
    
class AVL(BST):
    def __init__(self, root: Optional["Node"] = None) -> None:
        super().__init__(root)
        
    def insert(self, data: Any) -> bool:
        inserted = super().insert(data)
        if(inserted):
            dummy = Node(data) # Porque siempre será una hoja
            self.balanceTree(dummy)
        
    def balance(self, node: Optional["Node"]) -> int:
        if(node is None):
            return 0
        return super().node_height(node.right) - super().node_height(node.left)
            
    def balanceTree(self, until: Node):
        self.__balanceTree_r(until, self.root)
        
    def __balanceTree_r(self, until: Node, node: Node, parent: Optional["Node"] = None) -> int:
        if(node.data == until.data):
            parentBalance = self.balance(parent)
            print(parentBalance)
            return parentBalance
        else:
            if(until.data > node.data):
                return self.__balanceTree_r(until, node.right, node)
            else:
                return self.__balanceTree_r(until, node.left, node)