import time
import random
number = 0
index = 0
B = input("put in the encryption key")
B = int(B)
def Enter(password):
    if int(password)*int(password) == B:
        print("granted")
inp = input("guess or attack")
if inp == "guess":
    guess = input("whats your 4 digit guess")
    Enter(guess)
if inp == "attack":
    while number != B:
        number = index * index
        if number != B:
            index += 1
        if number == B:
            print(index)
            Enter(index)


