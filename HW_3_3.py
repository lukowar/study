def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {}!".format(name)

name_1 = input ("Please input your name ")
print (greet(name_1))
