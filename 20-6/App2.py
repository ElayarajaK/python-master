value1 = int(input("Enter the value1 "))
value2 = int(input("Enter the value2 " ))

def swap(arg1,arg2):
    temp = arg1;
    arg1 = arg2;
    arg2 = temp;
    return "value is swaped value 1 is : ",arg1," value 2 is  : ",arg2;

print(swap(value1,value2));

