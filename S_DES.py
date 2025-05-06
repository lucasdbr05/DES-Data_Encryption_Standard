class S_DES:
    def __init__(self, key: int):
        self.__key = key
        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        self.K1, self.K2 = self.generate_keys()

    def encrypt(self, data):
        pass 

    def decrypt(self, data):
        pass 
    
    def permutation10(self, data: int) -> int:
        bits, result = [0] * 10 ,[0] * 10
        ans:int = 0
        for i in range(10):
            bits[i] = 1 if data & (1 << i) else 0
        bits = bits[::-1]
        for i in range(10):
            result[i] = bits[self.P10[i]-1]
        result = result[::-1]
        for i in range(10):
            ans += result[i] << i 
        return ans

    def permutation8(self, data: int) -> int:
        bits, result = [0] * 10 ,[0] * 10
        ans:int = 0
        for i in range(10):
            bits[i] = 1 if data & (1 << i) else 0
        bits = bits[::-1]
        for i in range(8):
            result[i] = bits[self.P8[i]-1]
        result = result[7::-1]
        for i in range(8):
            ans += result[i] << i 
        return ans
    

    def round_shift(self, data: int, r: int) -> int:
        data = (data >> (5-r)) + (data << r)
        data = data & 0b11111
        return data   
    
    def generate_keys(self) -> tuple[int, int]:
        data = self.permutation10(self.__key)

        le, re = (data>>5 & 0b11111), (data & 0b11111)
        le, re = self.round_shift(le, 1), self.round_shift(re, 1)

        data = (le << 5) + re 
        K1 = self.permutation8(data)
        
        le, re = self.round_shift(le, 2), self.round_shift(re, 2)
        data = (le << 5) + re 

        K2 = self.permutation8(data)
        return (K1, K2)