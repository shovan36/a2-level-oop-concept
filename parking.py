from tabulate import tabulate

class Parking():
    def __init__(self,maxParkingLimit,parkingCharge):
        self.__maxParkingLimit = maxParkingLimit
        self.__currentParking = 0
        self.__totalAmount = 0
        self.__parkingCharge = parkingCharge

    def getVacantSpace(self):
        return self.__maxParkingLimit - self.__currentParking    
    
    def getTotalEarned(self):
        return self.__totalAmount
    
    def addVehicle(self):
         self.__currentParking += 1
         self.__totalAmount += self.__parkingCharge
    
    def exitVehicle(self):
        self.__currentParking -= 1
    
    def manageParking(self,command):
        if(command == "i" and self.__currentParking < self.__maxParkingLimit):
            self.addVehicle()
        elif(command == "o" and self.__currentParking > 0 ):
            self.exitVehicle()
        elif(command == "i" and self.__currentParking == self.__maxParkingLimit):
            print("Parking is full")
        elif(command == "o" and  self.__currentParking == 0):
            print("Parking is vacant")
        else:
            print("Parking Class not found")

    def showParkingStatus(self):
        message = [
            ["Total Space" , self.__maxParkingLimit], 
            ["Total Occupied" , self.__currentParking ],
            ["Total Vacant" , self.__maxParkingLimit - self.__currentParking ],
            ["Total Earned" , self.__totalAmount ],
            ["Mesage" , "Thank you for parking"],
        ]
        print(tabulate(message))
 


def main():
    parking = Parking(20,10)
    while(True):
        a = str(input("Do you want to enter or exit vehicle? type [i]/[o]? \t"))
        parking.manageParking(a)
        parking.showParkingStatus()
        a = str(input("press q to exit or c to continue? \t"))
        if(a == "q"):
            break
        else:
            continue

if __name__ == "__main__":
    main()
 

   