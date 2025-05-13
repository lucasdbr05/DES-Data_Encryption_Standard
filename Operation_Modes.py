from S_DES import S_DES



def format_bin (x: str) -> str:
    return bin(x)[2:].zfill(8)

def padding(x:str) -> str:
    padding_size = (8-(len(x)%8))%8
    return x + ('0' * padding_size if padding_size else '')

def encrypt_sdes_ecb(text: str, key: int) -> str:
    """
        Encrypt a given text using the Simplified DES (S-DES) algorithm in ECB mode.
        Args:
            text (str): The input text to be decrypted. It should be a string of characters.
            key (int): The encryption key used for decryption, represented as a 16-bit integer.
        Returns:
            str: the ciphertext resulting in ECB mode encryptation
    """
    # Initialize the S-DES instance with the provided key
    s_des = S_DES(key)
    text = padding(text)
    blocks = []
    for i in range(0, len(text), 8):
        block = int(text[i: i+8], base=2)
        # Encrypt each block using S-DES
        data = s_des.encrypt(block)
        blocks.append(data)

    # Combine all encrypted blocks into a single binary string
    return "".join(format_bin(block) for block in blocks)


def decrypt_sdes_ecb(text: str, key: int) -> str:
    """
        Decrypt a given text using the Simplified DES (S-DES) algorithm in ECB mode.
        Args:
            text (str): The input text to be decrypted. It should be a string of characters.
            key (int): The decryption key used for decryption, represented as a 16-bit integer.
        Returns:
            str: the ciphertext resulting in ECB mode decryptation
    """
    # Initialize the S-DES instance with the provided key
    s_des = S_DES(key)
    text = padding(text)
    blocks = []

    for i in range(0, len(text), 8):
        block = int(text[i: i+8], base=2)
        # Decrypt each block using S-DES
        data = s_des.decrypt(block)
        blocks.append(data)

    # Combine all decrypted blocks into a single binary string
    return "".join(format_bin(block) for block in blocks)

def encrypt_sdes_cbc(text: str, key: int, iv: int) -> str:
    """
        Encrypt a given text using the Simplified DES (S-DES) algorithm in CBC mode.
        Args:
            text (str): The input text to be decrypted. It should be a string of characters.
            key (int): The encryption key used for decryption, represented as a 16-bit integer.
            iv (int): Initialization vector used in the CBC process.
        Returns:
            str: the ciphertext resulting in CBC mode encryptation
    """
    # Initialize the S-DES instance with the provided key
    s_des = S_DES(key)
    next_xor = iv 

    text = padding(text)
    blocks = []
    for i in range(0, len(text), 8):
        block = int(text[i: i+8], base=2)

        block ^= next_xor
        
        data = s_des.encrypt(block) # Encrypt each block using S-DES
        next_xor = data             # Update next value to xor

        blocks.append(data)

    # Combine all encrypted blocks into a single binary string
    return "".join(format_bin(block) for block in blocks)


def decrypt_sdes_cbc(text: str, key: int, iv: int) -> str:
    """
        Decrypt a given text using the Simplified DES (S-DES) algorithm in CBC mode.
        Args:
            text (str): The input text to be decrypted. It should be a string of characters.
            key (int): The decryption key used for decryption, represented as a 16-bit integer.
            iv (int): Initialization vector used in the CBC process.
        Returns:
            str: the ciphertext resulting in CBC mode decryptation
    """
    # Initialize the S-DES instance with the provided key
    s_des = S_DES(key)

    blocks = []
    next_xor = iv
    text = padding(text)
    
    for i in range(0, len(text), 8):
        block = int(text[i: i+8], base=2)
        
        data = s_des.decrypt(block) # Decrypt each block using S-DES
        data ^= next_xor 
        next_xor = block            # Update next value to xor

        blocks.append(data)

    # Combine all decrypted blocks into a single binary string
    return "".join(format_bin(block) for block in blocks)

