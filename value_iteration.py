import copy
discount_factor = 0.99
def checkChange(now, earlier):
	now = abs(now)
	earlier = abs(earlier)
	delta = abs(now-earlier)
	
	factor = (1-discount_factor)/discount_factor; 
	try:
		if(delta < 0.01*factor):
			return 0
		else:
			return 1
	except ZeroDivisionError:
		return 0

n,m = input().split()
n = int(n)
m = int(m)
grid = [[0 for x in range(m)] for y in range(n)]	

for i in range(n):
	inp = list(map(float,input().split()))
	grid[i] = inp
# for i in range(n):
# 	for j in range(m):
# 		print (grid[i][j],end = '') 
# print (grid)
e,w = input().split()
e = int(e)
w = int(w)

end_states = [[0 for x in range(2)] for y in range(e)] 

for i in range(e):
	a,b = input().split()
	a = float(a)
	b = float(b)
	end_states[i][0] = a
	end_states[i][1] = b
	# grid[a][b] = 'E'

# print (end_states)

walls = [[0 for x in range(2)] for y in range(w)] 

for i in range(w):
	a,b = input().split()
	a = float(a)
	b = float(b)
	walls[i][0] = a
	walls[i][1] = b
	# grid[a][b] = 'W'

a,b = input().split()
a = int(a)
b = int(b)
start = []
start.append(a)
start.append(b)

reward = input();
reward = float(reward)

# end of user input
# start of utility calulation
temp = copy.deepcopy(grid)
previousValues = copy.deepcopy(grid)
cont = 1
moves = [[0 for x in range(m)] for y in range(n)]	

print ('Input Matrix')
for i in range(n):
		for j in range(m):
			print (temp[i][j],end = ' ')
		print ('\n')

for k in range(10000):
	cont = 0
	print('Iteration: ' + str(k+1)) 
	for i in range(n):
		for j in range(m):
			# for i in range(n):
			# 	for j in range(m):
			# 		print (grid[i][j],end = ' ')
			# 	print ('\n')
			# print ('*********************************') 
			utilityNorth = 0;
			utilitySouth = 0;
			utilityEast = 0;
			utilityWest = 0;

			if ([i,j] not in end_states) and ([i,j] not in walls):
				# checking when we want to go north
				correct = 0
				wrong1 = 0
				wrong2 = 0
				if(i>=1 and [i-1,j] not in walls):
					correct = temp[i-1][j]
				else:
					correct = temp[i][j]
				if(j>=1 and [i,j-1] not in walls):
					wrong1 = temp[i][j-1]
				else:
					wrong1 = temp[i][j]
				if(j<=m-2 and [i,j+1] not in walls):
					wrong2 = temp[i][j+1]
				else:
					wrong2 = temp[i][j]
				
				utilityNorth = 0.8*float(correct) + 0.1*float(wrong1) + 0.1*float(wrong2) + float(reward)
				# Checking when we want to go south
				correct = 0
				wrong1 = 0
				wrong2 = 0
				if(i<=n-2 and [i+1,j] not in walls):
					correct = temp[i+1][j]
				else:
					correct = temp[i][j]
				if(j>=1 and [i,j-1] not in walls):
					wrong1 = temp[i][j-1]
				else:
					wrong1 = temp[i][j]
				if(j<=m-2 and [i,j+1] not in walls):
					wrong2 = temp[i][j+1]
				else:
					wrong2 = temp[i][j]
				
				utilitySouth = 0.8*float(correct) + 0.1*float(wrong1) + 0.1*float(wrong2) + float(reward)

				# Checking when we want to go east
				correct = 0
				wrong1 = 0
				wrong2 = 0
				if(j<=m-2 and [i,j+1] not in walls):
					correct = temp[i][j+1]
				else:
					correct = temp[i][j]
				if(i>=1 and [i-1,j] not in walls):
					wrong1 = temp[i-1][j]
				else:
					wrong1 = temp[i][j]
				if(i<=n-2 and [i+1,j] not in walls):
					wrong2 = temp[i+1][j]
				else:
					wrong2 = temp[i][j]
				
				utilityEast = 0.8*float(correct) + 0.1*float(wrong1) + 0.1*float(wrong2) + float(reward)

				# Checking when we want to go west

				correct = 0
				wrong1 = 0
				wrong2 = 0
				if(j>=1 and [i,j-1] not in walls):
					correct = temp[i][j-1]
				else:
					correct = temp[i][j]
				if(i>=1 and [i-1,j] not in walls):
					wrong1 = temp[i-1][j]
				else:
					wrong1 = temp[i][j]
				if(i<=n-2 and [i+1,j] not in walls):
					wrong2 = temp[i+1][j]
				else:
					wrong2 = temp[i][j]
				
				utilityWest = 0.8*float(correct) + 0.1*float(wrong1) + 0.1*float(wrong2) + float(reward)
				# print (max(utilityNorth, utilitySouth, utilityEast, utilityWest))
				temp[i][j] = discount_factor * max(utilityNorth, utilitySouth, utilityEast, utilityWest) + grid[i][j]
				if(temp[i][j] == discount_factor *utilityNorth + grid[i][j]):
					moves[i][j] = 'N'
				elif(temp[i][j] == discount_factor *utilitySouth + grid[i][j]):
					moves[i][j] = 'S'
				elif(temp[i][j] ==discount_factor * utilityEast + grid[i][j]):
					moves[i][j] = 'E'
				elif(temp[i][j] ==discount_factor * utilityWest + grid[i][j]):
					moves[i][j] = 'W'
			if([i,j] in end_states or [i,j] in walls):
				moves[i][j] = 'o'

	
	for i in range(n):
		for j in range(m):
			print ("%.4f" % temp[i][j],end = '    ')
		print ('\n')

	for i in range(n):
		for j in range(m):
			print (moves[i][j],end = '    ')
		print ('\n')
	
	print ('********************')			
	for i in range(n):
		for j in range(m):
			if(checkChange(temp[i][j], previousValues[i][j])):
				cont = 1
				break;
		if(cont == 1):
			break
	if(cont == 0):
		break
	previousValues = copy.deepcopy(temp)
