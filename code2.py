print("Original String is:  pynative.")
print("Printing only even index chars.")
print()
y="pynative"
z=len(y)
for i in range(z):
    if i%2==0:
        print(y[i])