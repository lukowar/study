#Task 1

def ar_mean (*args):
    """Prints arithmetic mean value"""
    print (sum (args)/len(args))
    return     
      
ar_mean (300, 4, 2)

#Task 2

def abs_val (num):
    """Prints absolute value of input number"""
    print ("Absolute value of {} is {}".format(num, abs(num)))
abs_val (int(input("Please input integer value ")))

#Task 3

def find_max_of_nums (arg1, arg2):
  '''Написати функцію, яка знаходить максимальне число з двох чисел'''
  if arg1 > arg2:
    print ('{} is max number'.format(arg1))
  else:
    print ('{} is max number'.format(arg2))

num_1 = int(input("Enter first number "))
num_2 = int(input("Enter second number "))
find_max_of_nums (num_1, num_2)

#Task 4

def square_of_circle ():
  PI=3.14
  r=int(input("Enter radius of Circle "))
  square_circle = PI * (r * r)
  return square_circle
def square_of_triangle ():
  a=int(input("Enter lenght of Triangle's side "))
  h=int(input("Enter lenght of Triangle's height from a "))
  return 0.5*a*h
def square_of_rectangle ():
  a=int(input("Enter first side of rectangle "))
  b=int(input("Enter second side of rectangle "))
  return a*b

type_of_figure=(input("Enter square of which figure you need to count ")).upper()
if type_of_figure=="CIRCLE":
  print (square_of_circle())
elif type_of_figure=="TRIANGLE":
  print (square_of_triangle())
elif type_of_figure=="RECTANGLE":
  print (square_of_rectangle())
