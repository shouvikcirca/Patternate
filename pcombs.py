import random

def checkVerticalValidity(current, previous, maps):
    if maps[previous] == - 1:
        return True
    if maps[previous] < maps[current] - 1:
        return False
    if maps[previous] > maps[current] + 1:
        return False

    if cardinals[previous] > cardinals[current] + 1:
        return False

    if cardinals[previous] < cardinals[current] - 1:
        return False

    return True


letters = []
for i in range(97, 97+9):
    letters.append(str(chr(i)))


maps = {"-1":-1 ,"a":0,"b":0,"c":0, "d":1, "e":1, "f":1, "g":2, "h":2, "i":2}
cardinals = {"a":1,"b":2,"c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9}


#letters.pop(0)
print(letters)



ns = ''
previous = "-1"
current = -1
while len(ns) < 4:
    l = random.randint(0,len(letters)-1)
    current = letters[l]
    goForward = checkVerticalValidity(current, previous, maps)
    print(ns, maps[previous], goForward)
    if goForward:
        ns+=current
        letters.pop(l)
        previous = current
print(ns)

