Marks =int(input("Enter the Marks"))
printData=None;

if(Marks < 40):
    if(Marks < 10):
        printData="Better to search Another Field"
    elif(Marks>10 and Marks < 20):
        printData="Give More Hard Work"
    elif(Marks >20 and Marks < 30):
        printData="Required more revisions"
    else:
        printData="Study Properly"
elif(Marks > 40 and  Marks < 60):
    printData="Congrats got a C grade"
elif(Marks>60 and Marks <=75):
    printData="B Grade ";
elif(Marks>75 and Marks <90):
    printData="A Grade"
elif(Marks >90 and Marks <100):
    printData="S Grade"
else:
    if():
       print()
    elif():
        print()

printData="Over Gradiations"



print(printData)