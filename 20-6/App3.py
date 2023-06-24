def printData(para1,para2,para3):
    Add_value= "Addition is : ",(para1+para2+para3)
    '''
        what is meany by local variable
        Add_value
        if any of the variable is declared with in a funtion
        that variable is called as local variable 
        can't access that variable from outside function
    '''
    print(Add_value)
print(Add_value)

if(True):
    isAdmin="from if"
    print(isAdmin)
else:
    print("Nothing to print")

print(isAdmin)