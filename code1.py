print("Printing current and previous number sum in a range(10)")
print()
previous_num=0
for i in range(10):
    current_num=i 
    print(f"Current number is: {current_num} and the Previous number is:{previous_num} and the sum is: {previous_num + current_num}.")
    previous_num=current_num
    