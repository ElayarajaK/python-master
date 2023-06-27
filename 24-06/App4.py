class Employee:
    def __init__(self):
        print("from no arg constructor")
    def __init__(self,s_id,s_name):
        print("1 arg Constructor  : ",s_id)
        self.s_id = s_id;
        self.s_name=s_name;

emp2 = Employee(100,"Raja")
print(emp2.s_id)
print(emp2.s_name)
emp3 = Employee(200,"Rakesh")
print(emp3.s_id)
print(emp3.s_name)
emp4=Employee(300,"Dineh")
print(emp4.s_id)
print(emp4.s_name)