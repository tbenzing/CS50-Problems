def wasUpper(a):
    upper = 0
    for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if a == x:
            upper += 1

    if upper == 1:
        return True
    else:
        return False

def checkSub(a):
    if len(a) < 26:
        return False
    else:
        return True

def findPlaces(a):
    counter = -1
    lowera = a.lower()
    for x in "abcdefghijklmnopqrstuvwxyz":
        counter += 1
        if x == lowera:
            return counter

def encrypt(a, b):
    ptext = a
    cipher = list(b)
    ctext = ""
    for x in ptext:
        if x == "!" or x == "?" or x == "." or x == "," or x == " ":
            ctext += x
        else:
            if wasUpper(x) == False:
                ctext += cipher[findPlaces(x)]
            else:
                ctext += (cipher[findPlaces(x)]).upper()
    return ctext

substitution = input("substitution: ")
if checkSub(substitution) == True:
    plaintext = input("plaintext: ")
    print("ciphertext: " + encrypt(plaintext, substitution))
else:
    print("Your substitution must be 26 characters.")
