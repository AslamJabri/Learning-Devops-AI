from car import Car
from garage import Garage

tesla_m3    = Car(brand="Tesla", model="Model 3", is_electric=True)
porsche_ty  = Car(brand="Porsche", model="Taycan", is_electric=True)
byd_seal    = Car(brand="BYD", model="Seal", is_electric=True)
hyundai_i5  = Car(brand="Hyundai", model="Ioniq 5", is_electric=True)

toyota_sup  = Car(brand="Toyota", model="Supra", is_electric=False)
bmw_m3      = Car(brand="BMW", model="M3 Competition", is_electric=False)
ford_mus    = Car(brand="Ford", model="Mustang Dark Horse", is_electric=False)
honda_civ   = Car(brand="Honda", model="Civic Type R", is_electric=False)




my_garage = Garage()
print(tesla_m3.drive(10))

my_garage.add_car(bmw_m3)
my_garage.add_car(hyundai_i5)

print(my_garage.name)
(my_garage.inventory())