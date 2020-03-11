num = list(input("Please enter random four-digit integer number: "))

print ("1. Multiply the input numbers")
num_mult = 1;
for i in num:
	num_mult *= int(i)
print(num_mult)

print("2. Reverse the input numbers")
num.reverse()
print(num)

print ("3. Random sort of numbers")
num.sort()
print(num)
