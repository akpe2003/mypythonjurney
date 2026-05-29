n=input("Please enter a value with which we will calculate its factorial here: ")
n=int(n)
print()
factorial=1
final_result=None 
for i in range(1,n+1,1):
    first_result=factorial * i
    final_result *= first_result
    
    
    
print(final_result)

    

	
