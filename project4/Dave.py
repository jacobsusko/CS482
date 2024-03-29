
import re
from sage.all_cmdline import *

def encrypt(originalx1):
    ##############################################
    ########### NTRU ENCRYPTION ##################
    ##############################################
    ###
    ### PLAINTEXT
    ###
    # print ('\n++++++++++ ENCRYPTION BEGINS ++++++++++')
    mx_str = 'x^15 - x^12 + x^7 - 1'
    mx = R(mx_str)
    # print ('Plaintext m(x) = ', mx_str)

    #
    # Random polynomial for encryption
    #
    rx_str = 'x^19 + x^10 + x^6 - x^2'
    rx = R (rx_str)
    # print ('Random r(x) = ', rx_str)

    cx = rx * lastrem + mx
    lastq2, lastrem2 = cx.quo_rem(originalx1)
    # print ('\nCiphertext (needs to manually mods 31) = ', lastrem2)
    return cx

def decrypt(originalx1, cx):
    ##############################################
    ########### NTRU DECRYPTION ##################
    ##############################################
    # print ('\n++++++++++ DECRYPTION BEGINS ++++++++++')
    ax = fx * cx
    lastq3, lastrem3 = ax.quo_rem(originalx1)
    # print ('STEP 1: cleartext ax (needs to manually mods 31) = ', lastrem3)

    # print ('\nSTEP 2: needs to manually calculate ax mods p')
    return lastrem3


def mods_coef(b, n):
    if   -(n // 2) <= b <= (n // 2): # if b is in the range
        return b
    if   -(n // 2) <= b%n <= (n // 2): # if b%n is in the range
        return b%n
    if b%n == 0: 
        return 0
    
    if (b%n) > (n//2) and b > 0:
        return (b%n)-n
    elif (b%n) <= (n//2) and b > 0:
        return b-n
    
    if (b%n) > (n//2) and b < 0:
        return b+n
    elif (b%n) <= (n//2) and b < 0:
        return (b%n)


def mods(hx, n):
    hx = str(hx)

    coefficeient_pattern = r"([-+]?\d*)\*?x\^?\d*"
    coefficients = re.findall(coefficeient_pattern, hx)

    for index, element in enumerate(coefficients):
        if coefficients[index] == '':
            coefficients[index] = '1'

    mods_coefficents = [mods_coef(int(coeff), n) for coeff in coefficients]

    hx_final = hx
    for coeff in coefficients:
        hx_final = hx_final.replace(coeff + '*x', str(mods_coefficents.pop(0)) + '*x', 1)
    
    split = hx.split(" ")
    lastNum = split[len(split) - 1]
    lastNumLength = len(str(lastNum))
    if not('x' in lastNum):
        hx_final = hx_final[:(-lastNumLength)] + str(mods_coef(int(lastNum), n)) # does the mod for the coeff with no x
    
    hx_f = ''
    for num in hx_final.split(' + '):
        if num == '':
            return hx_f
        if num[0] != '0':
            hx_f += num + ' + '

    hx_f = hx_f[:-3] # removes ending " + "

    return hx_f


_sage_const_31 = Integer(31); _sage_const_3 = Integer(3); _sage_const_23 = Integer(23)
_sage_const_2 = Integer(2); _sage_const_22 = Integer(22); _sage_const_5 = Integer(5)
_sage_const_21 = Integer(21); _sage_const_7 = Integer(7); _sage_const_20 = Integer(20)
_sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18)
_sage_const_17 = Integer(17); _sage_const_15 = Integer(15); _sage_const_16 = Integer(16)
_sage_const_9 = Integer(9); _sage_const_13 = Integer(13); _sage_const_1 = Integer(1)
_sage_const_11 = Integer(11); _sage_const_4 = Integer(4); _sage_const_10 = Integer(10)
_sage_const_8 = Integer(8); _sage_const_6 = Integer(6); _sage_const_12 = Integer(12); _sage_const_0 = Integer(0)

p = _sage_const_3
q = _sage_const_31
N = _sage_const_23

p2 = _sage_const_3
q2 = _sage_const_31
p3 = _sage_const_3
q3 = _sage_const_31

h = - _sage_const_2*x**_sage_const_22 + _sage_const_5*x**_sage_const_21 + _sage_const_7*x**_sage_const_20 + _sage_const_14*x**_sage_const_19 + _sage_const_5*x**_sage_const_18 - _sage_const_3*x**_sage_const_17 + _sage_const_15*x**_sage_const_16 + _sage_const_2*x**_sage_const_15 - _sage_const_2*x**_sage_const_14 + _sage_const_9*x**_sage_const_13 - _sage_const_1*x**_sage_const_12 - _sage_const_14*x**_sage_const_11 - _sage_const_4*x**_sage_const_10 - _sage_const_1*x**_sage_const_9 - _sage_const_5*x**_sage_const_8 + _sage_const_5*x**_sage_const_7 - _sage_const_7*x**_sage_const_6 + _sage_const_9*x**_sage_const_5 + _sage_const_13*x**_sage_const_4 - _sage_const_15*x**_sage_const_3 + _sage_const_11*x**_sage_const_2 - _sage_const_9*x + _sage_const_10
R = PolynomialRing(GF(q), 'x', names=('x',)); (x,) = R._first_ngens(1)

expectedDecrypt = '1*x^15 + -1*x^12 + x^7 + -1'

breakingntru_23 = matrix(ZZ, 46, [
 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20,
 0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12,
 0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23,
 0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15,
 0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12,
 0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30,
 0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5,
 0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,
 0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19, 10,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12, 19,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8, 12,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,  8,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,  3,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26, 25,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14, 26,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28, 14,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24, 28,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1, 28, 14, 26, 25,  3,  8, 12, 19, 10,  9, 16, 10,  3, 20, 11,  5, 30, 12, 15, 23, 12, 20, 24,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31,  0,
 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 31])

res = breakingntru_23.LLL()
negativeRes = []

# formats the indexes as the normal matrix row, then its negative. So it alternates between normal and its prime
for array in res:
    negativeArr = []
    for num in array:
        negativeArr.append(num)
    negativeRes.append(negativeArr)

    negativeArr = []
    for num in array:
        negativeArr.append(num * -1)
    negativeRes.append(negativeArr)

finals = {}

i = 0
for row in res:
    finals[i] = row.norm().n()
    i += 1

shortest = min(finals.values())

short = []
for key, val in finals.items():
    if val == shortest:
        short.append(key)


new_finals = {}

negatives = []
for k in short:
    new_finals[k] = finals[k]
    
keys = []
for num in new_finals.keys():
    keys.append(num)

final_indexes = []
ind = 0
for number in new_finals.keys():
    final_indexes.append(keys[ind] * 2)
    final_indexes.append(keys[ind] *2 + 1)
    ind += 1

for index in final_indexes:
    f_coefficents = negativeRes[index][:N]
    g_coefficents = negativeRes[index][N:]

    degree = 0

    # Need to mods the coefficents other than that is as expected

    pow = _sage_const_0
    fx = _sage_const_0

    for c in f_coefficents:
        fx += c*(x**pow)
        pow += _sage_const_1
    pow = _sage_const_0
    Gx = _sage_const_0

    for c in g_coefficents:
        Gx += c*(x**pow)
        pow += _sage_const_1

    gx = Gx * p

    # Code to calculate fqx | was taken from stinson-program that was provided
    x1 = x**N - _sage_const_1
    ogx1 = x1
    x2 = fx
    t1 = _sage_const_0
    t2 = _sage_const_1
    s1 = _sage_const_1
    s2 = _sage_const_0

    while x2.degree() >= _sage_const_0:
        q, newx = x1.quo_rem(x2)
        x1 = x2
        x2 = newx
        newt = t1 - t2*q
        news = s1 - s2*q
        t1 = t2
        t2 = newt
        s1 = s2
        s2 = news

    x1inverse = inverse_mod(x1, q)
    fqx = t1 * x1inverse

    hx = fqx * gx
    lastq, lastrem = hx.quo_rem(ogx1)  # lastrem always ends up the same

    cx = encrypt(ogx1)
    lastResult = decrypt(ogx1, cx)
    results = mods(lastResult, q2)
    results = mods(results, p2)
    results = mods(results, p2)

    # print()
    # print("************************************")
    # print()
    # print(results)

    if (results == expectedDecrypt):
        # print('fx:', fx)
        # print('Gx:', Gx)
        # print()
        fx = mods(fx, q2)
        Gx = mods(Gx, q2)
        print('fx:', fx)
        print('Gx:', Gx)
        print()

        gx = mods(R(str(Gx)) * p2, q2)
        fx = mods(R(str(fx)), q2)

        # print('fx:', fx)
        # print('gx:', gx)
        # print()

        pow = _sage_const_0

        # Code to calculate fqx | was taken from stinson-program that was provided
        x1 = x**N - _sage_const_1
        ogx1 = x1
        x2 = R(fx)
        t1 = _sage_const_0
        t2 = _sage_const_1
        s1 = _sage_const_1
        s2 = _sage_const_0

        while x2.degree() >= _sage_const_0:
            q2, newx = x1.quo_rem(x2)
            x1 = x2
            x2 = newx
            newt = t1 - t2*q2
            news = s1 - s2*q2
            t1 = t2
            t2 = newt
            s1 = s2
            s2 = news

        x1inverse = inverse_mod(x1, q2)
        fqx = t1 * x1inverse

        hx = fqx * R(gx)
        lastq, lastrem = hx.quo_rem(ogx1)
        print("Returns to public key: " + str(mods(lastrem, q3)))
        break
        