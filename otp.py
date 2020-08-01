def encrypt(message):
    return None


def string_to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def main():
    k = input("Enter keyfile name: ")
    m = input("Enter message: ")
    bits = string_to_bits(m)
    print("Encrypted: ", encrypt(m))


if __name__ == "__main__":
    main()
