'''number =int(input("Enter any Number"))

print( not(number == 10))'''
number1 =int(input("Enter any Number1 : "))
number2 =int(input("Enter any Number2 : "))
number3=int(input("Enter the Number3 : "))
number4= int(input("Enter the number4 : "))
Max=None;
'''
if(number1 >= number2):
    Max=number1
else:
    Max=number2
    '''
#(condition)?"":"" 

Max = number1 if (number1 > number2 and number1 > number3 and  number1 > number4) else number2 if number2> number3 and number2 > number4 else number3 if number3 > number4 else number4


Min = number1 if number1<number2 else number2;

print("Maximum Val : ",Max)
print("Min  Val : ",Min)
