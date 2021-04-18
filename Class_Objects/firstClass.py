class Car:
    name = "Lambogrhini"  # this are called daa attribute
    color = "red"  # this are called daa attribute

    # when we write function in a class or object its called method
    def start():  # This one is called method
        print("starting car", Car.name)


print(Car.name)
print(Car.color)
Car.start()
