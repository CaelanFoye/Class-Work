x = 0

def setup():
    size(640, 480)


def draw():
    global x
    
    if x >= 640:
        x = 0
    x += 1
    
    background(135, 206, 250)  # sky blue
    
    # cloud
    noStroke()
    ellipse(x+25, 50+25, 50, 50)
    ellipse(x-25, 50+25, 50, 50)
    ellipse(x, 50, 50, 50)
    ellipse(x,50-25,50,50)
   
    ellipse(x-190, 50-30, 50, 50)
    ellipse(x-220, 50, 50, 50)
    ellipse(x-200, 50, 50, 50)
    ellipse(x-170, 50, 50, 50)
    fill("#31B522")
    
    noStroke()
    rect(0,height/1.25,640,480)
    fill(255,255,255)
    
