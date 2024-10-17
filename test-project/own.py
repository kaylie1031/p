import pgzero


rb = Actor('red')
rb.pos = 100,56

WIDTH = 200
HEIGHT = rb.height +20

def draw():
    screen.clear()
    rb.draw()