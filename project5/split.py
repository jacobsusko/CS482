# str = "34 3B 71 62 BA 9F 55 B8 D9 88 71 98 24 41 3E 4D A4 BD 1A E1 2C AE 2C FF 1D 4E 1A 9E 94 8A 4D 07 71 5D C6 1F EF 91 09 67 DA FA 37 96 11 E1 67 D6 3E A1 5E 58 0B 81 DD B2 AF 5D DE DE 9D 82 B3 72 36 86 A6 72 EA 3E 5A A0 21 4E 94 BF 51 12 BE FC B6 07 3D 51 36 CF 76 93 AB C6 6C 7B 5F C8 16 A2 11 C0 E6 87 9E AB 40 56 A4 B7 A5 20 44 BF B0 B7 5B 43 4A 02 19 09 1D B2 30 BB 15 CE 1C 97 D8 77 BC 42 87 14 93 85 D2 0A 7D C4 44 0E 82 35 3B C4 40 78 7A 59 A1 59 18 09 22 17 68 C0 FC 7A 5F 67 5B 2A B3 FC 53 BC E0 92 FF 0D 84 74 31 1F F5 16 4F 17 50 8D 95 51 06 F7 BC DA 15 05 76 B5 10 78 A4 A1 F1 45 F1 6E 78 2C 3A 01 4E 82 68 4F E8 12 69 DD 00 77 17 EC 95 76 BC 8C 43 C5 99 53 BA 86 4C 6B 46 4A 35 82 E1 10 EE 2A 73 4D 80 55 DC BC"
str = """A0 E2 57 8B 13 2D 3C 3B  92 1C BF BF 57 42 43 19 E9 34 6C BF 99 15 81 5F 71 18 12 97 A0 8F 8A F9 CE 07 73 B6 C7 FE D8 A2 2B 3E FC D0 D3 37 BF 3B C4 1E 5E 42 4A 21 00 83 9F F7 ED CC 8A 8E 60 06 7D 57 A3 8D 6E D5 69 1F 98 98 E0 AE C2 65 D5 1D 30 25 00 E8 99 69 9F 04 01 C4 81 34 C1 2D 13 A7 CC 5A B7 C8 5C 8E A4 29 23 98 E6 2B 6A 44 59 2E 31 F4 BE 7E 43 45 A5 05 4E AE 8C 4A 8F BA 6B 6D 2A 07 EB 82 8E FB CD E9 7B B1 5A AD 3F 5E 4F 7C 3F CE 79 7E 84 72 AD 34 8A BA 4A AA CE E0 FE 32 A2 7F F8 D7 FD 04 F1 EF 02 4A B3 2C 73 33 D3 96 D6 93 7D D9 A6 CA AF B3 F3 D6 FA AA 8E 77 38 D0 A7 78 B2 38 FE 50 D9 4F 5E 04 50 7C C7 B8 29 ED F7 8D 76 CA 89 71 F8 06 2D 72 67 F1 FA D4 B1 AA 08 34 C3 21 E7 97 21 6C 79 B8 29 AE D2 7D 68 CD"""
arr = str.split(" ")
str2 = "(byte) 0x" + ", (byte) 0x".join(arr)
print(str2)
byteArr = str2.split(" ")
print(byteArr)