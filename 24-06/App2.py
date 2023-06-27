'''
    1.static variable and static method(Globalize variable)
    2.instance variable and instance method(Object variable)
    3.local variable and local method

'''
class Student:
    s_id =20111;##static variable 

std1 = Student();## Object creation  std1--> Object ref
std2=Student();#Object creation   std2-->Object ref
print(Student.s_id)
Student.s_id=40011;
print(std1.s_id)
print(std2.s_id)
print("==========")
std1.s_id=77744;
print(std1.s_id)
print(std2.s_id)
