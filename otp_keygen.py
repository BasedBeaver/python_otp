import secrets
import sys


def keygen():
    key_file_name = sys.argv[1]
    key_lenght = int(sys.argv[2])
    if not key_file_name[-4:] == ".txt":
        key_file_name = key_file_name + ".txt"
    hex_key = secrets.token_hex(key_lenght)
    bit_len = len(hex_key)*4
    bit_key = str(bin(int(hex_key, 16)))[2:].zfill(bit_len)
    key_file = open(key_file_name, "w")
    key_file.write(bit_key)
    key_file.close()
    print("Key generated!")


if __name__ == "__main__":
    keygen()
