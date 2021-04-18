class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("Starting the class", '"', self.name,'"')


my_car = Car("Lamborghini", "Red")
print(my_car.name)
print(my_car.color)
my_car.start()

my_car1 = Car("Marcidies", "Black")
print(my_car1.name)
print(my_car1.color)
my_car1.start()

my_car2 = Car("Corolla", "White")
print(my_car2.name)
print(my_car2.color)
my_car2.start()