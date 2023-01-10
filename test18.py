# VCOUNT() count the number of vowel, consonants, uppercase, lowercase and words
def VCOUNT(string):
    vc = cc = uc = lc = wc = 0
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i in vowel:
            vc += 1
        if i not in vowel:
            cc += 1
        if i.isupper():
            uc += 1
        if i.islower():
            lc += 1
        if i == ' ':
            wc += 1
    print('The numeber of vowel is: ',vc)
    print('The numeber of consonant is: ',cc)
    print('The numeber of uppercase is: ',uc) 
    print('The numeber of lowercase',lc)
    print('The number of words are: ',wc+1)
string = input("Enter the paragraph: ")
VCOUNT(string)
