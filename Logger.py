from pprint import pprint
class Logger:
    @staticmethod
    def start(is_from_user:bool) -> None:
        print("Options:")
        print()
        print(f"T: change input origin for {"user" if not is_from_user else "default"} inputs")
        print("0: Stop")
        print("1E: encrypt using S-DES")
        print("1D: decrypt using S-DES")
        print("2E: S-DES encryptation with ECB operation mode")
        print("2D: S-DES decryptation with ECB operation mode")
        print("3E: S-DES encryptation with CBC operation mode")
        print("3D: S-DES decryptation with CBC operation mode")
        

    @staticmethod
    def print_data(data:str, title:str =  None, _bin = False, _bin_len= None) -> None:
        if(title): print(title)
        if(_bin):
            numeric_data = data
            binary = bin(numeric_data)[2:]
            binary_size  = ((len(binary) //8) + (1 if len(binary)%8 > 0 else 0)) * 8
            binary_size = _bin_len if _bin_len else binary_size
            data =  {
                "binary": binary.zfill(binary_size),
                "hexadecimal": hex(numeric_data)[2:].zfill(binary_size//4)
            }
            pprint(data)
            print()
        else:
            print(data)
    