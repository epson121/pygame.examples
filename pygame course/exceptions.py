#exceptions
try: 
	x = 5/0
except:
	print("Error")


numberEntered=False
while numberEntered == False:
    numberString = input("Enter an integer: ")
    try:
        n = int(numberString)
        numberEntered = True
    except:
        print ("Error, invalid integer")