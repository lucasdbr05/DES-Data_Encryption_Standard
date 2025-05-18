from os import system
from Logger import Logger
from S_DES import S_DES
from Operation_Modes import encrypt_sdes_ecb, decrypt_sdes_ecb, encrypt_sdes_cbc, decrypt_sdes_cbc

def get_input(from_user: bool, file_path: str = None) -> str:
    if(from_user):
        return input()
    else:
        content = open(file_path, 'r', encoding="utf-8").read()
        print(content)
        return content

def do_command(data: str, from_user: bool) -> None:
    if (data == "1E"):
        Logger.print_data("Type S-DES key (binary):")
        key = int(get_input(from_user, "inputs/1_E_key.txt"), base=2)
        Logger.print_data("Type binary data to be encrypted (data must have 8 bits):")
        text = int(get_input(from_user, "inputs/1_E_text.txt"), base=2 )
        s_des = S_DES(key)
        Logger.print_data(s_des.encrypt(text), "S-DES encryption result", True)
    elif (data == "1D"):
        Logger.print_data("Type S-DES key (binary):")
        key = int(get_input(from_user, "inputs/1_D_key.txt"), base=2)
        Logger.print_data("Type binary data to be decrypted (data must have 8 bits):")
        text = int(get_input(from_user, "inputs/1_D_text.txt"), base=2)
        s_des = S_DES(key)
        Logger.print_data(s_des.decrypt(text), "S-DES decryption result", True)
    elif (data == "2E"):
        Logger.print_data("Type S-DES key (binary):")
        key = int(get_input(from_user, "inputs/2_E_key.txt"), base=2)
        Logger.print_data("Type data to be encrypted (binary):")
        text = get_input(from_user, "inputs/2_E_text.txt")
        text = encrypt_sdes_ecb(text, key)
        Logger.print_data(int(text, base=2), "Final ECB operation message encryption", True)
    elif (data == "2D"):
        Logger.print_data("Type S-DES key (binary):")
        key = int(get_input(from_user, "inputs/2_D_key.txt"), base=2)
        Logger.print_data("Type data to be decrypted (binary):")
        text = get_input(from_user, "inputs/2_D_text.txt")
        text = decrypt_sdes_ecb(text, key)
        Logger.print_data(int(text, base=2), "Final ECB operation message decryption", True)
    elif (data == "3E"):
        Logger.print_data("Type S-DES key (binary):")
        key = int(get_input(from_user, "inputs/3_E_key.txt"), base=2)
        Logger.print_data("Type the initialization vector (iv):")
        iv = int(get_input(from_user, "inputs/3_D_iv.txt"), base=2)
        Logger.print_data("Type data to be encrypted (binary):")
        text = get_input(from_user, "inputs/3_E_text.txt")

        text = encrypt_sdes_cbc(text, key, iv)
        Logger.print_data(int(text, base=2), "Final CBC operation message encryption", True)
    elif (data == "3D"):
        Logger.print_data("Type S-DES key (binary):")
        key = int(get_input(from_user, "inputs/3_D_key.txt"), base=2)
        Logger.print_data("Type the initialization vector (iv):")
        iv = int(get_input(from_user, "inputs/3_D_iv.txt"), base=2)
        Logger.print_data("Type data to be decrypted (binary):")
        text = get_input(from_user, "inputs/3_D_text.txt")

        text = decrypt_sdes_cbc(text, key, iv)
        Logger.print_data(int(text, base=2), "Final CBC operation message decryption", True)
    else:
        Logger.print_data("Command not found :(")
    
    Logger.print_data("Press y to continue")
    while(not input()): continue
    

if __name__ == "__main__":
    inputs_from_user = False
    while (True):
        Logger.start(inputs_from_user)
        option = input()
        system("clear")

        if(option=="T"):
            inputs_from_user = not inputs_from_user
            continue
        if(option== '0'):
            break
        
        do_command(option, inputs_from_user)
        system("clear")