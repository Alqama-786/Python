import random
import inquirer

message = input("Enter your message: ")
question = inquirer.prompt([inquirer.List('operation', message="What operation you wanted to do?", choices=["Coding","Decoding"])])
operation = question["operation"]
randomLetters = "abcdefghijklmnopqrtuvwxyz"

def coding(message: str):
    randomThreeLetters = ""
    if len(message) >= 3:
        for _ in range(3):
            randomIdx = random.randint(0, len(randomLetters) - 1)
            randomThreeLetters += randomLetters[randomIdx]

        message = f"{randomThreeLetters}{message}{randomThreeLetters}"
    else:
        for _ in range(10):
            randomIdx = random.randint(0, len(randomLetters) - 1)
            randomThreeLetters += randomLetters[randomIdx]

        message = f"{randomThreeLetters}{message}{randomThreeLetters}"
    return message[::-1]


def decoding(secretCode: str):
    if len(message) >= 3:
        secretCode = secretCode[3:-3]
        secretCode = secretCode[::-1]
        secretCode = secretCode[-1] + secretCode[:-1]
    else:
        secretCode = secretCode[10:-10]
        secretCode = secretCode[::-1]
        secretCode = secretCode[-1] + secretCode[:-1]
    return secretCode

if operation.rstrip().lower() == "coding":
    print(f"Coded: {coding(message)}")
elif operation.rstrip().lower() == "decoding":
    print(f"Decoded: {decoding(message)}")
else:
    raise ValueError("Please enter a valid operation.")