def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
 
def countVowels(str):
    count = 0
    for i in range(len(str)):
        if isVowel(str[i]):
            count += 1
    return count
 
str = "this is awesome here"
print(countVowels(str))
