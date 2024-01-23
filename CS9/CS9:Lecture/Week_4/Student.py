from Quiz_test2 import Person

class Student(Person):
  def __init__(self, name, weight, perm):
     super().__init__(name, weight)
     self.perm = perm
  def getInfo(self):
     s = ", PERM: "
     s  = super().getInfo() + s
     s = s + "{}".format(self.perm)
     return s
  def __ge__(self, rhs):
     return self.perm >= rhs.perm
  

s1 = Student("Peter Parker", 167, 1234567)
s2 = Student("Flash Thompson", 160, 7654321)

print(s1 >= s2 == False)

