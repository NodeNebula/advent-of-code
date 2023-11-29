import hashlib

number = 1
inp = "bgvyzdsv"

while True:
    inputString = f"{inp}{number}"

    encoded = hashlib.md5(inputString.encode()).hexdigest()

    if encoded.startswith("000000"):
        break

    number += 1
    print(number)

print(number)
