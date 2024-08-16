class Car:
    total_car =0;

    def __init__(self , brand, model):
        self.__brand = brand
        self.model = model        
        Car.total_car +=1

    def get_brand(self):
        return self.__brand + " !"    

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_des():
        return "Cars means of transport"
    
    
    # Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,bettry_size):
        super().__init__(brand, model)
        self.bettry_size = bettry_size

        
    def fuel_type(self):
        return "Electric charge"    


my_tesla = ElectricCar("Tesla", "Model S5", "85kWH") 
# print(my_tesla.__brand)
# print(my_tesla.get_brand())

# print(my_tesla.fuel_type())
# safari = Car("tata", "safari")
# safari = Car("tata", "Nexon")
# print(safari.fuel_type())
# print(Car.total_car)

# my_car = Car("TATA", "SAFARAI")
# my_car.model = "City"
# Car("TATa", "NEXON")
# print(my_car.general_des())
# print(my_car.model)


# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.bettry_size)



# my_car = Car("toyota", "fortunar", "1500")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectrinCarTwo(Battery,Engine, Car):
    pass

my_new_Tesla = ElectrinCarTwo("tata", "sss")
print(my_new_Tesla.engine_info())
print(my_new_Tesla.battery_info())