import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)

x1, y1, x2, y2 = int(input("Enter 1st point x axis coordinate: ")), int(input("Enter 1st point y axis coordinate: ")), int(input("Enter 2nd point x axis coordinate: ")), int(input("Enter 2nd point y axis coordinate: "))
print(distance(x1, y1, x2, y2))
