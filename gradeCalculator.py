def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    
    try:
        hrs = float(input("Enter score:"))

        if hrs <= 1 and hrs >= .9:
            print('A')
        elif hrs <= .9 and hrs >= .8:
            print('B')
        elif hrs <= .8 and hrs >= .7:
            print('C')
        elif hrs <= .7 and hrs >= .6:
            print('D')
        elif hrs <= .6 and hrs > 0:
            print('F')
        else :
            print("Bad score")

    except:
        print("Bad score")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()