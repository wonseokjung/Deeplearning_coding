number = 23
running=True

while running:
    guess= int(input("Enter an interger:"))

    if guess==23:
        print("Congra")
        running= False # this makes whilte loop to stop
    elif guess>number:
        print("number is smaller")
    else :
        print("number is bigger")
else:
    print("done")