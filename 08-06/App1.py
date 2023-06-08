Marks = int(input("Enter the marks"))#100
Marks1 = int(input("Enter the marks"))#50

Marks2 = int(input("Enter the marks"))
Marks3 = int(input("Enter the marks3"))

'''
    logical operators
    AND
    A1      A2         A3          Result
    True   True        True         True
    True   True        False        False
    False  False       True        False
    False  False       False        False
    False  True        True         False


    OR
    A1      A2         A3          Result
    True    True      False         True
    False   False    True           True 
    False   False    False          False
    True    True     True            True

    NOT
    True   False
    False  True
'''
#      100       50           50      70

maxMarks=None;
if((Marks > Marks1)and (Marks > Marks2) and (Marks > Marks3)):
    maxMarks="Max Marks is",Marks;
elif((Marks1 > Marks)and (Marks1 > Marks2) and (Marks1 > Marks3)):
     maxMarks="Max Marks is",Marks1;

print(maxMarks)
Result =None

if(Marks < 40):
    Result="Marks is bellow 40 you are fails";

else:
    Result="Marks above 40  you are pass"
print(Result)