for i in range(6):
	for j in range(i):
		print(i, end=" ")
	print()
    
print()
for i in range(5):
    for j in range(i):
        print(i, end=" ")
    print(" ")
    
    
print()
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("")
    
print()
rows=5
b=0
for i in range(rows,0,-1):
    b +=1
    for j in range(1,i+1):
        print(b,end=" ")
    print("\r")