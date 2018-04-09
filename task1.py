"""
===================   TASK 1   ====================
* Name: Rectangular To Polar
*
* Write a function `rect2polar` that will convert
* rectangular complex number notation to polar
* notation. 
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
import math

def rect2polar(x,y):   # (x,y) odgovara kompleksnom zapisu z=x+iy
                       # r-moduo, r=|z|=(x**2+y**2)**1/2
                       # θ-argument, θ=arctg(y/x)
                       # polarni zapis : z = r(cos θ + isin θ), cije su polarne koordinate (r,θ)

    r = round(math.sqrt(x**2 + y**2),1)

    if x>0:
        fi=math.atan(y/x)

    elif x<0:
        fi=math.pi + math.atan(y/x)

    else:
        if y>0:
            fi=math.pi/2

        else:
            fi=-(math.pi/2)

    fi = round(fi * (180 / math.pi)) #pretvaramo radijane u stepene
    return str(r) + "*" + "(cos" + str(fi) + "° + isin" + str(fi) + "°)" # mozemo zapisati i kao odgovarajuce polarne koordinate(r,fi)

def main():

     print(rect2polar(-3,2))

main()