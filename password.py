import random
from random import randrange
import sys

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "%&!?"
numbers = "1234567890"
letters = "abcdefghijklmnopqrstuvwxyz"

lengthOk = False
passwordLength = 0

if len(sys.argv) == 1:
    while not lengthOk:
        print("Usage: password.py or password.py <number>")
        passwordLength = int(input("Passoword length [4-]? "))
        if passwordLength >= 4:
            lengthOk = True
else:
    passwordLength = int(sys.argv[1])

maxNonLetterCount = passwordLength // 4

uppercaseCount = randrange(maxNonLetterCount) + 1
specialCount = randrange(maxNonLetterCount) + 1
numberCount = randrange(maxNonLetterCount) + 1
letterCount = passwordLength - uppercaseCount - specialCount - numberCount

passwordChars = []

for _ in range(uppercaseCount):
    passwordChars.append(uppercase[randrange(len(uppercase))])

for _ in range(specialCount):
    passwordChars.append(special[randrange(len(special))])

for _ in range(numberCount):
    passwordChars.append(numbers[randrange(len(numbers))])

for _ in range(letterCount):
    passwordChars.append(letters[randrange(len(letters))])

random.shuffle(passwordChars)
print("".join(passwordChars))
