from graphics import *
win = GraphWin("House",800,600)

def rec(x1=250,y1=270,x2=550,y2=570,color='#9a653f'):                   #прямоугольник
    rec1 = Rectangle(Point(x1,y1),Point(x2,y2))
    rec1.setFill(color)
    rec1.draw(win)

def cir(x=100,y=100,r=50,color='red'):                                  #круг
	cir1 = Circle(Point(x,y),r)
	cir1.setFill(color)
	cir1.draw(win)

def pol(x1=100,y1=100,x2=150,y2=150,x3=125,y3=300,color='blue'):                    #треугольник
	pol1 = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3))
	pol1.setFill(color)
	pol1.draw(win)

def pol5(x1=504,y1=450,x2=510,y2=460,x3=520,y3=460,x4=524,y4=450,x5=514,y5=440,color='brown'):              #пятиугольник
        pol51 = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3),Point(x4,y4),Point(x5,y5))
        pol51.setFill(color)
        pol51.draw(win)

def lin(x1=270+150,y1=380,x2=380+150,y2=380,color='brown',size=10):                         #линия
        lin1 = Line(Point(x1,y1),Point(x2,y2))
        lin1.setFill(color)
        lin1.setWidth(size)
        lin1.draw(win)

'''new functions to make homothetic transformation of geometric objects from the old functions
(x, y) -> ((x+dx)*k, (y+dy)*k)
'''
def new_rec(dx, dy, k, color, x1=250,y1=270,x2=550,y2=570):
    rec((x1+dx)*k,(y1+dy)*k,(x2+dx)*k,(y2+dy)*k, color)
    
def new_cir(dx, dy, k, color, x=100,y=100,r=50):                                  
	cir((x+dx)*k, (y+dy)*k, r*k, color)

def new_pol(dx, dy, k, color, x1=100,y1=100,x2=150,y2=150,x3=125,y3=300):                    #треугольник
	pol((x1+dx)*k, (y1+dy)*k, (x2+dx)*k, (y2+dy)*k, (x3+dx)*k, (y3+dy)*k, color)

def new_pol5(dx, dy, k, color, x1=504,y1=450,x2=510,y2=460,x3=520,y3=460,x4=524,y4=450,x5=514,y5=440):              #пятиугольник
        pol5((x1+dx)*k, (y1+dy)*k, (x2+dx)*k, (y2+dy)*k, (x3+dx)*k, (y3+dy)*k, (x4+dx)*k, (y4+dy)*k, (x5+dx)*k, (y5+dy)*k, color)

def new_lin(dx, dy, k, color, size, x1=270,y1=380,x2=380,y2=380):                         #линия
        lin((x1+dx)*k, (y1+dy)*k, (x2+dx)*k, (y2+dy)*k, color, size*k)


def smoke(k, dx, dy, x1, x2, y1, y2):# draws smoke
    r = k*(x2-x1)/8
    xa = 5*k*x1/8+3*k*x2/8+k*dx
    y = k*(y1+dy-(x2-x1)/8)
    xb = k*(3*x1/8+5*x2/8+dx)

    i = 0
    while y>= 0:
        y = k * (y1 + dy - (x2-x1)/8*(2*i+1))
        c1 = Circle(Point(xa, y), r)
        c1.setFill('gray')
        c1.draw(win)

        c2 = Circle(Point(xb, y), r)
        c2.setFill('gray')
        c2.draw(win)
        i += 1


def roach(x1, x2, y1, y2, color): #cockroach in x1, x2, y1, y2 rectangle
    leg1 = Line(Point(x1, y1), Point(x2, y2))
    leg2 = Line(Point(x2, y1), Point(x1, y2))
    l = ((x2-x1)**2+(y2-y1)**2)**0.5
    leg3 = Line(Point((x1+x2)/2-l/2, (y1+y2)/2), Point((x1+x2)/2+l/2,(y1+y2)/2))
    leg1.draw(win)
    leg2.draw(win)
    leg3.draw(win)
    body = Oval(Point(x1, y1), Point(x2, y2))
    body.setFill(color)
    body.draw(win)
    whisker1 = Line(Point((x1+x2)/2, y1-(x2-x1)/2), Point(x1, y1-(x2-x1)))
    whisker2 = Line(Point((x1+x2)/2, y1-(x2-x1)/2), Point(x2, y1-(x2-x1)))
    whisker1. draw(win)
    whisker2.draw(win)
    c= (x1+x2)/2
    head = Circle(Point(c, y1-(x2-x1)/2), (x2-x1)/2)
    head.setFill(color)
    head.draw(win)
    
    
def tree(x1, y1, x2, y2, color1, color2): # draws a tree at x1, y1, x2, y2 rectangle
    leaves = Oval(Point(x1, y1), Point(x2, y2))
    leaves.setFill(color1)
    leaves.draw(win)
    trunk = Polygon(Point((x1+x2)/2, (y1+y2)/2), Point((7*x1+3*x2)/10, (3*y2-y1)/2), Point((3*x1+7*x2)/10, (3*y2-y1)/2))
    trunk.setFill(color2)
    trunk.draw(win)

def sun(x, y, r, color):# draws sun of arbitrary color w/center at x,y
    import math
    c = Circle(Point(x, y), r)
    c.setFill('yellow')
    c.draw(win)
    p = 6.28/12
    x1= x + 3*r/2
    x2=x + 2*r
    y1=  y
    y2= y
    for i in range(12):
        l = Line(Point(x+3*r/2*math.cos(p*i), y+3*r/2*math.sin(p*i)), Point(x+2*r*math.cos(p*i), y+2*r*math.sin(p*i)))
        l.setFill(color)

def cloud(x1, y1, x2, y2, color): #draws a cloud inside a rectangle (x1,y1), (x2,y2)
    part1 = Oval(Point(x1, y1), Point((x1+x2)/2, y2))
    part2 = Oval(Point((x1+x2)/2, y1), Point(x2, y2))
    part1.setFill(color)
    part2.setFill(color)
    part3 = Oval(Point(3*x1/4+x2/4, y1), Point(3*x2/4+x1/4, y2))
    part3.setFill(color)
    part1.draw(win)
    part2.draw(win)
    part3.draw(win)
    
# details - lightbulbs dont work either
def lightbulbs(x1, y1, x2, color1, color2):
    l = (x2-x1)//15
    A = [color1, color2]
    colors = []
    for i in range(l):
        colors.append(A[l%2])
    for i in range(l):
        new_cir(x1+5*(i+1), y1+5*(i+1), 5, colors[i])
        new_lin(x1+5*(i+1)+5, y1+5, x1+5*(i+1)+10, 'black', 2)
        
lightbulbs(250, 270, 550, 'red', 'green') 

def window_light():
    global window_down_color #doesn't work for some reason - why doesnt a local variable turn into a global one?
    global window_up_color 
    window_down_color = 'yellow'
    window_up_color = 'yellow'



'''how to build a house with arbitrary color, size and position'''
def house(dx, dy, k, roof_color, body_color, cross_color, window_up_color, window_down_color, door_color, osn_color, light_in_window, smoke_b):
    new_rec(dx, dy, k, cross_color, 245,265,555,575)    #обод дома
    new_rec(dx, dy, k, body_color, 250,270,550,570)   #стена дома
    new_rec(dx, dy, k, door_color, 420,350,533,570)    #дверная лутка
    new_rec(dx, dy, k, body_color, 425,355,528,565)  #двери
    new_rec(dx, dy, k, roof_color, 280,85,320,250)   #дымоходная труба
    new_rec(dx, dy, k, roof_color, 260,60,340,85)    #выход трубы
    new_rec(dx, dy, k, cross_color, 265,65,335,80)  #кирпич в трубе
    new_pol(dx, dy, k, roof_color, 235,255,565,255,400,35)   #крыша
    new_rec(dx, dy, k, osn_color, 220,255,580,265)  #основа крыши
    new_cir(dx, dy, k, cross_color, 400,190,55) #обод окна на крыше
    if light_in_window:
        window_light()
    new_cir(dx, dy, k, window_up_color, 400,190,50)   #окно на крыше
    new_rec(dx, dy, k, cross_color, 266,326,384,484)    #обод окна
    new_rec(dx, dy, k, window_down_color, 270,330,380,480) #окно
    new_lin(dx, dy, k, cross_color, 10, 325,330,325,480)    #1-ая лутка окна
    new_lin(dx, dy, k, cross_color, 10, 270,380,380,380)   #2-ая лутка окна
    new_lin(dx, dy, k, cross_color, 10, 352,170,448,170)    #1-ая лутка окна на крыше
    new_lin(dx, dy, k, cross_color, 10, 400,135,400,245)    #2-ая лутка окна на крыше
    new_pol5(dx, dy, k, door_color, 504,450,510,460,520,460,524,450,514,440)  #дверная ручка
    if smoke_b:
        smoke(k, dx, dy, 260, 340, 60, 85)



house(150, 0, 1, '#FF4500', '#A0522D', '#330000', '#3399ff', '#99ccff', '#800000', '#DC143C', True, True) #right house
house(-150, -40, 0.4, 'cyan', '#00ff00', 'magenta', '#0000ff', '#000066', '#800000', 'magenta', True, False) # left house



                   
win.getMouse()
win.close()
