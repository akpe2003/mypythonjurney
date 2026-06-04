for i in range(1,6):
	for j in range(1,i+1):
		print(j, end=" ")
	print(" ")
    
print()
rows=5
b=0
for i in range(rows,0,-1):
    b +=1
    for j in range(1,i+1):
        print(b, end=" ")
    print(" ")
print()   
rows=5
num=rows
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(num, end=" ")
    print(" ")
    
print()
rows=5
for i in range(rows,0,-1):
    for j in range(0,i+1):
        print(j, end=" ")
    print(" ")
    
print()
rows=5
for i in range(rows,0,-1):
    num=i
    for j in range(0,i):
        print(num, end=" ")
    print("\r")

print()    
rows=6
for i in range(1,rows):
    for j in range(i,0,-1):
        print(j, end=" ")
    print("\r")