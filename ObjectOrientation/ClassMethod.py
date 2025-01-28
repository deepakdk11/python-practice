class Student:
    college = "HICAS"

    def getInfo(self):
        print("College Name is:", Student.college)


    @classmethod
    def changeName(cls, newName):
        cls.college = newName


s1 = Student()
s1.getInfo()
Student.changeName("Code")
s1.getInfo()        