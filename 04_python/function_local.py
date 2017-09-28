x=50

def func(x):
    print("check if x works only local",x)
    x=2
    print("changed x to",x)

func(4)

print(func(x))

