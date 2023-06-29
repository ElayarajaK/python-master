class Besant:
    def __init__(self,no,name,designation,salary):
        self.e_no = no;
        self.e_name=name
        self.e_des=designation
        self.e_salary=salary;

    def printData(self):
        print(self.e_no,", ",self.e_name,", ",self.e_des,", ",self.e_salary,", ");


Emp1 = Besant(20111,"Apj","Developer",100000)

Emp2 = Besant(3011,"Raja","Testing",50000)

Emp3 = Besant(300,"Ganeh","SME",75000)
'''
print(Emp1.e_no,", ",Emp1.e_name,", ",Emp1.e_des,", ",Emp1.e_salary,", ",)        
print(Emp2.e_no,", ",Emp2.e_name,", ",Emp2.e_des,", ",Emp2.e_salary,", ",)        
print(Emp3.e_no,", ",Emp3.e_name,", ",Emp3.e_des,", ",Emp3.e_salary,", ",)        
'''

Emp1.printData()
Emp2.printData()
Emp3.printData()
