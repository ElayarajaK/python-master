

'''
comparator operators 
=====================
==(equ)  (10 == 10 )  = True
!=(not)  (5 != 10)    =True  | (10 ==10 )  = false
<=(less eql)   (5 <= 10 )   = True  ||  (10 <= 10)=true || (10 < 5) = false
>=(grea eql)  (100 >  50 )  = true || (100 >= 100 )=true || (100 > 200)= false
<(less)   (10 < 10) =false
>(greater)    (100 > 100 )=false
'''

Math_Marks = int(input("Enter the m marks : "));
S_Marks =int(input("Enter the s marks : "));

print(Math_Marks)
print(S_Marks)
print(Math_Marks == S_Marks)
if(True):
    print("Hello if ..")
else:
    print("Hello else ..")

if(Math_Marks > S_Marks):
    print("Max marks math")
    
else:
    print("math marks min")
