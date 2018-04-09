"""
===================   TASK 3   ====================
* Name:  Roulette
*
* Write a script that will simulate casino game -
* Roulette but only for red, black or green (zero)
* fields. On each run, the script should return
* 'red', 'black' or '0'.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""
'''
PRVI NACIN: 
import random

palo_na_broj = random.randrange(0,37)

if palo_na_broj == 0:
    print('0')
    
elif palo_na_broj in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
    print('red')
    
else:
    print('black')
'''

import random
bacanje = random.random() #daje nam broj u opsegu od 0 do 1


if bacanje <= 18/37:   #vjerovatnoca da padne na crveno polje je: broj crvenih(18) kroz ukupan broj mogucih(37)
    print('red')       # pa cemo postaviti da ako nam bacanje padne u tom opsegu, onda smo na crvenom polju

elif bacanje <= 2*(18/37):   #vjerovatnoca da padne na crno polje je jednaka vjerovatnoci za crveno polje
    print('black')           # pa cemo na sledecem opsegu, koji je iste duzine kao prvi opseg, postaviti crno polje

else:                    # u suprotnom je palo na nulu
    print('0')
