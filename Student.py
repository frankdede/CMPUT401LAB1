class Student:
    courseMarks={}
    name=""
    def __init__(self,name):
        self.name = name
    def addCourseMark(self,course,mark):
        self.courseMarks[course] = mark
        
        print(" %s added " % course )
    def average(self):
        sum = 0
        for i in self.courseMarks.keys():
            sum += self.courseMarks[i]
        print(" %s 's average is : %d " %(self.name,sum/len(self.courseMarks)))


def main():
    newStudent = Student("jack")
    newStudent.addCourseMark("English",90)
    newStudent.addCourseMark("Math",80)
    newStudent.average()
    
main()
