list1 = [10, 20, 25, 30, 35]

list2 = [40, 45, 60, 75, 90]

x=len(list1)
y=len(list2)

full_list=[]

for big in range(x):
	if list1[big]%2 !=0:
		full_list.append(list1[big])
		
		
for big2 in range(y):
	if list2[big2]%2==0:
		full_list.append(list2[big2])
		
print(full_list)