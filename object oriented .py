class Player:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def move(self,x,y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def showLocation(self):
        return self.__x, self.__y
    

def main():
    player1 = Player(0,0)
    x = int(input("ENTER COORDINATES"))
    y = int(input())
    player1.move(x,y)
    x, y = player1.showLocation()
    print("the location of player 1 is ", x,y)
    player2 = Player(10,10)
    x = int(input("ENTER LOCATION"))
    y = int(input())
    player2.move(x,y)
    x, y = player2.showLocation()
    print("the location of player 1 is ", x,y)
    
    x, y = player2.showLocation()
    print("the location of player 2 is ", x,y)
    


if __name__=="__main__":
    main()