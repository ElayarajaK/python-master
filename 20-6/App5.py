'''
variable lenth arguments
'''
'''
def addValue():
    print("value added");

def addValue(para1):
    print("value added pro",para1);

def addValue(para1,para2):
    print("value added pro",(para1+para2));

def addValue(para1,para2,para3):
    print("value added pro",(para1+para2+para3));

def addValue(para1,para2,para3,para4):
    print("value added pro",(para1+para2+para3+para4));
'''
def addValue(*arg):
    print("Value : ",arg)

addValue()
addValue(10)
addValue(10,20)
addValue(10,20,30)
addValue(10,20,30,40,50);
addValue(10,20,30,40,50,60);
addValue(10,20,30,40,50,60,70);
addValue(10,20,30,40);
addValue(10,20,30,40);
