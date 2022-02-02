import turtle

# Criando a tela e a caneta
tela = turtle.Screen()
pen = turtle.Turtle()


def triangulo(x, y):

    # A caneta é iniciada na posição do click do mouse
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Desenhando o triangulo
    for i in range(3):
        pen.forward(100)
        pen.left(120)
        pen.forward(100)


# Identifica o click do mouse
turtle.onscreenclick(triangulo, 1)
turtle.listen()

# Pausa o programa
turtle.done()
