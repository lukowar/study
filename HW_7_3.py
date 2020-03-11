def double_char(s):
    line = ""
    for i in s:
       line += i + i
    return line

print (double_char("String"))
print (double_char("Hello World"))
print (double_char("1234!_ "))
