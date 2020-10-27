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
    
    # The player meets another player and adds their location to itself
    def meetAnotherPlayer(self,Player2):
        self.__x = self.__x + Player2.getX()
        self.__y = self.__y + Player2.getY()
        

def main():
    player1 = Player(0,0)
    x = int(input())
    y = int(input())
    player1.move(x,y)
    x, y = player1.showLocation()
    print("the location of player is ", x,y)
    player2 = Player(10,10)
    player1.meetAnotherPlayer(player2)
    x, y = player1.showLocation()
    print("the location of player is ", x,y)
    


if __name__=="__main__":
    main()