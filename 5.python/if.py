number=23
guess=int(input(input("Enter an interger")))

if guess == number:
    print("correct")
elif guess >number:
    print("smaller")
else:
    print("bigger")

print("done")