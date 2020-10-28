import math
class Car:
    def __init__(self,carBrand,mps,carAcceleration):
        self.__carBrand= carBrand
        self.__mps= mps
        self.__carAcceleration= carAcceleration
    def getcarBrand(self):
        return self.__carBrand
    def getcarMps(self):
        return self.__mps
    def getcarAcceleration(self):
        return self.__carAcceleration




class Race:
    def __init__(self,raceLocation,raceDistance,racePrize):
        self.__raceLocation = raceLocation
        self.__raceDistance = raceDistance
        self.__racePrize = racePrize   
        self.__registeredCars = []
    
    def getLocation(self):
        return self.__raceLocation

    def getDistance(self):
        return self.__raceDistance
    def getPrize(self):
        return self.__racePrize 

    def raceWinner(self):
        distance = int(self.getDistance())
        least_time = float('inf')
        least_time_car_brand = "none"
        for car in self.__registeredCars:
            t= math.sqrt(2*distance/car.getcarAcceleration())
            if(least_time > t):
                least_time = t
                least_time_car_brand = car.getcarBrand()
        print (f"the winner is {least_time_car_brand} with the time of {least_time}")        
        
    def addCar(self,car):
        self.__registeredCars.append(car)
            

def main():
    race = Race("nepal",500,10000)
    bmw = Car("bmw",27.7,4)
    race.addCar(bmw)
    tesla = Car("tesla",19.4,3)
    race.addCar(tesla)
    duster = Car("renault",16.6,1.5)
    race.addCar(duster)
    race.raceWinner()
    
    
if __name__=="__main__":
    main()
