books = int(input("How many books have you puchased in the last year?: "))

if books >= 8:
    print("You have received 60 points")
else:
    if books >= 6:
        print("You have received 30 points")
    else:
        if books >= 4:
            print("You have received 15 points")
        else:
            if books >= 2:
                print("You have received 5 points")
            else:
                print("You have received no points")