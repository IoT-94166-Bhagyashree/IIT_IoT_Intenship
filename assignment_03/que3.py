# Function to count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    v = 0
    for ch in s:
        if ch in vowels:
            v += 1
    return v


# Function to count consonants
def count_consonants(s):
    vowels = "aeiouAEIOU"
    c = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            c += 1
    return c


# Function to calculate ratio of vowels to consonants
def vowel_consonant_ratio(s):
    v = count_vowels(s)
    c = count_consonants(s)

    if c == 0:
        return "Ratio not defined (no consonants)"

    return v / c


# Main program
text = input("Enter a string: ")

print("Number of vowels:", count_vowels(text))
print("Number of consonants:", count_consonants(text))
print("Vowel to Consonant Ratio:", vowel_consonant_ratio(text))
