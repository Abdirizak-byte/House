from graphics import *

def clickHouse():
   # Create the window
   win = GraphWin('5 Click House')
   win.setBackground("blue")

   
   #Creating the points to make the base
   p1 = win.getMouse()
   p1.draw(win)
   p2 = win.getMouse()
   p2.draw(win)

   house = Rectangle(p1 , p2)
   house.setFill("Red")
   house.draw(win)


   #The door length will and height
   p3 = win.getMouse()
   

   width = Point(p3.getX() + 0.2, p3.getY() + 0.2)
   p = Oval(p3, width)
   p.draw(win)

   bottom = Point(p3.getX() + 10, p2.getY())

   door = Rectangle(p3, bottom)
   door.setFill("Yellow")
   door.draw(win)

   #Have the Window one the opposite side then the door
   p4 = win.getMouse()


   width = Point(p4.getX() + .2, p4.getY() + .2)
   p = Oval(p4, width)
   p.draw(win)

   winDow = Point(p4.getX()+ 10, p4.getY()-10)

   window = Rectangle(p4,winDow)
   window.setFill("Cyan")
   window.draw(win)

   # Have the 5th point on the top and make the Roof
   p5 = win.getMouse()


   width = Point(p5.getX() + 0.2, p5.getY( + 0.2))
   p = Oval(p5, width)
   p.draw(win)

   tip = Point(p2.getX(), p1.getY())

   roof = Polygon(p1, tip, p5)
   roof.setFill("Grey")
   roof.draw(win)

   win.getMouse()
   win.close()

clickHouse()
    
