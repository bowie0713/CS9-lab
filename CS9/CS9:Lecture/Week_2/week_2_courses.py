from Week_2_class import Student

class Courses:
    '''Class representing a collection of courses organized by a dictionary where
    the key is the course number and hte corresponding value 
    is a list of Students in a course'''
    def __init__(self):
        self.courses = {}
    def addStudent(self, student, courseNum):
        '''Method that adds a student object to a courseNum {str}'''
        # if the course doesn't exist
        if self.courses.get(courseNum) == None:
            self.courses[courseNum] = [student]
        elif not student in self.courses.get(courseNum):
            self.courses[courseNum].append(student)
    def printCourses(self):
        for courseNum in self.courses:
            print("courseNum: ", courseNum)
            for student in self.courses[courseNum]:
                student.printAttributes()
            print("---")
a1 = Student("Jane", 1234567)
a2 = Student("Joe", 7654321)
a3 = Student("Jill", 5555555)

UCSB = Courses()
UCSB.addStudent(a1, "CS8")
UCSB.addStudent(a2, "CS9")
UCSB.addStudent(a2, "CS16")
UCSB.printCourses()



