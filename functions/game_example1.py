import pgzrun
HEIGHT = 300
WIDTH = 800
p = Actor('ironman', (100,100))
c = Actor('cookie')

def draw():
    screen.fill('white')
    p.draw()
    c.draw()
    print('drawing')
def update():
    print('updating')
    p.x -= 3
    p.angle = -10
    if p.x < 0:
        p.x = WIDTH
    print(p.x, p.y)
pgzrun.go()
 