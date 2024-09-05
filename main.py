from TreeUtils import *

tree = AVL()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(20)
tree.insert(25)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.insert(6, True)

tree.delete(4, show=True)
tree.delete(10, show=True)