#P is the paintext letter and k is the amount of positions the letter needs to be changed by
def cipher(p, k):
    return ((p + k) % 26)

def findp(a):
    counter = -1
    for x in "abcdefghijklmnopqrstuvwxyz":
        counter += 1
        if x == a:
            return counter

def encrypt(a, k):
    lst = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for x in a:
        if x == "!" or x == "?" or x == "." or x == "," or x == " ":
            ciphertext += str(x)
        else:
            ciphertext += str(lst[cipher(findp(x), k)])
    return ciphertext

plaintext = input("plaintext: ")
key = int(input("key: "))
print("ciphertext: " + encrypt(plaintext, key))