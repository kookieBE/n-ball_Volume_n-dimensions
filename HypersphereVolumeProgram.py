#Simple program designed to find volume of n-ball in n dimensions

import random
import math

n = 8 #number of dimensions
x = 1000000 #number of points to be pinged
reps = 10 #number of repitions to be made

#pointsPinged = [] #list of all points in space which have been made
#lengths = [] #output list for magnitude function
ratioResults = []

def randPoint(): #defining function which returns a point with a random set of coordinates
  i=0
  point = []
  while(i<n):
    i += 1
    point.append(random.uniform(-1,1));
  return point;

def magnitude(list): #defining function which finds magnitude of vector drawn from origin to point
  toBeSummed = []
  for v in list:
    toBeSummed.append((v)**2)
  leng = math.sqrt(sum(toBeSummed))
  return leng;

def sort(list, writeTo): #function finds ratio
	for v in list:
		if v <= 1:
			writeTo[0] += 1;
		writeTo[1] += 1;

def listWriter(list):
  fileOpened = open('./valueDump.txt', 'a') #change path for where to write program to
  for r in list:
    fileOpened.write(str(r)+'\n')

k=0
while k != reps:
  k += 1
  pingedPoints = []
  lengths = []
  j=0 #while loop which makes 'x' number of points
  while j!=x:
    j += 1
    pingedPoints.append(randPoint())
  
  for p in pingedPoints:
    lengths.append(magnitude(p))
  indvRatio = [0,0]
  sort(lengths, indvRatio)
  print(str(k)+' '+str(indvRatio))
  ratioResults.append(indvRatio)
#print(ratioResults)

#listWriter(ratioResults)


#print(pingedPoints);
#print("");
#print(lengths);
#print("");
#print(ratio);