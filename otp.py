def popkey(length, keyfile):
    key = bytearray()
    with open(keyfile, "rb") as file:
        key = file.read()
    key = key[length:]
    with open(keyfile, "wb") as file:
        file.write(key)


def encrypt(message, keyfile):
    with open(keyfile, "rb") as file:
        key = file.read()
        ciphertext = b''.join([bytes([i ^ j])
                               for i, j in zip(message, key[:len(message)])])
    popkey(len(message), keyfile)
    return ciphertext


def decrypt(ciphertext, keyfile):
    with open(keyfile, "rb") as file:
        key = file.read()
        plaintext = ''.join([chr(i ^ j)
                             for i, j in zip(ciphertext, key[:len(ciphertext)])])
    popkey(len(ciphertext), keyfile)
    return plaintext
