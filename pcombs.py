import sys
import random

def getValid_ps(ps, maps, cardinals):
    validps = []
    for p in ps:
        valid = 1
        for i in range(len(p) - 1):
            #print(p[i])
            if (maps[p[i]] != maps[p[i+1]]) and (   (abs(maps[p[i]] - maps[p[i+1]]) > 1) or (abs(cardinals[p[i]] - cardinals[p[i+1]]) >1 )  ):
                #print("1")
                valid = 0
                break

            if (maps[p[i]] == maps[p[i+1]]) and (abs(cardinals[p[i]] - cardinals[p[i+1]]) > 1):
                #print("3")
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



def applyTransition(startnode, endnode, patternmatrix):
    if (startnode[0] == endnode[0]) and(startnode[1] < endnode[1]):
        i = startnode[0]
        for j in range(startnode[1], endnode[1]+1):
            patternmatrix[i][j] = 1
    elif (startnode[0] == endnode[0]) and(startnode[1] > endnode[1]):
        i = startnode[0]
        for j in range(startnode[1], endnode[1]-1, -1):
            patternmatrix[i][j] = 1
    elif (startnode[1] == endnode[1]) and(startnode[0] < endnode[0]):
        j = startnode[1]
        for i in range(startnode[0], endnode[0]+1):
            patternmatrix[i][j] = 1
    elif (startnode[1] == endnode[1]) and(startnode[0] > endnode[0]):
        j = startnode[1]
        for i in range(startnode[0], endnode[0]-1, -1):
            patternmatrix[i][j] = 1
    elif (startnode[0] > endnode[0]) and(startnode[1] > endnode[1]):
        j = startnode[1]
        i = startnode[0]
        while i>=endnode[0]:
            patternmatrix[i][j] = 1
            i-=1
            j-=1
    elif (startnode[0] < endnode[0]) and(startnode[1] < endnode[1]):
        j = startnode[1]
        i = startnode[0]
        while i<=endnode[0]:
            patternmatrix[i][j] = 1
            i+=1
            j+=1
    elif (startnode[0] < endnode[0]) and(startnode[1] > endnode[1]):
        j = startnode[1]
        i = startnode[0]
        while i<=endnode[0]:
            patternmatrix[i][j] = 1
            i+=1
            j-=1
    elif (startnode[0] > endnode[0]) and(startnode[1] < endnode[1]):
        j = startnode[1]
        i = startnode[0]
        while i>=endnode[0]:
            patternmatrix[i][j] = 1
            i-=1
            j+=1

    



def transitionloci(eg, maps, cardinal, valid_ps):
    print(eg)
    pattern_matrix = [[0 for i in range(11)] for j in range(11)]
    matrix_pts = []
    for i in eg:
        row = maps[i]*5
        col = cardinals[i]*5
        matrix_pts.append([row, col])

    print(matrix_pts)
    for i in range(len(matrix_pts) - 1):
        applyTransition(matrix_pts[i], matrix_pts[i+1], pattern_matrix)


    print()
    for i in pattern_matrix:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()
    


perms = []
num = 0
desiredlength = int(sys.argv[1])+1



letters = []
for i in range(97, 97+9):
    letters.append(str(chr(i)))

maps = {"-1":-1 ,"a":0,"b":0,"c":0, "d":1, "e":1, "f":1, "g":2, "h":2, "i":2}
cardinals = {"a":0,"b":1,"c":2, "d":0, "e":1, "f":2, "g":0, "h":1, "i":2}

ps = recursivePerm(letters, '', 0, desiredlength, perms)
valid_ps = getValid_ps(ps, maps, cardinals)

#getPattern(valid_ps) replaced by transitionloci


for item in valid_ps:
    transitionloci(item, maps, cardinals, valid_ps)
    print()
    print()



