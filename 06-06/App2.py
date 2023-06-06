'''
        Other type to bool
'''

value=-10;

print("==============before convertion========")
print(value)
print(type(value))
print("==============after bool to int conver=====")
'''
  other than zero any number is true
  zero is false
'''
booltoint = bool(value)

print(booltoint)
print(type(booltoint))
print("=================");


avg=0.0;

print("==============before convertion========")
print(avg)
print(type(avg))
print("==============after bool to folat conver=====")
floattobool = bool(avg)

print(floattobool)
print(type(floattobool))
print("=================");

avg=0.0;
Origin = "\\";
print("==============before convertion========")
print(Origin)
print(type(Origin))
print("==============after bool to folat conver=====")
'''
if it is empty or None string to bool retun false
anystring return true
'''
strtobool = bool(Origin)

print(strtobool)
print(type(strtobool))
print("=================");

complexNumber=0+1j;

print("==============before convertion========")
print(complexNumber)
print(type(complexNumber))
print("==============after complext to bool conver=====")
comtobool = bool(complexNumber)

print(comtobool)
print(type(comtobool))
print("=================");

