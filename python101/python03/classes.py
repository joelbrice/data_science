class Car:
    def __init__(self, model="Toyota", year=2020, color="Red", price=50000, engine_started=False):
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.engine_started = engine_started

    def engine(self):
        return f"The engine is {self.model} model"

    def engine_start(self):
        self.engine_started = True
        return f"The engine has started? {self.engine_started} and its engine is {self.model} model"

    def engine_stop(self):
        self.engine_started = False
        return f"The engine has stopped? {not self.engine_started} and its engine is {self.model} model"

    def car_speed(self, speed):
        self.speed = speed
        return f"The car speed is {self.speed} km/h"



ferarri = Car() #Instance of Car class
print(type(ferarri)) #<class '__main__.Car'>
ferarri.engine_started = True

print(ferarri.engine_started) #True

model ="V20"

print(ferarri.engine_start()) #The engine has started? True and its engine is V20 model
print(ferarri.engine_stop()) #The engine has stopped? False and its engine is V20 model
print(ferarri.car_speed(200)) #The car speed is 200 km/h
