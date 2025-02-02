import pgzrun

WIDTH=300
HEIGHT=300
def draw():

    screen.fill("red")
    r=Rect((140,0),(150,100))
    screen.draw.filled_rect(r,"yellow")

    re=Rect((0,170),(150,100))
    screen.draw.rect(re,"yellow")


pgzrun.go()