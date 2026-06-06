with open("notes.txt","w") as f:
	f.write("Hello, this is my first note.\r")
	f.write("Python file handling is simple.\r")
	f.write("End of file.\r")
	
with open("notes.txt") as f:
	print(f.read())