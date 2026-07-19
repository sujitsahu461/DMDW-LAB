#Write a program to create a class for Employee having member data: Emp ID, Name, Basic Pay, TA, DA, Gross Pay and member functions display(), calc(). calc() finds Gross Pay = Basic Pay + 10% of TA + 40% of DA. display() displays the information.

class Employee:
    def __init__(self):
        self.emp_id = int(input("Enter the ID: "))
        self.emp_name = input("Enter the Name: ")
        self.basic_pay = int(input("Enter the Basic Pay: "))
        self.ta = int(input("Enter the TA: "))
        self.da = int(input("Enter the DA: "))
    def calc(self):
        self.gross_pay = self.basic_pay + (0.10 * self.ta) + (0.40 * self.da)
    def display(self):
        print("Employee Details")
        print("Emp ID:", self.emp_id)
        print("Emp Name:", self.emp_name)
        print("Basic Pay:", self.basic_pay)
        print("TA:", self.ta)
        print("DA:", self.da)
        print("Gross Pay:", self.gross_pay)
e = Employee()
e.calc()
e.display()