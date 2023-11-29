import hashlib

number = 1
inp = "bgvyzdsv"

while True:
    inputCount = f"{inp}{number}"
    encoded = hashlib.md5(inputCount.encode()).hexdigest()

    if encoded[:5] == "00000":
        break

    number += 1

print(number)
