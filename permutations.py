def getValid_ps(ps, maps, cardinals):

    validps = []
    for p in ps:
        valid = 1
        for i in range(len(p) - 1):
            #print(p[i])
            if (maps[p[i]] != maps[p[i+1]]) and (maps[p[i]] < maps[p[i+1]] - 1):
                #print("1")
                valid = 0
                break
            if (maps[p[i]] != maps[p[i+1]]) and (maps[p[i]] > maps[p[i+1]] + 1):
                #print("2")
                valid = 0
                break

            if (maps[p[i]] == maps[p[i+1]]) and (cardinals[p[i]] > cardinals[p[i+1]] + 1):
                #print("3")
                valid = 0
                break

            if (maps[p[i]] == maps[p[i+1]]) and (cardinals[p[i]] < cardinals[p[i+1]] - 1):
                #print("4")
                valid = 0
                break
        
        if valid == 1:
            validps.append(p)
    
    return validps



def recursivePerm(currentletters, newString, currlength, desiredlength, perms):
    if currlength == desiredlength:
        perms.append(newString)
        return

    for i in range(len(currentletters)):
        ce = currentletters[i]
        newString+=ce
        del currentletters[i]
        recursivePerm(currentletters, newString, len(newString), desiredlength, perms)
        newString = newString[:-1]
        currentletters.insert(i, ce)

    if currlength == 0:
        return perms

    


perms = []
num = 0
desiredlength = 6



letters = []
for i in range(97, 97+9):
    letters.append(str(chr(i)))

maps = {"-1":-1 ,"a":0,"b":0,"c":0, "d":1, "e":1, "f":1, "g":2, "h":2, "i":2}
cardinals = {"a":0,"b":1,"c":2, "d":0, "e":1, "f":2, "g":0, "h":1, "i":2}

ps = recursivePerm(letters, '', 0, desiredlength, perms)
valid_ps = getValid_ps(ps, maps, cardinals)


eg = valid_ps[101]
patternmatrix = [[0,0,0],[0,0,0],[0,0,0]]

matrix_pts = []
for i in eg:
    row = maps[i]
    col = cardinals[i]
    matrix_pts.append([row, col])

print(eg)
print(matrix_pts)






















