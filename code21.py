prev2=0
prev1=1
#print(prev2)
#print(prev1)
full_list=[]
full_list.append(prev2)
full_list.append(prev1)
for fibo in range(13):
    newFibo=prev2+prev1
    full_list.append(newFibo)
    #print(newFibo)
    prev2=prev1
    prev1=newFibo
    
print(full_list)