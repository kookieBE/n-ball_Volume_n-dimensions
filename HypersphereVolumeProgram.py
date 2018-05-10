import random

n = 3 #number of dimensions
x = 10000 #number of points to be pinged
reps = 10 #number of repitions to be made

def randPoint(): #defining function which returns a point with a random set of coordinates
  i=0
  point = []
  while(i<n):
    i += 1
    point.append(random.uniform(-1,1));
  return point;

def magnitude(list): #defining function which finds magnitude of vector drawn from origin to point
  sum = []
  for v in list:
    sum.append((v)**2)
  leng = (sum)**0.5
  return leng;

def sort(list): #function finds ratio
	for v in list:
		if v <= 1:
			rat[0] += 1;
	rat[1] = x;
	return rat

k=0
ratio = []
while k != reps:
  k += 1
  pingedPoints = []
  lengths = []
  
  j=0
  while j!=x:
    j += 1
    pingedPoints.append(randPoint())
  
  for p in pingedPoints:
    lengths.append(magnitude(p))
  indvRatio = [0,0]
  indvRatio = sort(lengths)
  print(str(k)+' '+str(indvRatio))
  ratio.append(indvRatio)

#print(ratio)
