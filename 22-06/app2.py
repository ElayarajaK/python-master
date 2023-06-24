'''
local variable
      1. variables declared with a funtion that variable is called local variable
      2. 
Globel variable
'''

name=None;#Globel variable

def Variables():
    Address="Chennai";
    global College;
    College="IIT";    
    print(name,", ",Address,", ",College)
Variables();
print(name)
print(College)
#recurssion