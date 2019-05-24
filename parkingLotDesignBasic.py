class Car:
    def __init__(self, owner, plate):
        self.owner = owner
        self.plate = plate


class Floor:
        def __init__(self, name, number_of_spaces):
            self.spaces = []
            self.name = name
            self.number_of_spaces = number_of_spaces
            for i in range(self.number_of_spaces):
                self.spaces.append("")
        
        def add_car_to_space(self, car, space_num):
            if self.spaces[space_num] == "":
                self.spaces[space_num] = car
                return car.owner + " parked " + str(car.plate) + " on " + self.name + " floor at " + str(space_num)
            else:
                car = self.spaces[space_num]
                return car.plate + " already parked on " + self.name + " floor at " + str(self.space_num)
        
        def remove_car(self,space_num):
            self.spaces[space_num] = ""
            
class Garage:

        def __init__(self, name, address, number_of_floors, num_of_spaces_per_floor):
            self.name = name
            self.address = address
            self.number_of_floors = number_of_floors
            self.num_of_spaces_per_floor = num_of_spaces_per_floor
            self.floors = []
            self.initGarage(number_of_floors, num_of_spaces_per_floor)
            
        def initGarage(self, number_of_floors, num_of_spaces_per_floor):
            f = 0
            while f < number_of_floors:
                color = "White"
                if f == 0:
                    color = "Red"
                elif f == 1:
                    color = "Black"
                floor = Floor(color, num_of_spaces_per_floor)
                self.floors.append(floor)
                f = f + 1
                
        def add_car(self,car, floor_num, space_num):
            floor = self.floors[floor_num]
            print("-----------------------")
            msg = floor.add_car_to_space(car, space_num)
            #print(msg)
            return msg
        
        def remove_car(self, plate):
            floor_num = 0
            while floor_num < len(self.floors):
                space_num  = 0
                while space_num < len(self.floors[floor_num].spaces):
                    parking_space_contents = self.floors[floor_num].spaces[space_num]
                    if parking_space_contents == "":
                        space_num = space_num + 1
                    else:
                        if parking_space_contents.plate == plate:
                            self.floors[floor_num].remove_car(space_num)
                            msg = str(parking_space_contents.owner) + " " + str(parking_space_contents.plate) + " Removed "
                            return msg 
                        else:
                            space_num = space_num + 1
                floor_num = floor_num + 1 
            msg = "car not found"
            return msg

print("Welcome to parking lot:")
car1 = Car("Noopur", 1)
car2 = Car("Joey", 2)
car3 = Car("John", 3)    
car4 = Car("Jolly",4)
garage = Garage("A1", "Summit Ave", 2, 10)
print(garage.add_car(car1,1,3))
print(garage.remove_car(1))
    
