class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price
    def __gt__(self, rhs):
        if self.make > rhs.make.upper():
            return True
        elif self.make == rhs.make.upper():
            if self.model > rhs.model.upper():
                return True
            elif self.model == rhs.model.upper():
                if self.year > rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
        return False
    def __lt__(self, rhs):
        if self.make < rhs.make.upper():
            return True
        elif self.make == rhs.make.upper():
            if self.model < rhs.model.upper():
                return True
            elif self.model == rhs.model.upper():
                if self.year < rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
        return False
    def __eq__(self, rhs):
        if rhs is None:
            return False
        if (self.make == rhs.make.upper()) and (self.model == rhs.model.upper()) and (self.year == rhs.year) and (self.price == rhs.price):
            return True
    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make, self.model, self.year, self.price)

car3 = Car("Mercedes", "Sprinter", 2021, 40000)
car4 = Car("Mercedes", "Sprinter", 2022, 40000)


    