import secrets
import sys


def keygen():
    key_file_name = sys.argv[1]
    key_len = int(sys.argv[2])
    if not key_file_name[-4:] == ".txt":
        key_file_name = key_file_name + ".txt"

    key = secrets.token_bytes(key_len)

    key_file = open(key_file_name, "wb")
    key_file.write(key)
    key_file.close()

    print("Key generated!")


if __name__ == "__main__":
    keygen()
