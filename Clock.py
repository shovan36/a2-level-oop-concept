class Clock:
    #the constructor
    def __init__(self,second,minute,hour,day,month,year):
        self.__second=int(second)
        self.__hour=int(hour)
        self.__minute=int(minute)
        self.__day=int(day)
        self.__month=int(month)
        self.__year=int(year)
    def gethour(self):
        return self.__hour
    def getmin(self):
        return self.__minute
    def getsec(self):
        return self.__second
    def getday(self):
        return self.__day
    def getmonth(self):
        return self.__month
    def getyear(self):
        return self.__year
    def showtime(self):
        return self.__second,self.__minute,self.__hour
    def showdate(self):
        return self.__day,self.__month,self.__year
 
 
 
 
def main():
 
    hour,minute,second,day,month,year=input("enter hour, minute ,second,day,month,year for clock 1").split()
    clock1=Clock(second,minute,hour,day,month,year)
    second,minute,hour = clock1.showtime()
    print(f"the time in clock 1  is {hour:02}:{minute:02}:{second:02}")
    day,month,year =clock1.showdate()
    print(f"the date clock 1 is {day:02}-{month:02}-{year:04}")
    hour,minute,second,day,month,year=input("enter hour, minute ,second,day,month,year for clock 2").split()
    clock2=Clock(second,minute,hour,day,month,year)
    second,minute,hour = clock2.showtime()
    print(f"the time in clock 2 is {hour:02}:{minute:02}:{second:02}")
    day,month,year =clock2.showdate()
    print(f"the date clock 2 is {day:02}-{month:02}-{year:04}")
 
 
 
 
 
if __name__=="__main__":
    main()