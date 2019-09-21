from graphics import *
win = GraphWin("House",800,600)

def rec(x1=250,y1=270,x2=550,y2=570,color='brown'):
    rec1 = Rectangle(Point(x1,y1),Point(x2,y2))
    rec1.setFill(color)
    rec1.draw(win)

def cir(x=100,y=100,r=50,color='red'):
	cir1 = Circle(Point(x,y),r)
	cir1.setFill(color)
	cir1.draw(win)

def pol(x1=100,y1=100,x2=150,y2=150,x3=125,y3=300,color='blue'):
	pol1 = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3))
	pol1.setFill(color)
	pol1.draw(win)


rec(0,0,800,400,'blue')
rec(0,400,800,600,'green')
rec(245,265,555,575,'brown')
rec()
rec(220,260,580,270,'black')
pol(235,260,565,260,400,40,'yellow')
cir(400,200,55,'brown')
cir(400,200,50,'blue')
rec(266,326,384,484,'brown')
rec(270,330,380,480,'cyan')

win.getMouse()
win.close()
