class Employe:
    def __init__(self, name, income):
        self.name = name #public
        self._department = None #protected
        self.__income = income #private
        
    @property #Getter
    def income(self):
        return self.__income

    @income.setter #Setter
    def income(self, new_income):
        if new_income > 0:
            self.__income = new_income
        else: 
            print("El salario debe ser positivo")
            
    def _assign_department(self, department):
        self.department = department
        
    def _bonus_calculate(self):
        return self.__income * 0.1
    
#Main
employe = Employe("Robert", 200)
print(employe.name) #access to a public attribute
employe.income = 550 #using setter
print(employe.income) #using getter
employe._assign_department("Sales") #using a protected method
print(employe._Employe__income) #using a private attribute
#employe._bonus_calculate()