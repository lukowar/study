num_1 = input("Input first number: ")
num_2 = input("Input second number: ")
print ("Normal order {0} {1}".format(num_1, num_2))
num_1, num_2 = num_2, num_1
print ("Reverse order {0} {1}".format(num_1, num_2))
