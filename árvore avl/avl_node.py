class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    # Altura do nó
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Fator de balanceamento
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Rotação à direita
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # Rotação à esquerda
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Inserção balanceada
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # valores duplicados não são inseridos

        # Atualizar altura
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Verificar balanceamento
        balance = self.get_balance(root)

        # Casos de rotação
        # Esquerda-Esquerda
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Direita-Direita
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Esquerda-Direita
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Direita-Esquerda
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Busca
    def search(self, root, key):
        if not root or root.key == key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Obter o menor valor de uma subárvore
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Remoção balanceada
    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Nó com um ou nenhum filho
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Nó com dois filhos → pegar o sucessor
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Atualizar altura
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Balancear
        balance = self.get_balance(root)

        # Casos de rotação
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Travessia em ordem (in-order)
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.key] + self.inorder(root.right)

    # Travessia pré-ordem
    def preorder(self, root):
        if not root:
            return []
        return [root.key] + self.preorder(root.left) + self.preorder(root.right)