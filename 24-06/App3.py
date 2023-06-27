class A:
    name="Raja";
    #constructor 
    '''
        syntax 
        def __init__(self):
            statement
    '''
    def __init__(self):
        print("From constructor")


print(A.name)
#constructor is executing during object creation
#constructor is used for initialization for instance type of variable
# def __init__(self): 
#constructor can create with in classes only outside of class  constructor is not possible
obj1 = A();

