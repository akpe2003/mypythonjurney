num_list = [10, 20, 33, 46, 55]
y=len(num_list)
z=[]
for x in range(y):
	if num_list[x] % 5 ==0:
		z.append(num_list[x])
		
print(z)
				