text = "electronics and telecommunication"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

text = "python programming"

print(text.find("pro"))      # index or -1
print(text.index("python"))  # index or error
print(text.count("p"))
print(text.startswith("py"))
print(text.endswith("ing"))

text1 = "Python123"
text2 = "12345"
text3 = "python"

print(text1.isalnum())
print(text2.isdigit())
print(text3.isalpha())
print(text3.islower())
print(text3.isupper())
print(text3.isspace())
