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

def lin(x1=270,y1=380,x2=380,y2=380,color='brown',size=10):                         #линия
        lin1 = Line(Point(x1,y1),Point(x2,y2))
        lin1.setFill(color)
        lin1.setWidth(size)
        lin1.draw(win)



rec(0,0,800,400,'#5bd0ff')  #небо
rec(0,400,800,600,'green')  #трава
rec(245,265,555,575,'black')    #обод дома
rec()   #стена дома
rec(420,350,533,570,'brown')    #дверная лутка
rec(425,355,528,565,'#9a653f')  #двери
rec(280,85,320,250,'#ff7c04')   #дымоходная труба
rec(260,60,340,85,'#ff7c04')    #выход трубы
rec(265,65,335,80)  #кирпич в трубе
pol(235,255,565,255,400,35,'#ff7c04')   #крыша
rec(220,255,580,265,'#ff0104')  #основа крыши
cir(400,190,55,'brown') #обод окна на крыше
cir(400,190,50,'#0296ff')   #окно на крыше
rec(266,326,384,484,'brown')    #обод окна
rec(270,330,380,480,'cyan') #окно
lin(325,330,325,480)    #1-ая лутка окна
lin()   #2-ая лутка окна
lin(352,170,448,170)    #1-ая лутка окна на крыше
lin(400,135,400,245)    #2-ая лутка окна на крыше
pol5()  #дверна ручка


win.getMouse()
win.close()
