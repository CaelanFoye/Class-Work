x = 0

def setup():
    size(640,480)

def draw():
    global x
    if x == 640:
        x = 0
    x += 1
    background(135,206,235)
    noStroke()
    ellipse(x,50,50+30,80)
    ellipse(x+40,50+25,80,80)
    ellipse(x-40,50+25,80,80)
    ellipse(x,50+30,80,80)
    
    
