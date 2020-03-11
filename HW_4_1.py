def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        return True
    else:
        return False

dist = int(input("Please input the distance (in miles) to the gas station: "))
fuel = int(input("Please input the fuel volume left in the tank: "))
mpg = int(input("Please input average fuel consumption of your car in mpg: "))
print(zero_fuel(dist, mpg, fuel))
