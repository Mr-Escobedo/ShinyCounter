#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

def rotate(key:int = 0) -> "int":
    '''Rotates a list of numbers that are strings'''
    numbers = "123456789"
    key = abs(key) % len(numbers)
    return numbers[key:] + numbers[:key]

def encrypt(count:int = 0, key: int = 0) -> int:
    '''Encrypts a number using Caesar encryption'''
    table = str.maketrans("123456789", rotate(key))
    return int(str(count).translate(table)) + key

def decrypt(count:int = 0, key: int = 0) -> int:
    '''Decrypts a number using Caesar encryption'''
    table = str.maketrans(rotate(key), "123456789")
    return int(str(count - key).translate(table))


if __name__ == "__main__":
    a = 1234567890
    for key in range(101):
        try:
            b = encrypt(a, key)
            c = decrypt(b, key)
            assert a == c
        except AssertionError:
            print("Key: {}".format(key))
            print("Original: {}".format(a))
            print("Encrypted: {}".format(b))
            print("Decrypted: {}".format(c))
