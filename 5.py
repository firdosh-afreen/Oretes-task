def gcd(a, b):
    if (a == 0):
        return b 
    return gcd(b % a, a) 
 
def product(n, num, den):
    new_num = 1 
    new_den = 1 
    for i in range(n):
        new_num = new_num * num[i] 
        new_den = new_den * den[i] 
  
    GCD = gcd(new_num, new_den) 
     
    new_num = new_num / GCD
    new_den = new_den / GCD
     
    print(int(new_num),"/",int(new_den))
 
n = 3
num = [2, 4, 6]
den = [6, 5, 8]
product(n, num, den)
'''
import fractions
from decimal import Decimal
f1=fractions.Fraction(2,6)
f2=fractions.Fraction(4,5)
f3=fractions.Fraction(6,8)
print('{} * {} * {} = {}'.format(f1,f2,f3,f1*f2*f3))
'''


























