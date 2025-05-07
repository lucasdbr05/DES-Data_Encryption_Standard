from S_DES import S_DES

dado=S_DES(int("1010000010",2))
ans = dado.encrypt(int("10010111",2))
print(bin(ans)[2:].zfill(8))