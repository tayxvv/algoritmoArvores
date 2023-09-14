from BinaryTree import BinaryTree

tree = BinaryTree()
print(tree)
tree.insertNode(5)
tree.insertNode(3)
tree.insertNode(7)
tree.insertNode(6)
tree.insertNode(9)
tree.insertNode(2)
tree.insertNode(1)

tree.printTree()

valorABuscar = int(input("Digite o valor a buscar: "))
if tree.search(valorABuscar):
    print("Valor encontrado")
else:
    print("Valor não encontrado")   
