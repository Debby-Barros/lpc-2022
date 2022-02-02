import turtle
import math


def fibonacci(n):

    num_anterior = 0
    num_atual = 1
    quadrado_anterior = num_anterior
    quadrado_atual = num_atual

    # Reproduzindo o primeiro quadrado
    pen.forward(num_atual * escala)
    pen.left(90)
    pen.forward(num_atual * escala)
    pen.left(90)
    pen.forward(num_atual * escala)
    pen.left(90)
    pen.forward(num_atual * escala)

    # Atualizando a serie de Fibonacci
    aux = quadrado_atual
    quadrado_atual = quadrado_atual + quadrado_anterior
    quadrado_anterior = aux

    # Reproduzindo os demais quadrados da serie
    for i in range(1, n):
        pen.backward(quadrado_anterior * escala)
        pen.right(90)
        pen.forward(quadrado_atual * escala)
        pen.left(90)
        pen.forward(quadrado_atual * escala)
        pen.left(90)
        pen.forward(quadrado_atual * escala)

        # Atualizando a serie de Fibonacci
        aux = quadrado_atual
        quadrado_atual = quadrado_atual + quadrado_anterior
        quadrado_anterior = aux

    # Reiniciando a caneta
    pen.penup()
    pen.setposition(escala, 0)
    pen.seth(0)
    pen.pendown()
    pen.pencolor("red")

    # Reproduzindo a espiral de Fibonacci
    pen.left(90)
    for i in range(n):
        print(num_atual)

        # Calculando as espirais
        fdwd = math.pi * num_atual * escala / 2
        fdwd /= 90

        for j in range(90):
            pen.forward(fdwd)
            pen.left(1)

        # Atualizando a serie de Fibonacci
        aux = num_anterior
        num_anterior = num_atual
        num_atual = aux + num_atual


escala = int(input("Informe a escala para vizualização da espiral: "))
num = int(input("Informe o número de repetições (deve ser > 1): "))

if num > 0:
    print("Serie de Fibonacci para {} elementos: ".format(num))

    # Iniciando a tela e a função principal
    pen = turtle.Turtle()
    pen.speed(100)
    fibonacci(num)

    # Pausa o programa
    turtle.done()

else:
    print("É necessário que o valor seja > 1 ")
