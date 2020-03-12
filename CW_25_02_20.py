Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: C:/Users/Adm/SoftServe/task_1_25Feb Triangle_Rectangle.py ======

>>> class Polygon:
        def __init__(self, no_of_sides):
            self.n = no_of_sides
            self.sides = [0 for i in range(no_of_sides)]

        def inputSides(self):
            self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

        def dispSides(self):
            for i in range(self.n):
                print("Side",i+1,"is",self.sides[i])

>>> class Triangle(Polygon):
        def __init__(self):
            Polygon.__init__(self,3)  #super().__init__(3) 

        def findArea(self):
            a, b, c = self.sides
            s = (a + b + c) / 2
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print('The area of the triangle is %0.2f' %area)

>>> t = Triangle()

>>> t.inputSides()
Enter side 1 : 4
Enter side 2 : 7
Enter side 3 : 3
>>> t.dispSides()
Side 1 is 4.0
Side 2 is 7.0
Side 3 is 3.0
>>> t.findArea()
The area of the triangle is 0.00
>>> t.inputSides()
Enter side 1 : 2
Enter side 2 : 3
Enter side 3 : 4
>>> t.findArea()
The area of the triangle is 2.90
>>> class Rectangle(Polygon):
	def __init__(self):
		Polygon.__init__(self, 2)
	def findArea (self):
		a,b = self.sides
		area = a * b
		print ("The area of rectangle is {}".format(area))

>>> r = Rectangle()
>>> r.inputSides()
Enter side 1 : 5
Enter side 2 : 4
>>> r.findArea()
The area of rectangle is 20.0


>>> class Automobile:
	def __init__(self, make, model):
		self.m = make
		self.t = model
	def start(self):
		print ("You have started the {} {}".format(self.m, self.t))
	def stop(self):
		print ("You have stopped the {} {}".format(self.m, self.t))

>>> my_car = Automobile (make = "Ford", model = "Focus")
>>> my_car.start()
You have started the Ford Focus
>>> my_car.stop()
You have stopped the Ford Focus
>>> my_car = Automobile ("Ford", "Focus")
>>> my_car.start()
You have started the Ford Focus
>>> class Person:
	def __init__ (self, name)
	
SyntaxError: invalid syntax
>>> class Person:
	def __init__ (self, name):
		self.name = input ("Enter the name")
	def printInfo (self):
		print ("Hello, my name is {}".format(self.name))

>>> hum = Person()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    hum = Person()
TypeError: __init__() missing 1 required positional argument: 'name'
>>>
