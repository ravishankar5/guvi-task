TW=9 #Amount for TwoWheeler per distance 
A=12 #Amount for Auto per distance
C=20 #Amount for Cab per distance
print("Welcome to Uber\n1.'TwoWheeler'\n2.'Auto\n3.'Cab'")
option=(input("Enter your vehicle from above"))
if option=="1" or option=="TwoWheeler":
    sp=int(input("Enter the Starting Point"))
    ep=int(input("Enter the Ending Point"))
    dis=ep-sp
    print("-----***Boking Confirm***-----")
    print("Your Starting point is " ,sp)
    print("Your Ending point is " ,ep)
    print("Total Distance is",dis)
    amount=dis*TW
    print("Expected Amount to be paid" ,amount)
    print("Enjoy your Ride")
elif option=="2" or option=="Auto":
    sp=int(input("Enter the Starting Point"))
    ep=int(input("Enter the Ending Point"))
    dis=ep-sp
    print("--***Boking Confirm***--")
    print("Your Starting point is " ,sp)
    print("Your Ending point is " ,ep)
    print("Total Distance is",dis)
    amount=dis*A
    print("Expected Amount to be paid" ,amount)
    print("Enjoy your Ride")
elif option=="3" or option=="Cab":
    sp=int(input("Enter the Starting Point"))
    ep=int(input("Enter the Ending Point"))
    dis=ep-sp
    print("--***Boking Confirm***--")
    print("Your Starting point is " ,sp)
    print("Your Ending point is " ,ep)
    print("Total Distance is",dis)
    amount=dis*C
    print("Expected Amount to be paid" ,amount)
    print("Enjoy your Ride")
else:
    print("Enter only above three number or Vehicle")


