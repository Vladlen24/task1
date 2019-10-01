from graphics import *
w = GraphWin('Animation',800,800)

def snowball():
    a = []
    for i in range(100):
        a.append(Circle(Point(10+10*i,0),2))
        a[i].setFill('cyan')
        a[i].draw(w)
    return a

def move(list1, x, y):
    for b in list1:
        b.move(x, y)

def main():
    figure = snowball()
    while True: 
        move(figure, 0, 1)
        time.sleep(0.1)

main()
w.getMouse()
w.close()
