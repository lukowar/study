def reverse(self):
    return (' '.join(self.split()[-1::-1]))
print (reverse ("Hello World"))

phrase = input ("Write a two word phrase: ")
print (reverse(phrase))
