
def bonus(salary, rate=0.1, *extras, **options):  
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])
    return result  
print("Bonus:", bonus(30000))
print("Bonus with extras:", bonus(30000, 0.1, 500, 1000))
print("Bonus with cap:", bonus(30000, 0.1, 500, cap=2000))

class InvalidSalaryError(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f" Name: {self.name}, Salary:{self.salary}, Team Size: {self.team_size}"

emp = Employee("Arun", 30000)
print(emp.get_details())
print("Annual Salary:", emp.annual_salary())

mgr = Manager("Priya", 60000, 5)
print(mgr.get_details())


try:
    emp = Employee("Arun", -500)

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")

employees = [ 
    {"name" :"Arun", "salary":30000, "city": "Chennai"},
    {"name" :"Priya", "salary":45000, "city": "Chennai"},
    {"name" :"Rahul", "salary":60000, "city": "Bangalore"},
    {"name" :"Divya", "salary":75000, "city": "Chennai"},
    {"name" :"Karthik", "salary":90000, "city": "Mumbai"},
    {"name" :"Meena", "salary":52000, "city": "Bangalore"},
    {"name" :"Suresh", "salary":68000, "city": "Chennai"},
    {"name" :"Anitha", "salary":48000, "city": "Mumbai"},
]

above_50000 = [emp["name"]for emp in employees if emp["salary"]> 50000]
print("Above 50000:", above_50000)    

raised_salaries = list(map(lambda emp: emp["salary"]* 1.1, employees))

chennai_employees = list(filter(lambda emp: emp["city"] == "Chennai", employees))
print("Chennai:", [emp["name"]for emp in chennai_employees])

for emp in employees:
    salary = emp["salary"]

    if salary == 0:
        continue
    if salary> 85000:
        break
    print(emp["name"],salary)