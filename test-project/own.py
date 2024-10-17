import pgzero


rb = Actor('red')
rb.pos = 100,56

WIDTH = 200
HEIGHT = rb.height +20

rb.topright = 0,10

def draw():
    screen.clear()
    rb.draw()

def update():
    rb.left += 2
    if rb.left> WIDTH:
        rb.right = 0

def on_mouse_down():
    rb.y -=1