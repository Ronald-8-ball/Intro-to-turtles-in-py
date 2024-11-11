import turtle
# creating the bgcolour
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400,400)
turtle.title("A square on a canvas")
# creating the shape
board = turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.right(90)
turtle.done()