# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:28:05 2020

@author: Furcas
"""

num1 = 9 
num2 = 18 
class Art:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.base = []
    def bin_formarter(self, znak1, znak2, vivot1, vivot2):
        interface = '{}9 -- {} \n{}18 --  {} \n  bin format'
        print( interface.format(znak1, vivot1, znak2, vivot2))
    def binPlus(self):
        return self.bin_formarter(' ', ' ', bin(self.num1)[2:], bin(self.num2)[2:])
    
    def binMinus(self):
        return self.bin_formarter('-', '-', bin(self.num1), bin(self.num2))
    
angel = Art(num1, num2)

angel2 = Art(-9, -28)

#angel.binPlus()
#angel2.binMinus()

snum = '00000000'
snum2 = '00000000'
def twos_complement(n, bits=32):
    mask = (1 << bits) - 1
    if n < 0:
        n = ((abs(n) ^ mask) + 1)
    return n & mask
 
#print(twos_complement(-9, 8))  

def zap(num1):
    #snum = '00000000'
    alert = 8 - len(bin(num1)[2:])
    if num1 < 0:
        lord = '1'
        alert-1
        num1 = abs(num1)
        
    else:
        lord = ''

    for i in range(alert):
        lord+='0'
    
    
    #for i in range(len(snum)-1, 0, -1):
       
            

    return lord+bin(num1)[2:]
def zapforMP(num1):
    #snum = '00000000'
    alert = 12 - len(bin(num1)[2:])
    if num1 < 0:
        lord = '1'
        alert-1
        num1 = abs(num1)
        
    else:
        lord = ''

    for i in range(alert):
        lord+='0'
    
    
    #for i in range(len(snum)-1, 0, -1):
       
            

    return lord+bin(num1)[2:]

def reverse(num):
    
   
    war = ''
    
    for i in num:
        
        if i == '1':
            war += '0'
        else:
            war += '1'
           
    return war
def obrzap(num1):
    if num1 > 0:
        
        return zap(num1)
    else:
        return '1'+reverse(zap(num1))[1:]
     



def binsum(a, b):
    a = int(a, 2)
    b = int(b, 2)
    return zap(int(format(a|b)))

def dopkod(num1):
    if num1 < 0:
        
        return reverse(zap(abs(num1)))[:7]+'1'
        
    else:
        return zap(num1)
   


def obrsum(num1, num2):
    a1 = int(num1, 2)
    b1 = int(num2, 2)
    return (a1+b1+1) & 32
#print(binary_sum("-0b1001", "0b10010"))
def binAdd(x, y):
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    y = y.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len-1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1       

    if carry !=0 : result = '1' + result
    
    if len(result.zfill(max_len)) > 8:
        return binAdd(str(result.zfill(max_len))[1:], '00000001')
    return result.zfill(max_len)

def mno(a, b):
    a = list(reversed(list(map(int, a))))
    b = list(reversed(list(map(int, b))))
     
    lena = len(a)
    lenb = len(b)
     
    c = [0 for i in range(lena)]  # для переполнения
    c = [0 for i in range(lena + 1)]
    p = False  # вариант с переполнением
     
    for i, bita in enumerate(a):
        bitb = b[i]
     
        add = bita + bitb + c[i]
        if add < 2:
            c[i] = add
        else:
            c[i] = 0
            c[i + 1] = 1
            if i < lena - 1:
                c[i+1] = 1
            else:
                p = True
    c = list(reversed(c))
    print(p)
    return int(''.join(map(str, c)), 2)
def binadd2(num1, num2, target):
    
    if target == 0:
        
        if num1 and num2 < 0:
            ark = binAdd(zap(abs(num1)), zap(abs(num2)))
            
            return '1' + ark[1:]
        
        

def binary_exps(n):
    L = list(bin(n)[2:])
    L.reverse()
    L = [i for i,c in enumerate(L) if c == '1']
    return L

def mainLogic(x, y):
    if y > x:  x,y = y,x
    result = 0
    L = binary_exps(y)
    for e in L:
        result += x << e
    return result
def multiply(x,y):
    
    
    if x < 0 and y > 0:
        return '1' + zapforMP(mainLogic(x, y))[1:]
    elif x > 0 and y < 0:
        return '1' + zapforMP(mainLogic(x, y))[1:]
    elif x < 0 and x < 0:
        return zapforMP(mainLogic(abs(x), abs(y)))
    else:
        return zapforMP(mainLogic(x, y))
'''
def binary_addition( a, b ):
"""
Binary addition.

:param a: the first operand - a tuple of bits
:param b: the second operand - a tuple of bits
:type a: tuple
:type b: tuple
:return: the sum, as a tuple of bits
:rtype: tuple
"""

# first, ensure that the 2 arrays have the same number of bits,
# by filling in with 0s on the left of the shortest operand
diff = len(a)-len(b)

if diff > 0:
    # concatenating a tuple of size <diff> with tuple b (all elements are 0s)
    b = ((0,) * diff) + b   
elif diff < 0:
    # concatenating a tuple of size <-diff> with tuple a (all elements are 0s)
    a = ((0,) * (-diff)) + a 

c = 0
s = [0] * (len(a)+1)
for j in reversed(range(0,  len(a))):
        d = (a[j] + b[j] + c) // 2
        s[j+1] = (a[j] + b[j] + c) - 2*d
        c = d
s[0] = c

# removing unneeded 0s on the left
if s[0] == 0:
    s.remove(0)

return tuple(s)

def shift_left(a,n):
   ...
   #
   if not isinstance(a, tuple): return ()
   return a + (0,) * n       
            
def binary_multiplication(a, b):
    ...
    # initialize a null tuple of same size as a for the final sum
    s = (0,) * len(a)
    # take a copy of a for the intermediary products
    m = a[:]
    for i in reversed(range(len(b))):
        if b[i] != 0:     # when digit is one, add the intermediary product
            s = binary_addition(s, m)
        m = shift_left(m, 1)  # shift one per digit in b
    return s        
'''
print('прямой код +\+, +\-, -\+, -\-')
print('', zap(9), zap(18), '9 and 18' )
print('', zap(-9), zap(-18), '-9 and -18' )
print(binAdd(zap(9), zap(18)), '= 9+18')
print(binAdd(zap(9), zap(-18)), '= 9-18')
print(binAdd(zap(-9), zap(18)), '= 18-9')
print(binadd2(-9, -18, 0), '= -18-9')
print("обратный код +\+, +\-, -\+")
print(obrzap(9), obrzap(18), '9 and 18')
print(obrzap(-9), obrzap(-18), '-9 and -18')
print(binAdd(obrzap(9), obrzap(18)), '= 9+18')
print(binAdd(obrzap(-9), obrzap(18)), '= -9+18')
print(binAdd(obrzap(9), obrzap(-18)), '= 9-18')
print(binAdd(obrzap(-9), obrzap(-18)), '= -9-18')
print("доп код код +\+, +\-, -\+, -\-")
print('', dopkod(9), dopkod(18), '9 and 18' )
print('', dopkod(-9), dopkod(-18), '-9 and -18' )
print(binAdd(dopkod(9), dopkod(18)),  '= 9+18')
print(binAdd(dopkod(9), dopkod(-18)), '= -9+18')
print(binAdd(dopkod(-9), dopkod(18)), '= 9-18')
print(binAdd(dopkod(-9), dopkod(-18)), '= -9-18')
print('18*9=162')
print('PR_KOd', '', multiply(9,18))
print('OBR_KOd', multiply(9,18))
print('DOP_KOd', multiply(9,18))
print("\\\\\\\'" )
print('-18*9=-162')
print('PR_KOd', '', multiply(-9,18))
print('OBR_KOd', '1' + reverse(multiply(-9,18)[1:]))
print('DOP_KOd', '1' + reverse(multiply(-9,18)[1:11] + '1'))
print('18*-9=-162')
print('PR_KOd', '', multiply(-9,18))
print('OBR_KOd', '1' + reverse(multiply(-9,18)[1:]))
print('DOP_KOd', '1' + reverse(multiply(-9,18)[1:11] + '1'))
print('-18*-9=162')
print('PR_KOd', '', multiply(9,18))
print('OBR_KOd', multiply(9,18))
print('DOP_KOd', multiply(9,18))

print('9/18 = 0.5 (0.1)')


#print( binary_multiplication((0,0,0,0,1,0,0,1), (0,0,0,1,0,0,1,0)))
    
