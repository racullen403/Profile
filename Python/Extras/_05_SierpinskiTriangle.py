import turtle

t = turtle.Turtle()
display = turtle.Screen()


def draw(t, line):
    if line > 0:
        t.forward(line)
        t.right(90)
        draw(t, line-2)


# draw(t, 50)
""" 
Drawing out trees by recursion is a great way to visualise the order of function calls.
"""


def tree(t, line):
    if line > 5:
        t.forward(line)
        t.right(15)
        tree(t, line - 10)
        t.left(30)
        tree(t, line - 10)
        t.right(15)
        t.backward(line)


# tree(t, 50)

# display.exitonclick()


""" 
Sierpinski Triangle:

This fractal is created as follows,

    - Create a filled in triangle using the the coordinates of the corners.
    - Fill in 3 new triangles using the midpoints of the the sides of the previous.
    - Continue like this for some specified number of degrees
    
"""


def triangle(t, coords, colour):
    t.fillcolor(colour)
    t.up()
    t.goto(coords[0][0], coords[0][1])
    t.begin_fill()
    t.goto(coords[1][0], coords[1][1])
    t.goto(coords[2][0], coords[2][1])
    t.goto(coords[0][0], coords[0][1])
    t.end_fill()


def mid_point(coord1, coord2):
    return (coord1[0] + coord2[0]) / 2, (coord1[1] + coord2[1]) / 2


def sierpinski_triangle(t, coords, degree):
    colours = ["blue", "red", "green", "white", "yellow", "orange", "violet"]
    triangle(t, coords, colours[degree])
    if degree > 0:
        # Bottom left triangle
        sierpinski_triangle(
            t,
            [coords[0], mid_point(coords[0], coords[1]), mid_point(coords[0], coords[2])],
            degree - 1
        )
        # Top Triangle
        sierpinski_triangle(
            t,
            [mid_point(coords[0], coords[1]), coords[1], mid_point(coords[1], coords[2])],
            degree - 1
        )
        # Bottom right triangle
        sierpinski_triangle(
            t,
            [mid_point(coords[0], coords[2]), mid_point(coords[1], coords[2]), coords[2]],
            degree - 1
        )


def example():
    sierpinski_triangle(t, [(-200, -200), (0, 200), (200, -200)], 5)
    display.exitonclick()