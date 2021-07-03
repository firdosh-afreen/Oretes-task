def convert(str):
    n = len(str)
 
    
    for i in range(n):
        if str[i] >= 'a' and str[i] <= 'z':
            str[i] = chr(ord(str[i]) - 32)
 
        elif str[i] >= 'A' and str[i] <= 'Z':
            str[i] = chr(ord(str[i]) + 32)
 

if __name__ == "__main__":
    str = "Hi jUlian, hOW hAvE yOu Been?"
    str = list(str)
 
   
convert(str)
str = ''.join(str)
print(str)
