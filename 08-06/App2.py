trainStatus="Stop";
track1 = int( input("Train1 travling in  : "))
track2 =int(input("Train2 travling in  : "))
track3=int(input("Train3 travling in  : "))
travlelResult = None;

if((track1 != track2) and (track1 != track3) and (track2!=track3) and (trainStatus == "Running")):
    travlelResult="Thank you for visiting come aging";
elif(((track1 ==track2 or track1 == track3 or track2 == track3) and (trainStatus=="Running"))):
    travlelResult="its got Accesident";
else:
    travlelResult="train has not starting";

print(travlelResult)



'''
or

'''

