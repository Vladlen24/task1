from graphics import *
win = GraphWin("House",800,600)

def rec(x1=250,y1=270,x2=550,y2=570,color='#9a653f'):
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


rec(0,0,800,400,'#5bd0ff')
rec(0,400,800,600,'green')
rec(245,265,555,575,'black')
rec()
rec(420,350,533,570,'brown')
rec(425,355,528,565,'#9a653f')
pol(235,255,565,255,400,35,'#ff7c04')
rec(220,255,580,265,'#ff0104')
cir(400,190,55,'brown')
cir(400,190,50,'#0296ff')
rec(266,326,384,484,'brown')
rec(270,330,380,480,'cyan')

win.getMouse()
win.close()
