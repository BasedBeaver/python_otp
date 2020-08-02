import otp


def main():
    key = input("Enter keyfile name: ")
    message = input("Enter message: ").encode("utf-8")

    ciphertext = otp.encrypt(message, key)

    file = open("ciphertext", "wb")
    file.write(ciphertext)
    file.close()


if __name__ == "__main__":
    main()
