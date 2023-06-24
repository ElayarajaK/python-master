'''
 default arguments
'''

def printData(para1,para2,name="raja"):
    add = para1+para2,name;
    return add;
print(printData(100,200,"java"))


def method1(lang="Eng",address="TamilNadu",name):
    print("My name : ",name ,"i am from : ",address,"and my lan is : ",lang)

method1("Raja");
method1("Vicky");
method1("Jhonson","Tamil","Nellagiri")