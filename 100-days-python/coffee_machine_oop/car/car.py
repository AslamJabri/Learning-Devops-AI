class Car:
    def __init__(self,brand,model,is_electric):
        self.brand = brand
        self.model = model
        self.fuel_level = 100
        self.is_electric = is_electric
        self.battery = 100
        
    def drive(self, distance):      
        fuel_needed = distance / 5
        battery_needed = fuel_needed + 2  # Your custom electric consumption math
        
        if self.is_electric:
            if self.battery >= battery_needed:
                print(f"🔋 Starting Battery: {self.battery}%")
                self.battery -= battery_needed
                return f"Battery after the journey: {self.battery}%"
            else:
                return "❌ Sorry, not enough battery charge for this trip!"
        else:
            # Check if we have enough fuel BEFORE we start driving
            if self.fuel_level < fuel_needed:
                return f"❌ Sorry, no fuel left or not enough for this distance! Current fuel: {self.fuel_level}%"
            else:
                print(f"⛽ Starting Fuel: {self.fuel_level}%")
                self.fuel_level -= fuel_needed
                return f"Fuel after the journey: {self.fuel_level}%"
        
        
            
        
        
        
        
        