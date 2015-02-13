n = raw_input()
n = int(n)
for i in range(0,n):	
	x,y,x1,y1,x2,y2 = raw_input().split()
	x = int(x)
	x1 = int(x1)
	x2 = int(x2)
	y = int(y)
	y1 = int(y1)
	y2 = int(y2)

	ans = abs(x - x1)
	if abs(x-x2) < ans:
		ans = abs(x-x2)
	if abs(y-y1) < ans:
		ans = abs(y-y1)
	if abs(y-y2) < ans:
		ans = abs(y-y2)
   
	print ans    

