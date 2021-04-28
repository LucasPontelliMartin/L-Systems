#*RA/Nome:
#*082180042 - Arthur Ferreira Rocha
#*082180041 - Ronaldo Vicente Lopes
#*081190042 - Lucas Pontelli Martin
#*082180003 - Clarissa Reis Fonseca

import turtle

generations = 4
size = 20
rule = ("F", "FF+[+F-F-F]-[-F+F+F]")
sentence = "F"
positions = []
gen = turtle.Turtle()
gen.setposition(0, -550)
gen.speed(80)
gen.left(90)

for i in range(generations):
    sentence = sentence.replace(*rule)

for op in sentence:
    if op == "F":
        gen.forward(size)
    elif op == "+":
        gen.right(size)
    elif op == "-":
        gen.left(size)
    elif op == "[":
        positions.append(gen.position())
    elif op == "]":
        gen.setposition(positions.pop())

turtle.exitonclick()