import pgzrun
WIDTH = 1200
HEIGHT = 600

scr = 0
def gamescr(bgcolor, title, info="play the game"):
            screen.fill(bgcolor)
            screen.draw.text(title,center =(WIDTH/2,HEIGHT/2),fontsize=100, color='white',
                            align='center')
            screen.draw.text(info,
                            center=(WIDTH/2,HEIGHT/2+100),
                            fontsize=50,color='white',align='center')
        

def draw():
    if scr == 0:
        gamescr('black','Amazing game','press space to start')
 
    elif scr == 1:
        gamescr('green','game is running','press esc to exit')
    elif scr == 2:
        gamescr('red','game over','press escape to start')
           
def update():
    global scr
    if keyboard.SPACE and scr == 0:
        scr=1
    elif keyboard.ESCAPE and scr ==1:
        scr = 2
    if keyboard.RETURN and scr == 2:
        scr = 0
    print(scr)
pgzrun.go()