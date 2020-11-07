import datetime
class LibraryItem:
    def __init__(self,title,author,itemId):
        self.__title=title
        self.__author=author
        self.__itemId=itemId
        
        


    def GetTitle(self):
         return self.__title
    
    def GetAuthor(self):
        return self.__author
    
    def GetItemId(self):
        return self.__itemId
    
    def printDetails(self):
        print(self.__author)

    
            


class Book(LibraryItem):
    def __init__(self,title,author,itemId):
        LibraryItem.__init__(self,title,author,itemId)



class Cd(LibraryItem):
    def __init__(self,title,author,itemId):
        LibraryItem.__init__(self,title,author,itemId)


def main():
    book1 = Book("harry","shovan",12)
    print(book1)
    cd1 = Cd("knight Rider","bla ", 12)
    print(cd1)
  
if __name__=="__main__":
    main()  