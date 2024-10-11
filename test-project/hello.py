import pgzrun
from math import ceil

WIDTH = 500
HEIGHT = 300

red = Actor("red")
red.x = 250
red.y = 250
pig = Actor("pig")
pig.x = 550
pig.y = 120
score = 0
timetick = 1200
ended = False

jumping = False
started = False


def draw():
    screen.clear
    screen.blit("sky1", (0, 0))
    red.draw()
    pig.draw()

    screen.draw.text('Count down: ' + str(ceil(timetick / 60)), (370, 10),
                     color=(255, 255, 255))

    if ended:
        screen.draw.text('Mission completed', (170, 120), color=(107, 27, 148))

    screen.draw.text('Score: ' + str(score), (10, 10), color=(255, 255, 255))

    if not started:
        screen.draw.text('The pig is attacking the bird', (150, 100),
                         color=(107, 27, 148))
        screen.draw.text('Tap on the screen to jump', (160, 120),
                         color=(152, 65, 196))
        screen.draw.text('Click to start', (210, 140), color=(189, 110, 230))


def update():
    global jumping
    global started
    global score
    global timetick
    global ended
    if started and not ended:
        timetick -= 1
        if timetick <= 0:
            started = False
            score = 0
            timetick = 1200
        pig.x -= 3
        if pig.x < -50:
            pig.x = 550
        if red.colliderect(pig):
            pig.x = 550
            score += 1
            if score >= 10:
                ended = True

        red.y += 2
        if red.y > 250:
            red.y = 250
            jumping = False


def on_mouse_down(pos):
    cx, cy = pos
    print(pos)
    global jumping
    global started
    if started and not ended:
        if not jumping:
            red.y = 50
            jumping = True
    else:
        started = True


pgzrun.go()