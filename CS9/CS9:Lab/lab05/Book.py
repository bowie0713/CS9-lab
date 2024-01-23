class Book:
    def __init__(self, title = "", author = "", year= None):
        self.title = title
        self.author = author
        if year == None:
            self.year = year
        elif type(year) == int:
            self.year = year
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getYear(self):
        return self.year
    def getBookDetails(self):
        return "Title: {}, Author: {}, Year: {}".format(self.title, self.author, self.year)
    def __gt__(self, other):
        if self.author.upper() > other.author.upper():
            return True
        elif self.author.upper() < other.author.upper():
            return False
        elif self.author.upper() == other.author.upper():
            if self.year > other.year:
                return True
            elif self.year < other.year:
                return False
            elif self.year == other.year:
                if self.title.upper() > other.title.upper():
                    return True
                elif self.title.upper() < other.title.upper():
                    return False
                else:
                    return False
a = Book("Bowie", "Chuang", 12)
b = Book("Stacey", "Chuang", 9)
c = Book("Bowie", "Chuang", 15)
d = Book("Bowie", "Lin", 15)
#print(b.__gt__(c))