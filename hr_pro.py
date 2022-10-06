
class Employee:
    def __init__(self, name, age, salary, employment_years):
        self.name= name
        self.age= age
        self.salary= salary 
        self.employment_years= employment_years

    def __str__(self):
        annual_salary= self.salary*12
        return (f"Name: {self.name}, Age: {self.age}, Salary: {annual_salary}, Working Years: {self.employment_years},")


    def get_annual_salary(self,):
        annualsalary=self.salary*12
        return annualsalary

    

def list_employee ():
    listemployee=[]
    employee_one=Employee("dalal", 19, 100, 2)
    employee_two=Employee("sara", 18, 90, 1)
    employee_three=Employee("moodi", 21, 120, 4)
    employee_four=Employee("haya", 27, 300, 6)
    employee_five=Employee("nouf", 30, 120, 2)
    listemployee.append(employee_five,employee_four,employee_three,employee_two, employee_one)
    return listemployee



class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)    #Manager class here
        self.bonus_percentage= bonus_percentage

    def get_bonus(self):
        return self.salary * self.bonus_percentage
    
    def __str__(self) -> str:
        bonus=self.get_bonus()
        print (f"{super().__str__()} bonus {bonus}")

def list_ofmanagers ():
    listofmangers=[]
    manager_one= Manager("ahmed", 40, 500, 10, 0.8)
    manager_two=Manager("laila", 20, 400, 3, 0.9)
    listofmangers.append(manager_one)
    listofmangers.append(manager_two)
    return (listofmangers)








def main():
    
        options=["Show Employees","Show Managers","Add An Employee","Add A Manager"
	    "Exit"]
        listofmanagers= []
        listofemployee= []

        print ("Welcome to HR Pro")
        print ("options")

        index=1
        for option in options:
            print (index, option)
            index= index+1

        choose= int(input("What would you like to do?"))
        print (choose)

        print ("---------------------------------")
        if choose== 1:
            return(list_employee)
             
            
        elif choose==2:
            return (list_ofmanagers)
            
        elif choose==3:
            name= input("whats the employees name?")
            age= input("whats the employees age?")
            salary= input(" whats the salary?")
            employment_years= input("how many years of employment?")
            employee_add= Employee(name, age, salary, employment_years)
            listofemployee.append(employee_add)
            return (employee_add)
            
        elif choose==4:
            name= input("whats the manager name?")
            age= input("whats the manager age?")
            salary= input(" whats the manager salary?")
            employment_years= input("how many years of managment?")
            bonus_percentage= input("bonus percentage?")
            manager_add= Manager(name, age, salary, employment_years, bonus_percentage)
            listofmanagers.append(manager_add)
            return (manager_add)
        
        else:
            return ("programme off")  


print (main())
