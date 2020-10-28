from tabulate import tabulate
class Book():
    def __init__(self,bookId,bookName,bookAuthor,bookCategory):
        self.__bookId = bookId
        self.__bookName = bookName
        self.__bookAuthor = bookAuthor
        self.__bookCategory = bookCategory

    def getBookId(self):
        return self.__bookId

    def getBookName(self):
        return self.__bookName

    def getBookAuthor(self):
        return self.__bookAuthor

    def getBookCategory(self):
        return self.__bookCategory


class Library():
    def __init__(self,library_name):
        self.__file_name = library_name
        self.__catalog = []

    def addBook(self,book):
        bk=open(self.__file_name,'a')
        name=book.getBookName()
        id = book.getBookId()
        author = book.getBookAuthor()
        category = book.getBookCategory()
        t = name +',' + str(id) + ',' + author + ',' + category + '\n'
        self.__catalog.append(t)
        bk.write(t)
        bk.close()
    
    def showAllBooks(self):
        content = []
        with open(self.__file_name,'r') as f:
            content = f.readlines()
        content = [x.strip() for x in content] 
        for book in content:
            b = book.split(",")
            message = [
                ["Book ID" , b[1]], 
                ["Book Name" , b[0]],
                ["Book Author" ,b[2]],
                ["Book Category", b[3] ],
                ["Mesage" , "Enjoy the book"],
            ]
            print(tabulate(message))

def main():
    book_name = str(input("enter books name :"))
    book_id = str(input("enter book's ID :"))
    book_author = str(input("enter book's author :"))
    book_cateogry = str(input("enter book's category :"))
    b1 = Book(book_id,book_name,book_author,book_cateogry)
    lib = Library("book.txt")
    lib.addBook(b1)
    lib.showAllBooks()    
  
if __name__=="__main__":
    main()