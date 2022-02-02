from turtle import *


# Função que gera a arvore Y
def y_tree(tamanho, nivel):

    if nivel > 0:
        colormode(255)
        pencolor(0, 255//nivel, 0)

        # Desenhando a base
        forward(tamanho)
        right(angulo)

        # Criando ramificações da árvore
        y_tree(0.8 * tamanho, nivel-1)
        pencolor(0, 255//nivel, 0)

        left(2 * angulo)
        y_tree(0.8 * tamanho, nivel-1)

        pencolor(0, 255//nivel, 0)
        right(angulo)
        forward(-tamanho)


# Angulo entre a base e a ramificação de Y
angulo = 30

# Indicando a velocidade da caneta e virando-a para cima
speed('fastest')
right(-90)

# Inciando a função
y_tree(80, 7)
