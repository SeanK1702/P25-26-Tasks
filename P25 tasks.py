#Sean Kenneally
#19/9/24
#P25

#Task 1
#artist = input("Favourite artist:")
#comment = " is good"
#print(artist + comment)
#print("\n")

#Task 2
#name = input("Type full name: ")
#fName = name[:5]
#sName = name[5:]
#print(fName + sName)
#print("\n")

#Task 3
#hours = int(input("Hours: "))
#minutes = int(input("Minutes: "))
#seconds = int(input("Seconds: "))
#sHours = hours*3600
#sMinutes = minutes*60
#print("This time in seconds is: ", seconds+sHours+sMinutes)
#print("\n")

#Task 4
#digits = int(input("Insert a five-digit number: "))
#print("This time in minutes is: ", digits/60)
#print("\n")

#Task 5
#i1 = input("Type something here: ")
#i2 = input("Type something here: ")
#i3 = input("Type something here: ")
#i4 = input("Type something here: ")
#i5 = input("Type something here: ")
#ascii1 = ord(i1)
#ascii2 = ord(i2)
#ascii3 = ord(i3)
#ascii4 = ord(i4)
#ascii5 = ord(i5)
#print(i1,"=",ascii1)
#print(i2,"=",ascii2)
#print(i3,"=",ascii3)
#print(i4,"=",ascii4)
#print(i5,"=",ascii5)
#print("\n")

#Task 6
#units = float(input("Input units: "))
#unitCharge = units*0.19
#fullCharge = unitCharge + 26.20
#print("The full charge is", fullCharge)
#print("\n")

#Task 7
#chips = float(input("Input amount of portions of chips: "))
#fish = float(input("Input amount of portions of fish: "))
#fishPrice = fish*4.50
#chipsPrice = chips*2.80
#print("Total cost: ", fishPrice + chipsPrice)
#print("\n")

#Task 8
character1 = "H"
character2 = "e"
character3 = "l"
character4 = "l"
character5 = "o"
character6 = "!"
key = 6
ascii1 = ord(character1)
ascii2 = ord(character2)
ascii3 = ord(character3)
ascii4 = ord(character4)
ascii5 = ord(character5)
ascii6 = ord(character6)
encryptedLetter1 = chr(ascii1 + key)
encryptedLetter2 = chr(ascii2 + key)
encryptedLetter3 = chr(ascii3 + key)
encryptedLetter4 = chr(ascii4 + key)
encryptedLetter5 = chr(ascii5 + key)
encryptedLetter6 = chr(ascii6 + key)
print("The encrypted letter is: ", encryptedLetter1)
print("The encrypted letter is: ", encryptedLetter2)
print("The encrypted letter is: ", encryptedLetter3)
print("The encrypted letter is: ", encryptedLetter4)
print("The encrypted letter is: ", encryptedLetter5)
print("The encrypted letter is: ", encryptedLetter6)