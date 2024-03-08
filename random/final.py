
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
    if (b%n) > (n/2) and b > 0:
        return b-n 
    if (b%n) > (n/2) and b < 0:
        return b+n 
    return b%n


def mods(hx, n):
    hx = str(hx)

    coefficeient_pattern = r"([-+]?\d*)\*?x\^?\d*"
    coefficients = re.findall(coefficeient_pattern, hx)

    for index, element in enumerate(coefficients):
        if coefficients[index] == '':
            coefficients[index] = '1'

    # print(coefficients)

    mods_coefficents = [mods_coef(int(coeff), n) for coeff in coefficients]
    hx_final = hx
    for coeff in coefficients:
        hx_final = hx_final.replace(coeff + '*x', str(mods_coefficents.pop(0)) + '*x', 1)

    hx_f = ''
    for num in hx_final.split(' + '):
        if num == '':
            return hx_f
        if num[0] != '0':
            hx_f += num + ' + '

    
    try:
        hx_f = hx_f[:-5]
        split = hx.split(" ")
        lastNum = mods_coef(int(split[len(split) - 1]), n)
        hx_f += str(lastNum)
    except ValueError:
        hx_f = hx_f[:-3]
        pass
    
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
# use norm().n() to get shortest vectors and check those
# For each row calculate norm and for 5 smallest calculate and then check
# print(res)
# print("")
negativeRes = []

for array in res:
    negativeArr = []
    for num in array:
        negativeArr.append(num)
    negativeRes.append(negativeArr)

    negativeArr = []
    for num in array:
        negativeArr.append(num * -1)
    negativeRes.append(negativeArr)

# for arr in negativeRes:
#     print(arr)


finals = {}

i = 0
for row in res:
    finals[i] = row.norm().n()
    i += 1

shortest = min(finals.values())

# order finals
# sorted = dict(sorted(finals.items(), key=lambda item: item[1]))
# for x in sorted.items():
#     print(x[1])

short = []
for key, val in finals.items():
    if val == shortest:
        short.append(key)


new_finals = {}

negatives = []
for k in short:
    new_finals[k] = finals[k]

    # creates the primes of all the shortest vectors
    # negativeArr = []
    # for num in res[k]:
    #     negativeArr.append(num * -1)
    # negatives.append(negativeArr)
    
# for num in negatives:
#     print(num)
    
keys = []
for num in new_finals.keys():
    keys.append(num)

final_indexes = []
ind = 0
for number in new_finals.keys():
    final_indexes.append(keys[ind] * 2)
    final_indexes.append(keys[ind] *2 + 1)
    ind += 1

# print(new_finals.keys())
# print(final_indexes)


for index in final_indexes:
    f_coefficents = negativeRes[index][:23]
    g_coefficents = negativeRes[index][23:]

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
    # print(fx)

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
    # print(hx)
    # print()


    cx = encrypt(ogx1)
    lastResult = decrypt(ogx1, cx)
    results = mods(lastResult, 31)
    results = mods(results, 3)

    if (results == expectedDecrypt):
        print('fx:', fx)
        print('Gx:', Gx)
        print(results)
        

    # if (index == 25): # the correct index
    #     print('*************************')
    #     print(index)
    #     cx = encrypt(ogx1)
    #     lastResult = decrypt(ogx1, cx)
    #     print(lastResult)
    #     print()
    #     results = mods(lastResult, 31)
    #     print(results)
    #     print()
    #     results = mods(results, 3)
    #     print(results)