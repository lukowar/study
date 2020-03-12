class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    Adam = Man()
    Eva = Woman()
    return [Adam,Eva]

paradise = God()
print (isinstance(paradise[0], Woman))
print (isinstance(paradise[0], Man))
print (isinstance(paradise[1], Woman))
print (isinstance(paradise[1], Man))
