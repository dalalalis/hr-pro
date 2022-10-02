from curses import ACS_GEQUAL
from unicodedata import name


class Employee:
   def __init__(self, name, age, salary, employment_years):
    self.name= name
    self.age= age
    self.salary= salary 
    self.employment_years= employment_years

    def get_annual_salary(self, salary):
        annualsalary=self.salary*12
        return (annualsalary)

    def __strg__(self):
     print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years},")


class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)    #Manager class here
        self.bonus_percentage= bonus_percentage

    def get_bonus(self, salary, bonus_percentage):
        return (salary* bonus_percentage)
    
    def __str__(self) -> str:
        bonus= self.get_bonus
        print (f"{super().__str__()} bonus {bonus}")











def main():
	# main code here

if __name__ == '__main__':
	main()
