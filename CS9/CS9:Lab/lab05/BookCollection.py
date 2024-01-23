from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count
    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData().__gt__(book):
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = BookCollectionNode(book)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self, author):
        str = ""
        temp = self.head #always start in the beginning
        while temp != None:
            if temp.getData().getAuthor().upper() == author.upper():
                str = str + temp.getData().getBookDetails() + "\n"
                temp = temp.getNext()
            else:
                temp = temp.getNext()
        return str
        
    def getAllBooksInCollection(self):
        str = ""
        temp = self.head
        while temp != None:
            str = str + temp.getData().getBookDetails() + "\n"
            temp = temp.getNext()
        return str
    def removeAuthor(self, author):
        current = self.head
        if current == None:
            return
        previous = None
        found = False
        while not found:
            if current == None:
                return 
            if current.getData().getAuthor().upper() == author.upper():
                found = True
            else:
                previous = current
                current = current.getNext()
        
        next = current.getNext()
        found2 = False
        while not found2:
            if next == None:
                break
            if next.getData().getAuthor().upper() != author.upper():
                found2 = True
            else:
                current = current.getNext()    
                next = current.getNext()        
        if (next == None) and (previous == None):
            #print("case 1")
            self.head = None
        elif previous == None:
            #print("case 2")
            self.head = next
        elif next == None:
            #print("case 3")
            previous.setNext(None)
        else:
            #print("case 4")
            previous.setNext(next)
    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        if title.upper() == bookNode.getData().getTitle().upper():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())


'''ll = BookCollection()
book1 = Book("Title", "Bowie", 2000)
book2 = Book("Title1", "Bowie", 2012)
book3 = Book("Title1", "Stacey", 2005)
book4 = Book("Title1", "Stacey", 2009)
book5 = Book("Title1", "Bowie", 2006)
ll.insertBook(book1)
ll.insertBook(book2)
ll.insertBook(book3)
ll.insertBook(book4)
ll.insertBook(book5)
print(ll.getAllBooksInCollection())
print(ll.getNumberOfBooks())
print(ll.getBooksByAuthor("Bowie"))
ll.removeAuthor("Bowie")
print("Result: ")
print(ll.getAllBooksInCollection())'''

        
    

