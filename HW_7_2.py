def list_animals(animals):
    list = str()
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + "\n"
    return list

animals = ["dog", "cat", "elephant"]
print (list_animals(animals))

animals_big = ["dog", "cat", "elephant", "mouse", "rat", "bat"]
print (list_animals(animals_big))
