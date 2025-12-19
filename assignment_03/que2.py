
#basic slicing
text = "PythonProgramming"

print("Original String:", text)
print("First 6 characters:", text[0:6])
print("From index 6 to end:", text[6:])
print("From start to index 6:", text[:6])

#negative indexing
text = "PythonProgramming"

print("Last 5 characters:", text[-5:])
print("All except last 5:", text[:-5])
print("Middle part:", text[-11:-5])

#step slicing
text = "PythonProgramming"

print("Every 2nd character:", text[::2])
print("Every 3rd character:", text[::3])
print("Characters from index 1 to 10 with step 2:", text[1:10:2])

#reverse string
text = "Python"

print("Original:", text)
print("Reversed:", text[::-1])

#slicing with user input
text = input("Enter a string: ")

print("Original String:", text)
print("First half:", text[:len(text)//2])
print("Second half:", text[len(text)//2:])
print("Alternate characters:", text[::2])      
print("Reverse string:", text[::-1])



