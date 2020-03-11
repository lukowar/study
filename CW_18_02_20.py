#Task 1

#cmd: pip install pyowm
import pyowm
city=input("What city you are interested: ")
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')    # You MUST provide a valid API key
# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# Search for current weather in the city

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
print("In this city "+ w.get_detailed_status())

#Task 2

import random
from random import randint
num_rand = randint (1, 100)
print (num_rand)
num_user = int(input ("Please input any integer number in range from 1 to 100 "))
if num_user <= 0 or num_user > 100:
    print ("You have input a wrong number, please try again")
while num_user != num_rand:
    if num_user < num_rand:
        print ("Your number is smaller")
        num_user = int(input ("Please input any integer number in range from 1 to 100 "))
    elif num_user > num_rand:
        print ("Your number is bigger")
        num_user = int(input ("Please input any integer number in range from 1 to 100 "))
else:
    print ("You've chosen the right number")

#Task 3

