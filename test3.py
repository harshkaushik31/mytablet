# To diaplay the number of vowels, consonants, uppercase letter, lower case letters in a file named "Answer.txt"
myfile = open("Answer.txt",'r')
data = myfile.read()
vowels = ['a','e','i','o','u','A','E','I','O','U']
vowel_count = consonat_count = upper_count = lower_count = 0
for i in data:
    if i in vowels:
        vowel_count += 1
    if i not in vowels:
        consonat_count += 1
    if i.isupper():
        upper_count += 1
    if i.islower():
        lower_count += 1
print("Number of vowels: ",vowel_count)
print("Number of consonats: ",consonat_count)
print("Number of uppper: ",upper_count)
print("Number of lower: ",lower_count)
