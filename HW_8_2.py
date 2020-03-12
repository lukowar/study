def sorter(textbooks):
    return sorted(textbooks,key=str.lower)

print (sorter(['Algebra', 'History', 'Geometry', 'English']), ['Algebra', 'English', 'Geometry', 'History'])
print (sorter(['Algebra', 'history', 'Geometry', 'english']), ['Algebra', 'english', 'Geometry', 'history'])
print (sorter(['Alg#bra', '$istory', 'Geom^try', '**english']), ['$istory', '**english', 'Alg#bra', 'Geom^try'])
