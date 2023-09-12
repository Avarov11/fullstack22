length = 0
word= 0
vowel = 0
vowels = ("AEIOUaeiou")
enterr = input("enter ur sentence >")
for char in enterr:
    length += 1
    if char in vowels:
        vowel += 1
    elif char == ' ':
        word += 1
word+= 1
print("length of the sentence:", length)
print("number of words in the sentence:", word)
print("number of vowels in the sentence:", vowel)