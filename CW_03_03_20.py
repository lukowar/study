#Task 1

names = ['Sam', 'Don', 'Daniel'] 
#for i in range(len(names)): 
#    names[i] = hash(names[i]) 
#print(names) 

# => [6306819796133686941, 8135353348168144921, -1228887169324443034]

h_names = map(hash, names)
print(list(h_names))

#Task 2

#colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow" ]
#result = filter ("red", colors)
#print(result)

def redCol (col):
    return col == "red"

colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
result = filter (redCol, colors)
print (list(colors))
print (list(result))

#Task 3

my_list = ['1', '2', '3', '4', '5', '6', '7']
into_int = map(int, my_list)
print(list(into_int))


new_list = []
for i in my_list:
    new_list.append(int(i))
print(new_list)

#Task 4

def mToKm (miles):
    return miles*1.6

miles_list = [1, 2, 60, 4]
km_list = [1.6*n for n in miles_list]
print (list(km_list))

new_km_list = map(lambda n: 1.6*n, miles_list)
print(list(new_km_list))

last_km_list = map(mToKm, miles_list)
print(list(last_km_list))

