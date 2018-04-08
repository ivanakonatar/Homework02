"""
===================   TASK 2   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def gcd(a,b):   #f-ja racuna najveci zajednicki djelilac dva cijela broja

    if not isinstance(a,int) and not isinstance(b,int): #ispitujemo da li su unijeti brojevi iz skupa cijelih brojeva
        return -1

    a1 = abs(a)
    b1 = abs(b)
    z = abs(a1-b1)

    if z == 0:      #primjenjujemo Euklidov algoritam
        return b1
    else:
        return gcd(z,min(a1,b1))

def main():

    print(gcd(-120, 24))

main()
