from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def test_getBookDetails():
    a = Book("Ready Player One", "Cline, Ernest", 2011)
    b = Book("Cinderella", "NA", 1000)
    assert a.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"
    assert b.getBookDetails() == "Title: Cinderella, Author: NA, Year: 1000"
    assert a.getAuthor() == "Cline, Ernest"
    assert b.getAuthor() == "NA"
    assert a.getTitle() == "Ready Player One"
    assert b.getTitle() == "Cinderella"
    assert a.getYear() == 2011
    assert b.getYear() == 1000
def test_gtfunction(): 
    a = Book("Bowie", "Chuang", 12)
    b = Book("Stacey", "Chuang", 9)
    c = Book("Bowie", "Chuang", 15)
    d = Book("Bowie", "Lin", 15)
    assert a.__gt__(b) == True
    assert b.__gt__(a) == False
    assert c.__gt__(d) == False
    assert b.__gt__(c) == False
def test_BookCollection():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    b4 = Book("Cujo", "King", 2020)

    bc = BookCollection()
    assert bc.isEmpty() == True
    bc.insertBook(b0)
    assert bc.isEmpty() == False
    assert bc.getNumberOfBooks() == 1
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getNumberOfBooks() == 4
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\nTitle: Rage, Author: King, Stephen, Year: 1977\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    bc.removeAuthor("Cline, Ernest")
    assert bc.getNumberOfBooks() == 3
    bc.insertBook(b4)
    #print(bc.getBooksByAuthor("King, Stephen"))
    assert bc.getBooksByAuthor("King, Stephen") == "Title: Rage, Author: King, Stephen, Year: 1977\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.recursiveSearchTitle("Cujo", bc.head) == True
    assert bc.recursiveSearchTitle("Bowie", bc.head) == False
#test_BookCollection()