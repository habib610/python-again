class Car:
    name = ""  # this are called daa attribute
    color = ""  # this are called daa attribute

    # when we write function in a class or object its called method
    def start():  # This one is called method
        print("starting car", Car.name)


Car.name = "Toyota"
Car.color = "Blue"

print(Car.name)
print(Car.color)
Car.start()
