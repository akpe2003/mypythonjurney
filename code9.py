def patterns(my_list):
    y=len(my_list)
    for x in range(y):
        if my_list[x]==my_list[y-1]:
            print(f"Given list: {my_list} | Result is True.")
            break
        else:
            print(f"Given list: {my_list} | Result is False.")
            break
            
			
patterns([10, 20, 30, 40, 10])
print()
patterns([75, 65, 35, 75, 30])