def checkright(a):
    if a <= 8 or a >= 1:
        return True
    else:
        return False

def makespace(a):
    counter = a
    while counter >= 1:
        print(" ", end=" ")
        counter -= 1

def makehash(a):
    counter = a
    while counter >= 1:
        print("#", end=" ")
        counter -= 1

def makestring(a):
    counter = a
    string = ""
    while counter >= 1:
        string += "a"
        counter -= 1
    return string

def makepyramid(a):
    string = makestring(a)
    counter = a
    counterb = 0
    for char in string:
        counterb += 1
        (makespace(counter - 1)); (makehash(counterb)); (makespace(1)); (makehash(counterb)); (makespace(counter - 1))
        print("\n")
        counter -= 1

get_int = int(input("Number: "))
checkright(get_int)
while checkright(get_int) == False:
    get_int = input("Number: ")
    checkright(get_int)
makepyramid(get_int)