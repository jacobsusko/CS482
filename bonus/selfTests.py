string_76 = "-60*x^78 - 64*x^77 + 58*x^76 - 104*x^75 - 49*x^74 - 58*x^73 + x^72 - 12*x^71 + 80*x^70 + 9*x^69 + 8*x^68 - 63*x^67 - 19*x^66 - 80*x^65 - 49*x^64 + 38*x^63 - 11*x^62 - 13*x^61 - 104*x^60 - 5*x^59 - 40*x^58 - 19*x^57 + 30*x^56 + 78*x^55 - 30*x^54 + 93*x^53 + 30*x^52 - 26*x^51 + 59*x^50 + 41*x^49 - 103*x^48 - 99*x^47 - 102*x^46 - 48*x^45 - 16*x^44 - 83*x^43 - 70*x^42 - 9*x^41 + 6*x^40 + 86*x^39 - 2*x^38 - 44*x^37 - 76*x^36 + 36*x^35 + 59*x^34 - 20*x^33 - 92*x^32 - 100*x^31 + 102*x^30 - 44*x^29 - 8*x^28 - 75*x^27 + 104*x^26 + 77*x^25 + 41*x^24 - 62*x^23 - 68*x^22 - 27*x^21 + 32*x^20 + 12*x^19 - 42*x^18 + 87*x^17 - 96*x^16 + 23*x^15 - 46*x^14 - 52*x^13 + 15*x^12 + 90*x^11 - 53*x^10 - 17*x^9 - 11*x^8 - 63*x^7 + 34*x^6 + 56*x^5 + 84*x^4 + 87*x^3 - 74*x^2 + 19*x - 37"
arr = string_76.split(" ")

new_arr = []
new_arr.append(arr[0])
print(arr[0])
for x in range(1, (len(arr) + 1) // 2):
    print(arr[(x * 2) - 1] + "" + arr[(x * 2)])
    new_arr.append(arr[(x * 2) - 1] + "" + arr[(x * 2)])

print(new_arr)

remove_arr = []
for x in new_arr:
    if x[0] == '+' and x[1] != 'x':
        remove_arr.append(x[1:])
    elif x[0] == '+' and x[1] == 'x':
        remove_arr.append("1*" + x[1:])
    elif x[0] == '-' and x[1] != 'x':
        remove_arr.append(x)
    elif x[0] == '-' and x[1] == 'x':
        remove_arr.append("-1*" + x[2:])
    
split = []
for x in remove_arr:
    num = x.split("*")
    split.append(num[0])

# remove_power_arr = []
# for x in remove_arr:
    
