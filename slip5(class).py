#slipno5
#creat class print data
class employee:
    def getdata(self):
        self.name=input("Enter Name:")
        self.department=input("Enter Department:")
        self.salary=int(input("Enter Salary:"))

    def putdata(self):
        print("\nEmployee Details:")
        print("Employee Name:",self.name)
        print("Employee Department:",self.department)
        print("Employee Salary:",self.salary)

emp=employee()
emp.getdata()
emp.putdata()
