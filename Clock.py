
class parking():
    def __init__(self,space,rate):
        self.__space=space
        self.__rate=rate
    def getspace(self):
        return self.__space    
    def getrate(self):
        return self.__rate
            
def main():
    j=0
    p="p"
    rate= 0
    while p != "q":
        print(f"the total number of vechile in parking is {j} and the total fee collected is RS.{rate}")
        a=str(input("enter 'i' if vechile entering parking or 'o' if veching exiting parking"))
        if j==0 and a=="o":

            print("parking is empty already")
        elif j==20 and a=="i":
            print ("parking is full already")
        elif a == "i" and j < 20:
            j=j+1
            rate=rate+10
        elif a == "o" and j >0:
            j=j-1
        p = str(input("enter 'q' if u want to quit the program"))    

   




if __name__ == "__main__":
    main()
 

       