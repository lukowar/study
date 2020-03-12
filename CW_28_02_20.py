#Task 1

#try:
#    num = int(input("Please input any integer number"))
#    if num % 2 == 0:
#        print ("{} is even number".format(num))
#    elif num % 2 != 0:
#        print ("{ is odd number}".format(num))
#    elif num is float:
#        raise ValueError ("You've input a wrong type of number")
#except ValueError as e:
#    print (e)

try:
    num = int(input("Please input any integer number "))
    if num == 0:
        raise ValueError ("You've input a wrong type of number")
    elif num % 2 == 0:
        print ("{} is even number".format(num))
    elif num % 2 != 0:
        print ("{} is odd number".format(num))
except ValueError as e:
    print (e)


#Task 2

#try:
#    num = int(input("Please enter your age "))
#    if num <= 0:
#        raise ValueError ("You've input an impossible age value")
#    elif num % 2 == 0:
#        print ("Your age is {} and it is even number".format(num))
#    elif num % 2 != 0:
#        print ("Your age is {} and it is odd number".format(num))
#except ValueError as e:
#    print (e)
##################

def age_input (age):
    try:
        age = int(input("Please input your actual age as integer number "))
        if age <= 0:
            raise ValueError ("You've input an impossible age value")
        elif age % 2 == 0:
            print ("Your age is {} and it is even number".format(age))
        elif age % 2 != 0:
            print ("Your age is {} and it is odd number".format(age))
    except ValueError as e:
        print (e)

my_age = age_input(0)

#Task 3

def num_div (num_1, num_2):
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        print ("Division by zero isn't possible!")
    except NameError:
        print ("You have a name error")
    except SyntaxError:
        print ("Syntax error occured")
    else:
        print ("Result is {}".format(result))
    finally:
        print ("Congrats!")

num_1 = float(input("Please input first number "))
num_2 = float(input("Please input second number "))

my_res = num_div(num_1, num_2)

#Task 4

week = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
#my_day = int(input("Enter the number of the day "))
#print ("You have chosen {}".format(week[my_day]))

try:
    my_day = int(input("Enter the number of the day "))
    if my_day <= 0 or my_day > 7:
        raise DayError ("Your number is wrong")
    print ("You have chosen {}".format(week[my_day]))
except DayError as e:
        print(e)
#else:
#    print ("You have chosen {}".format(week[my_day]))
finally:
    print('Congrats!')


