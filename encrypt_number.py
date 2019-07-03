#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

def rotate(key:int = 0) -> ['int']:
    '''Rotates a list of numbers that are strings'''
    numbers = [str(x) for x in range(10)]
    key = abs(key)
    while key >= 10:
        key -= 10
    return numbers[key:] + numbers[:key]

def encrypt(count:int = 0, key: int = 0) -> int:
    '''Encrypts a number using Caesar encryption'''
    rotated = rotate(key)
    table = str.maketrans(str([str(x) for x in range(10)]), str(rotated))
    count = str(count)
    return int(count.translate(table))

def decrypt(count:int = 0, key: int = 0) -> int:
    '''Decrypts a number using Caesar encryption'''
    rotated = rotate(key)
    table = str.maketrans(str(rotated), str([str(x) for x in range(10)]))
    count = str(count)
    return int(count.translate(table))
    


if __name__ == "__main__":
    L = encrypt()
