def encrypt(message):
    return None


def main():
    k = input("Enter keyfile name: ")
    m = input("Enter message: ")
    print("Encrypted: ", encrypt(m))

    """
    pt = b'hejhej'
    with open(key_file_name, "rb") as test:
        bs = test.read()
        print(type(bs), type(pt))
        ct = b''.join([bytes([i ^ j]) for i, j in zip(pt, bs[:len(pt)])])
        print("ct", ct, type(ct))
        dt = ''.join([chr(i ^ j) for i, j in zip(ct, bs[:len(ct)])])
        print("dt", dt)
    """


if __name__ == "__main__":
    main()
