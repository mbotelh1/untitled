__author__ = 'mbotelh1'

print("Hello World")

reply = -1

while reply != 0:

    try:
        reply = int(input("Enter a positive integer, zero when done: "))

        if reply <= -1:
            print("You enter a negative integer, try again")

        else:
            print("Your input doubled is ", reply * 2)
    except:
        print("You did not enter an integer")