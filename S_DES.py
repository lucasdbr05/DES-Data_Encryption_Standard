class S_DES:
    def __init__(self, key: int):
        self.__key = key
        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        self.P4 = [2, 4, 3, 1]
        self.S0 = [
            [1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 3, 2]
        ]
        self.S1 = [
            [0, 1, 2, 3],
            [2, 0, 1, 3],
            [3, 0, 1, 0],
            [2, 1, 0, 3]
        ]
        self.permutation_table = [2, 6, 3, 1, 4, 8, 5, 7]
        self.inverse_permutation_table = [4, 1, 3, 5, 7, 2, 8, 6]
        
        self.K1, self.K2 = self.generate_keys()

    def encrypt(self, data):
        data= self.initial_permutation(data)
        
        data= self.function_k(data, self.K1)
        data= self.sw(data)

        data= self.function_k(data, self.K2)
        data= self.inverse_permutation(data)
        
        return data


    def decrypt(self, data:int):
        data= self.initial_permutation(data)
        
        data= self.function_k(data, self.K2)
        data= self.sw(data)

        data= self.function_k(data, self.K1)
        data= self.inverse_permutation(data)
        
        return data
        

    def permutation10(self, data: int) -> int:
        bits, result = [0] * 10 ,[0] * 10
        value:int = 0
        for i in range(10):
            bits[i] = 1 if data & (1 << i) else 0
        bits = bits[::-1]
        for i in range(10):
            result[i] = bits[self.P10[i]-1]
        result = result[::-1]
        for i in range(10):
            value += result[i] << i 
        return value

    def permutation8(self, data: int) -> int:
        bits, result = [0] * 10 ,[0] * 10
        value:int = 0
        for i in range(10):
            bits[i] = 1 if data & (1 << i) else 0
        bits = bits[::-1]
        for i in range(8):
            result[i] = bits[self.P8[i]-1]
        result = result[7::-1]
        for i in range(8):
            value += result[i] << i 
        return value
    

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
    

    def initial_permutation(self, data:int)->int:
        binary_string = bin(data)[2:]
        list_binary_string = list(binary_string.zfill(8))
        result = ['0'] * 8
        for i in range(len(list_binary_string)):
            result[i] = list_binary_string[self.permutation_table[i]-1]
        
        return int("".join(result), base=2)


    def inverse_permutation(self, data:int)->int:
        binary_string = bin(data)[2:]
        list_binary_string = list(binary_string.zfill(8))
        result = ['0'] * 8
        for i in range(len(list_binary_string)):
            result[i] = list_binary_string[self.inverse_permutation_table[i]-1]
        
        return int("".join(result), base=2)


    def expanded_permutation(self, data:int)->int:
        binary_string = bin(data)[2:]
        list_binary_string = list(binary_string.zfill(4))
        ans = [0]*8
        ans[0] = list_binary_string[3]
        ans[1] = list_binary_string[0]
        ans[2] = list_binary_string[1]
        ans[3] = list_binary_string[2]
        ans[4] = list_binary_string[1]
        ans[5] = list_binary_string[2]
        ans[6] = list_binary_string[3]
        ans[7] = list_binary_string[0]

        return int("".join(ans), base=2)


    def split_8bits_block(self, data: int) -> tuple[int, int]:
        LE = (data >> 4) & 0xF
        RE = (data) & 0xF
        return (LE, RE)
    

    def permutation4(self,data:int)->int:
        binary_string = bin(data)[2:]
        list_binary_string = list(binary_string.zfill(4))
        for i in range(len(list_binary_string)):
            list_binary_string[i] = (list_binary_string[i], self.P4[i])
        list_binary_string.sort(key=lambda x: x[1])
        for i in range(len(list_binary_string)):
            list_binary_string[i] = list_binary_string[i][0]
        return int("".join(list_binary_string), base=2)
    

    def sw(self, data:int)-> int:
        binary_string = bin(data)[2:]
        list_binary_string = list(binary_string.zfill(8))
        temp_list= list_binary_string[4:]
        for i in range (4):
            temp_list.append(list_binary_string[i])
        return int("".join(temp_list), base=2)


    def function_k(self, data:int, key:int)-> int:
        LE, RE = self.split_8bits_block(data)
        new_data_left= self.expanded_permutation(LE)
        new_data_right= self.expanded_permutation(RE)
        new_data_right ^= key
        
        le,re= self.split_8bits_block(new_data_right)
        s0= self.convert_with_S_box(le, self.S0)
        s1= self.convert_with_S_box(re, self.S1)
        new_data= (s0 << 2) + s1
        new_data= self.permutation4(new_data)
        new_data= LE ^new_data
        new_data = (new_data<<4) | RE
        
        return new_data


    def convert_with_S_box(self, data: int, box: list[list[int]]) -> int:
        row = ((data>>2) & 0b10) | (data & 0b1)
        col = ((data & 0b0110) >>1 )
        return box[row][col]
    