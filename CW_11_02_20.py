#Task 1

list_len = range (int ( input ("Inup list length ")))
my_list = []
for i in list_len:
    my_list.append(int ( input("enter {} number ".format(i))))
print (my_list)
print ("List max number is {}".format(max(my_list)))
print ("List min number is {}".format(min(my_list)))

#Task 2

#my_list = [ x for x in range (1, 11) ]
#print (my_list)
#print ("Even numbers:")
#for i in range(10):
#    if my_list[i]%2 == 0:
#        print (my_list[i])
#print ("Devides by 3:")
#for i in range(10):
#    if my_list[i]%3 == 0:
#        print (my_list[i])
#print ("Don't devide by 2 & 3:")
#for i in range(10):
#    if my_list[i]%2 != 0 and my_list[i]%3 != 0:
#        print (my_list[i])
##########################

even_num_list = [ x for x in range (1, 11) if x%2 == 0]
print ("List of even numbers in range of 10 is {}".format(even_num_list))
dev_3_list = [ x for x in range (1, 11) if x%3 == 0]
print ("List of numbers devided by 3 in range of 10 is {}".format(dev_3_list))
not_dev_2_3 = [ x for x in range (1, 11) if x%3 != 0 and x%2 != 0]
print ("List of numbers not devided by 2 & 3 in range of 10 is {}".format(not_dev_2_3))

#Task 3

fact = int(input("Please enter the number for factorial calculation "))
fact_rang = range(1, fact+1)
fact_calc = 1
if fact < 0:
    print ("You have input negative value, please try again")
elif fact == 0:
    print ("Input value is 0, please try again")
else:
    for i in fact_rang:
        fact_calc = fact_calc * i
    print ("The factorial of {} is equal to {}".format(fact,fact_calc))

#Task 4

login=input("Enter your login: ")
while login != str('First'):
    login=input("Entered login is incorrect! \nEnter your login again: ")
else:
    print("Welcome, ", login)

#Task 5

mylist=[]
n = int(input("Please enter the element: "))
while n > 0:
    mylist.append(n)
    n = int(input("Please enter the element: "))
else:
    print(mylist)

#Task 6

nums = []
k=int(input("Please enter the count of the elements of sequence: "))
for i in range(k):
     n = int(input("Please enter the element: "))
     nums.append(n)
     if n>0:
       continue
     else:
       nums.pop()
       break
print("You enter not valid value")
