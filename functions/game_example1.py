import pgzrun
HEIGHT = 300
WIDTH = 800
p = Actor('ironman', (100,100))
c = Actor('cookie')

def draw():
    screen.fill('white')
    p.draw()
    c.draw()
pgzrun.go()
 