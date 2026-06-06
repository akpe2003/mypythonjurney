text = "hello world from python"
text_new=text.split(" ")
print(text_new)
print()
sentence=[]
for word in text_new:
    y=word.capitalize()
    sentence.append(y)
    
print(sentence)
print()
z=" ".join(sentence)
print(z)