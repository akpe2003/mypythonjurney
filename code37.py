with open("sample.txt") as f:
	y=f.read()
	
print(y)
print()
x=y.split(" ")
print(f"The file contains {len(x)} words.")