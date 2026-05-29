def Slice_Words():
	word=input("Please enter a any word/string here: ")
	word=str(word)
	print()
	number=input("Please from what index number in the word you entered here should we start slicing from?")
	number=int(number)
	print()
	final_string=word[number:]
	print(final_string)
	
Slice_Words()
