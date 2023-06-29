

id = input("Enter the id")
def result(m1,m2,m3):
    if m1>40 and m2 >40 and m3 >40:
        return "Pass"
    return "fail"
 
class Student:
    def __init__(self,s_id,name,marks1,m2,m3,address):
        self.id=s_id;
        self.name=name;
        self.marks=marks1;
        self.add = address;
        self.sum = m1+m2+m3;
        self.result=resulet(m1,m2,m3)
    def printData(self):
        print(self.id,", ",self.name,", ",self.marks,", ",self.add)        
        


student1 = Student(id,"Raja",100,100,100,"Chennai");
#print(student1.id,", ",student1.name,", ",student1.marks,", ",student1.add)
student2 = Student(20211,"Vickram",88,"Truchi");
#print(student2.id,", ",student2.name,", ",student2.marks,", ",student2.add)
student3 = Student(20311,"Sham",45,"Madhurai");
#print(student3.id,", ",student3.name,", ",student3.marks,", ",student3.add)
student4 = Student(20411,"abu",67,"Chennai");

#print(student4.id,", ",student4.name,", ",student4.marks,", ",student4.add)
student5 = Student(20511,"Arjun",77,"Chennai");
print("Done")
student1.printData();
student2.printData();
student3.printData();
student4.printData();
student5.printData();