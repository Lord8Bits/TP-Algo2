from math import floor, log2
import numpy as np

# EX 1:
def exponentiation(x, n) -> int:
    if n == 0:
        return 1
    if n == 1:
        return x
    if not n % 2:
        return exponentiation(x**2, n/2)
    if n > 2 and n % 2:
        return x*exponentiation(x**2, (n-1)/2)

def naive_exponentiation(x, n) -> int:
    prod = 1
    for _ in range(n):
        prod *= x
    return prod

# EX 2:
def base2_recursive(n) -> list:
    """
    Retourne la représentation binaire de n sous forme de liste de bits.

    Arguments
    ----------
    n : int
        The decimal number to convert
    
    return : list
        The binary version in list form
    
    """

    if len(list(str(n))) == 1 and n == 0:
        return [0]
    if n == 0:
        return [] # Je ne sais pas comment gerer le cas pour n = 0 donc j'ai cree une version iterative car je suis mieux en iteration.
    else:
        return base2_recursive(n//2) + [n%2]


def base2_iterative(decimal) -> list:
    """
    Retourne la représentation binaire de n sous forme de liste de bits.

    Arguments
    ----------
    decimal : int
        The decimal number to convert
    
    return : list
        The binary version in list form
    
    """
    # Edge Cases:
    if decimal == 0:
        return [0]
    if decimal == 1:
        return [1]
    
    # Power of 2 numbers which are always in the form of 10^n:
    bit_length = floor(log2(decimal)+1)
    if decimal == 1 << (bit_length-1):
        return [1]+[0]*(bit_length-1)
    
    # We use 'columns' to identify which power of 2 (eg. ...,32,16,8,4,2,1) is smaller to substract the decimal until it equals to 0:
    # We will use the same << bit shift operator to find every power of 2 numbers with a limit of bit_lenght - 1 because 2^5 != 16 == 10000
    column = [1 << (bit_length - 1 - i) for i in range(bit_length)]
    binary = [0]*bit_length

    for i in range(bit_length):

        if decimal >= column[i]:
            binary[i] = 1
            decimal -= column[i]

        if decimal == 0:
            break
    return binary
    # Took me a whole day to finally understand how bitwise operators work 🥲, but hey at least its 6x faster than recursive. plus recursive cannot handle big numbers.

def base10(binary) -> int:
    if isinstance(binary, str):
        binary = list(binary)
    if isinstance(binary, int):
        binary = list(map(int, str(binary)))
    if not binary:
        return 0
    
    bit_length = len(binary)
    selected_bit = binary[0]
    binary = binary[1:]

    return selected_bit*(2**(bit_length-1)) + base10(binary)

#print(base2_recursive(6))
#print(base10(base2_recursive(6)))
#print(base10(1111))

# EX 3:
def taille_list(L) -> int:
    """
    Retourne le nombre d'elements dans une liste

    Arguments
    ----------
    L : list 

    Return : int
        Le nombre d'elements
    
    """
    if isinstance(L, str):
        L = list(L)
    if not L:
        return 0
    L = L[1:]
    return 1 + taille_list(L)

def sum_liste(L) -> float:
    """
    Retourne la somme de toutes elements d'une liste

    Arguments
    ----------
    L : list (int, float)
        liste a calculer la somme 
    Return : float
        La somme de toute les nombres de la liste
    
    """   
    if not L:
        return 0
    element = L[0]
    L = L[1:]
    return float(element + sum_liste(L))

def aff_liste_inv(L) -> list:
    """
    Retourne la liste en sens inverse

    Arguments
    ----------
    L : list
        Liste a inverser
    Return : list
        Liste inverse
    
    """ 
    if not L:
        return []
    dernier_element = L[-1]
    L = L[:-1]
    return [dernier_element] + aff_liste_inv(L)

# EX 4:
def strcpy(src: str, dest : str) -> str:
    """
    Copies a str to another str

    Arguments
    ----------
    src : str
        The string to be copied (src short for source)
    dest : str
        The string that will be pasted on
    return : str
        New string with copied src
    
    """

    if not src:
        return ''
    char = src[0]
    src = src[1:]
    return dest + char + strcpy(src, '')

def strcpm(ch1 : str, ch2 : str) -> int:
    """
    Compare les deux chaines
    
    Arguments
    ----------
    ch1: str

    ch2: str

    return : int
        Si sont egaux retourne 0 sinon 1
    """
    if not ch1 and not ch2:
        return 0
    letter = ch1[0]
    count1 = ch1.count(letter)
    count2 = ch2.count(letter)
    if count1 == count2:
        for _ in range(count1):
            index1 = ch1.rindex(letter)
            index2 = ch2.rindex(letter)
            ch1 = ch1[:index1] + ch1[index1+1:]
            ch2 = ch2[:index2] + ch2[index2+1:]
        return strcpm(ch1, ch2)
    else:
        return 1

def anagramme(str1, str2) -> bool:
    """
    Une anagramme est un mot ou une expression obtenu(e) en
    réarrangeant toutes les lettres d’un autre mot ou d’une autre expression,
    sans en ajouter ni en retirer. 

    Arguments
    ----------
    str1 et str2 : str
        Les chaines a comparer
    return: bool
        retourne True si c'est un anagramme sinon False
    """
    if strcpm(str1, str2):
        return False
    else:
        return True

# EX 5:
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)
