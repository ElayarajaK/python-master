'''number =int(input("Enter any Number"))

print( not(number == 10))'''
number1 =int(input("Enter any Number1 :"))
number2 =int(input("Enter any Number2"))
Max=None;
'''
if(number1 >= number2):
    Max=number1
else:
    Max=number2
    '''
#(condition)?"":"" 

Max = number1 if number1>number2 else number2;
print(Max)