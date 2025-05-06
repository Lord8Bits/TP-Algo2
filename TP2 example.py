def exponentiation_rapide(x: int, n: int):
    print(x)
    if n == 1: #Base case 1
        return x
    if n == 0: # Base case 2
        return 1
    if n % 2 == 0:
        return exponentiation_rapide(x**2, n//2) # 
    if n > 2:
        return x * exponentiation_rapide(x**2, (n-1)//2) # exponentiation_rapide(5, 8) --> 5 * exponentiation_rapide(5**2, 1) --> 5 * 5**2

# #def exponentiation(nombre, puissance):
#     prod = 1

#     for _ in range(puissance): # exponentiation(5, 3) --> prod = prod * 5 --> prod = prod * 5 --> prod = prod * 5
#         print(prod)
#         prod = prod * nombre
#     return prod


#base 2: 
# 0 = 0
# 1 = 1
# 2 = 10
# 3 = 11
# 4 = 100
# 5 = 101
# 6 = 110
# 7 = 111
# 8 = 1000
# 9 = 1001
# 10 = 1010 = [1,0,1,0]
# 11 = 1011
# 12 = 1
# 9009 | 1
#+  1 1
#------
# 9 0 1 0
    
# 1001 | 1
#+   1
#_____
# 1 0 1 0 

# 1 0 1 1 | 1
#+      1
#________
# 1 1 0 0

def base2(x: int) -> list:
    
    if x == 0:
        return [0]
    if x == 1:
        return [1]
    return base2(x//2) + [x % 2] 

def base10(binary):

    if isinstance(binary, str):
        binary = [int(b) for b in binary]

    if isinstance(binary, int):
        binary = [int(b) for b in str(binary)]

    bit_length = len(binary)-1

    column = [2**(bit_length-i) for i in range(bit_length+1)]

    somme = 0

    for i in range(bit_length+1):
        if binary[i]:
            somme += column[i]
    return somme

def base10_recursive(binary):
    
    if isinstance(binary, str):
        binary = [int(b) for b in binary]

    if isinstance(binary, int):
        binary = [int(b) for b in str(binary)]
    
    if len(binary) == 1:
        return binary[0]
    return binary[0] * (2**(len(binary)-1)) + base10_recursive(binary[1:])



#[256,128,64,32,16,8,4,2,1]
#[1]
#128+ 0+ 32+ 0+ 0 + 4 + 2 + 0 = 166