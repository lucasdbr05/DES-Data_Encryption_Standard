# DES - Data Encryption Standard

This project implements the S-DES (Simplified Data Encryption Standard) algorithm in Python, including support for ECB and CBC operation modes. S-DES is a didactic version of the DES algorithm, widely used for educational purposes to demonstrate the principles of symmetric-key block ciphers.

---

## 📖 About S-DES

S-DES is a symmetric-key block cipher that operates on 8-bit blocks of data using a 10-bit key. The algorithm consists of key generation, initial and inverse permutations, two rounds of substitution and permutation using S-boxes, and supports operation modes such as ECB and CBC for encrypting larger messages.

**Main Features:**
- S-DES encryption and decryption for 8-bit blocks
- Key generation from a 10-bit key
- ECB (Electronic Codebook) and CBC (Cipher Block Chaining) operation modes

---

## 🚀 How to Run


  ```bash
  python main.py
   ```
**Usage:**
   - When you run the program, a menu will be displayed with the following options:
     - **1E**: Encrypt a single 8-bit block using S-DES.
     - **1D**: Decrypt a single 8-bit block using S-DES.
     - **2E**: Encrypt a binary message using S-DES in ECB mode.
     - **2D**: Decrypt a binary message using S-DES in ECB mode.
     - **3E**: Encrypt a binary message using S-DES in CBC mode (with a fixed IV).
     - **3D**: Decrypt a binary message using S-DES in CBC mode (with a fixed IV).
   - You can toggle between user input and default input files by pressing `T` at the menu.
   - To stop the program, enter `0`.
   - After each operation, press `y` to return to the menu.

---

## 🛠️ Project Structure

```
.
├── S_DES.py              # S-DES algorithm implementation
├── Operation_Modes.py    # ECB and CBC operation modes
├── Logger.py             # Logger utility for user interaction
├── main.py               # Main interface and menu
├── inputs/               # Example input files for testing
└── README.md             # This file
```

---



## 👨‍💻 Authors

<table>
  <tr>
    <td align="center"><a href="https://github.com/lucasdbr05" target="_blank"><img style="border-radius: 50%;" src="https://github.com/lucasdbr05.png" width="100px;" alt="Lucas Lima"/><br /><sub><b>Lucas Lima - 231003406</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/pedro-neris" target="_blank"><img style="border-radius: 50%;" src="https://github.com/pedro-neris.png" width="100px;" alt="Pedro Neris"/><br /><sub><b>Pedro Neris - 231018964</b></sub></a><br /></td>
  </tr>
</table>