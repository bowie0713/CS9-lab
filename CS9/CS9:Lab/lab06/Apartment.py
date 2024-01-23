class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition
    def getRent(self):
        return self.rent
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    def getCondition(self):
        return self.condition
    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.rent, self.metersFromUCSB, self.condition)
    def __lt__(self, other):
        if self.rent < other.rent:
            return True
        elif self.rent > other.rent:
            return False
        elif self.rent == other.rent:
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif self.metersFromUCSB > other.metersFromUCSB:
                return False
            elif self.metersFromUCSB == other.metersFromUCSB:
                if other.condition == 'excellent' and self.condition == 'excellent':
                    return True
                elif other.condition == 'average' and self.condition == 'excellent':
                    return True
                elif other.condition == 'bad' and self.condition == 'excellent':
                    return True
                elif other.condition == 'average' and self.condition == 'average':
                    return True
                elif other.condition == 'bad' and self.condition == 'average':
                    return True
                else:
                    return False
    def __eq__(self, other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == other.condition:
                    return True
        return False
    def __gt__(self, other):
        if self == other:
            return False
        else:
            return not (self<other)



    
