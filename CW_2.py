#Class work
#Task 1

num_1 = int(input("input first number "))
num_2 = int(input("input second number "))
if num_1 > num_2:
    print ("{} is bigger than {}".format(num_1,num_2))
elif num_1 < num_2:
    print ("{} is bigger than {}".format(num_2,num_1))
else:
    print ("You have input equal values")

#Task 2

num_1 = int(input("Please input any numeric value "))
if num_1 % 2 == 0:
    print ("{} is even number".format(num_1))
else:
    print ("{} is odd number".format(num_1))

#Task 3

num_1 = int(input("Please input any value "))
if num_1 >= 1:
    i = 1
    fact = 1
    while i <= num_1:
        fact *= i
        i += 1
    print ("{}! = {}".format(num_1,fact))
else:
    print ("You have input a wrong number!!!")

#Task 4_1

i = 1
l = 100
print ("Even numbers up to 100: ", end = '')
while i <= l:
    if i % 2 ==0:
        print (i, end = ' ')
    i += 1
else:
    print ("The end!")

#Task 4_2
num_1 = 1
num_2 = range (1, 101)
print ("Even numbers up to 100: ", end = '')

for num_1 in num_2:
    if num_1 % 2 == 0:
        print (num_1, end = ' ')
    num_1 += 1
print ("The end!")

#Task 5_1

print("Odd numbers up to 100: ", end='')
for odd in range(100):
  if odd %2 == 0:
    continue
  print(odd, end=' ')
print ("The end!")

#Task 5_2

odd = 1
print("Odd number up to 100: ", end='')
while odd < 100:
    if odd % 2 != 0:
        print (odd, end = ' ')
    odd += 1
else:
    print ("The end!")

#Task 6

seq = [7, 5, 8]
print (seq)
for i in seq:
    if not(i % 2==0):
        pass
    else:
        print("List consists even numbers")
        break
else:
    print("List doesn\'t consist even numbers")

#Task 7

seq = [8, 4, 7, 1]
k = 0
for i in seq:
    seq[k] = float(seq[k])
    k += 1
print(seq , end=' ')

#Task 8

fib = int(input("Input the last wanted number in Fibonachi series = "))
num_1, num_2 = 0, 1
print('Fibo series = 0 ', end= '')
while num_2 < fib:
    print(num_2, end=' ')
    num_1, num_2 = num_2, num_1 + num_2


