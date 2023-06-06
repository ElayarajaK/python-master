'''
    conversion
    string to others

    int() 
    float()
    bool()
    str()
    complex()
"5326481"
"fdsafsadfd"con't convert to int cause albha is not allowed to int
   

    
    
      '''



isAdmin=False;

booltoint = int(isAdmin)
print("==============before convertion========")
print(isAdmin)
print(type(isAdmin))
print("==============after bool to int conver=====")
'''
True ===> 1
False ===> 0
'''
print(booltoint)
print(type(booltoint))


avg =40.60;


print("==============before convertion========")
print(avg)
print(type(avg))
print("==============after float to int conver=====")
floattoint = int(avg)

print(floattoint)
print(type(floattoint))


'''
complex type to int is not possible
'''
MathVal=100+665j;
print("==============before convertion========")
print(MathVal)
print(type(MathVal))
print("==============after complex to int conver=====")
complextoint = int(MathVal)

print(complextoint)
print(type(complextoint))

