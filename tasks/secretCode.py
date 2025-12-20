import random

name = input("Enter your name: ")
randomLetters = "abcdefghijklmnopqrtuvwxyz"

def coding(name: str):
    randomThreeLetters = ""
    if len(name) >= 3:
        for _ in range(3):
            randomIdx = random.randint(0, len(randomLetters) - 1)
            randomThreeLetters += randomLetters[randomIdx]
        name = f"{randomThreeLetters}{name[1:] + name[0]}{randomThreeLetters}"
    else:
        name = name[::-1]
    return name


def decoding(secretCode: str):
    if len(name) >= 3:
        secretCode = secretCode[3:-3]
        secretCode = secretCode[-1:] + secretCode[:-1]
    else:
        secretCode = secretCode[::-1]
    return secretCode

secretCode = coding(name)
decode = decoding(secretCode)
print(secretCode)
print(decode)