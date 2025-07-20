class Person:
    # Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    # Method to display a greeting
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. My employee ID is {self.employee_id}."

#person = Person("John Doe", 30)
employee = Employee("Jane Doe", 25, "12345")

#print(person.greet())
print(employee.greet())