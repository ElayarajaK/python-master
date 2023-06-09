TrainStatus=input("Start / Stoped")
Train1 = int(input("Enter the Train no :"))
Train2 = int(input("Enter the Train no :"))
Train3 = int(input("Enter the Train no :"))

Track1 = int(input("Enter the Train1  Track no :"))
Track2 = int(input("Enter the Train2  Track no :"))
Track3 = int(input("Enter the Train3  Track no :"))

travelResult=None;
if(Track1 !=Track2 and Track1 != Track3 and Track2 != Track3 and TrainStatus=="Start"): 
    travelResult="Thanks visitAgain";
elif((Track1 == Track2 or Track1 == Track3 or Track2 == Track3)and (TrainStatus=="Start")):
    travelResult="Accident Happen";
else:
    travelResult="Still train has not start to travel";

print(travelResult)

