def altura(self, node):
    if node == None:
        return 0
    alturaEsquerda = self.altura(node.esquerda)
    alturaDireita = self.altura(node.direita)
    return 1 + max(alturaEsquerda, alturaDireita)
