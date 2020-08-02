import secrets
import sys


def keygen():
    key_len = int(sys.argv[1])

    key = secrets.token_bytes(key_len)

    key_file = open("enc_key", "wb")
    key_file.write(key)
    key_file.close()

    key_file = open("dec_key", "wb")
    key_file.write(key)
    key_file.close()

    print("Key generated!")


if __name__ == "__main__":
    keygen()
