class Employee:

    company_name = "code"

    def __init__(self,name,age,designation):
        self.name = name
        self.age = age
        self.designation = designation

    def login(self, time):
        print(f"{self.name} logged in at {time}")

    def work(self, time):
        print(f"{self.name} logged out at {time}")

    def logout(self, hours):
        print(f"{self.name} worked for {hours}")

e1 = Employee("Deepak", 24, "Software Developer")
e2 = Employee("Sandhiya", 21, "HR")
e3 = Employee("Siva", 25, "SAP")

e1.login(5)