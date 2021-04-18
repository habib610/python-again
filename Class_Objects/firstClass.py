class Car:
    name = ""  # this are called daa attribute
    color = ""  # this are called daa attribute

    # when we write function in a class or object its called method
    def start(self):  # This one is called method
        print("starting car", Car.name)


Car.name = "Toyota"
Car.color = "Blue"

print(Car.name)
print(Car.color)
# Car.start()

# Here we will  create objects or instances of Class Car
print("Car class objects or instances are here>>>>>>>>>>>>>")
my_car = Car()
my_car.name = "Marcidies"
my_car.color = "Brown"

print(my_car.name)
print(my_car.color)
my_car.start()