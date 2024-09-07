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
tree.insert(6)

# tree.delete(4)
tree.delete(10)
tree.delete(25)
tree.delete(6)
tree.delete(8, show=True)

print(tree.uncle(15))
print(tree.grandfather(4))
print(tree.father(4))
x = tree.GetLevel(4)
print(x)
