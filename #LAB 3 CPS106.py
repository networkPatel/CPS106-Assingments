#LAB 3 CPS106

def encode(string, cipherbet):
    alphabet="abdefghijklmnopqrstuvwxyz"
    pile = ""

    for letter in string:
        if letter == " ":
            pile += " "
        else:
            i = alphabet.find(letter)
            pile += cipherbet[i]
    print(pile)

    # for letter in string:
    #     i = alphabet.find(letter)
    #     if i != -1 :
    #         pile += cipherbet[i]
    # print(pile)

    
encode("ama zon", "earthbcdfgijklmnopqsuvwxyz")

def setstring(string) :
    pile = ''
    for letter in string :
        if letter not in pile :
            pile += letter
            return pile
        

def build_cipherbet(keyword) :
    return setstring(keyword + 'abcdefghijklmnopqrstuvwxyz')


def decode(string1, cipherbet1):
    alphabet="abdefghijklmnopqrstuvwxyz"
    decoded = ""
    for letter in string1:
        if letter == " ":
            decoded += " "
        else: 
            i = cipherbet1.find(letter)
            decoded += alphabet[i]

    print(decoded)

decode("eje ylk", "earthbcdfgijklmnopqsuvwxyz")


#3.12 part b)
def build_cipherbet(keyword):
    alphabet="abdefghijklmnopqrstuvwxyz"
    pile = ""
    reversealphabet = ""
    for i in alphabet(25,0):
        reversealphabet = alphabet[i]

    print(keyword + reversealphabet)

#3.13
def duplicate(duplicateString):
    print(duplicateString*4)

duplicate("alphabet")

#3.16
def spaceitout(spaceString, n):
    result = ""
    for i in spaceString:
        result += i + " " *n
    
    print(result)

spaceitout("It was a dark and stormy night", 3)

def spaceout(spaceOutString, num):
    result = ""
    a = spaceOutString.split()
    for i in a:
        result += i + " " * num

    print(result)

spaceout("It was a dark and stormy night", 3)