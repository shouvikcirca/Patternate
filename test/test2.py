import sys
import random
import time
import os
import cv2
import numpy as np

def getValid_ps(ps, maps, cardinals):
	validps = []
	for p in ps:
		valid = 1
		for i in range(len(p) - 1):

			if maps[p[i]] == maps[p[i + 1]] and abs(cardinals[p[i]] - cardinals[p[i+1]]) > 1 or cardinals[p[i]] == cardinals[p[i + 1]] and abs(maps[p[i]] - maps[p[i+1]]) > 1 or abs(maps[p[i]] - maps[p[i+1]]) > 1 and abs(cardinals[p[i]] - cardinals[p[i+1]]) > 1:
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




def transitionloci(maps, cardinal, valid_ps):
	eg = valid_ps[random.randint(0,len(valid_ps)-1)]

	print(eg)

	mat = np.zeros((500,500))

	pattern_matrix = [[0 for i in range(11)] for j in range(11)]
	matrix_pts = []
	for i in eg:
		row = maps[i]*200 + 50
		col = cardinals[i]*200 + 50
		matrix_pts.append((col, row))

	for i in range(len(matrix_pts) - 1):

		# mat = cv2.arrowedLine(mat, matrix_pts[i], matrix_pts[i+1], 255, 2, tipLength = 0.05)
		mat = cv2.line(mat, matrix_pts[i], matrix_pts[i+1], 255, 2)

		cv2.imshow('image', mat)

		if i < len(matrix_pts) - 2:
			cv2.waitKey(500)
		else:
			cv2.waitKey(0)


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
transitionloci(maps, cardinals, valid_ps)


