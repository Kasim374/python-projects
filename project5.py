class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, department):
        super().__init__(emp_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, emp_id, name, age, salary, programming_language):
        super().__init__(emp_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")

employee = None
manager = None
developer = None

while True:
    print("\n============================================================================")
    print("~~~~~~~~~~~~~~~~  EMPLOYEE MANAGEMENT SYSTEM ~~~~~~~~~~~~~~~~~")
    print("============================================================================")
    print("1. CREATE AN EMPLOYEE")
    print("2. CREATE A MANAGER")
    print("3. CREATE A DEVELOPER")
    print("4. CHECK CLASS")
    print("5. SHOW DETAILS")
    print("6. EXIT")

    choice = int(input("Enter your choice (1–6): "))

    if choice == 1:
        employee = Employee(
            input("Enter Employee ID: "),
            input("Enter Employee Name: "),
            int(input("Enter Employee Age: ")),
            float(input("Enter Employee Salary: "))
        )
        print("Employee created successfully!")

    elif choice == 2:
        manager = Manager(
            input("Enter Manager ID: "),
            input("Enter Manager Name: "),
            int(input("Enter Manager Age: ")),
            float(input("Enter Manager Salary: ")),
            input("Enter Manager Department: ")
        )
        print("Manager created successfully!")

    elif choice == 3:
        developer = Developer(
            input("Enter Developer ID: "),
            input("Enter Developer Name: "),
            int(input("Enter Developer Age: ")),
            float(input("Enter Developer Salary: ")),
            input("Enter Programming Language: ")
        )
        print("Developer created successfully!")

    elif choice == 4:
        print("Class Checking:")
        if manager:
            print("Manager is Employee:", isinstance(manager, Employee))
        if developer:
            print("Developer is Manager:", isinstance(developer, Manager))
        if employee:
            print("Employee is Developer:", isinstance(employee, Developer))

    elif choice == 5:
        if employee:
            print("\nEmployee Details:")
            employee.display()
        if manager:
            print("\nManager Details:")
            manager.display()
        if developer:
            print("\nDeveloper Details:")
            developer.display()

        if not any([employee, manager, developer]):
            print("No records found!")

    elif choice == 6:
        print("Exiting the Employee Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
