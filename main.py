from S_DES import S_DES
from Operation_Modes import encrypt_sdes_cbc, encrypt_sdes_ecb

dado=S_DES(int("1010000010",2))
ans = dado.encrypt(int("10010111",2))
print(bin(dado.decrypt(ans))[2:].zfill(8))


print(encrypt_sdes_ecb(text="11010111011011001011101011110000",key=int("1010000010", base=2), ))
print(encrypt_sdes_cbc(text="11010111011011001011101011110000",key=int("1010000010", base=2), iv= int("01010101", base=2)))
