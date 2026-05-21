class Garage:
    def __init__(self):
        self.name = "AJ Garage"
        self.car_list = []
        
    def add_car(self,car):
        self.car_list.append(car)
        print(f"Added {car.brand} to {self.name}")
        
    def inventory(self):
        count = 0
        for car in self.car_list:
            count +=1
            print(f"🚗 Car #{count}: {car.brand} {car.model} (Fuel/Battery: {car.fuel_level if not car.is_electric else car.battery}%)")
        print(f"We have {count} cars in {self.name} ")

