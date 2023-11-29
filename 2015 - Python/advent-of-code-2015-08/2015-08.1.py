def convert_string(input_str):
    # Decode the string using unicode-escape encoding
    decoded_str = bytes(input_str, 'utf-8').decode('unicode-escape')

    # Remove non-printable characters
    printable_str = ''.join(char for char in decoded_str if char.isprintable())

    return printable_str


# Input string
input_string = "sjdivfriyaaqa\xd2v\"k\"mpcu\"yyu\"en"

# Convert and print the result
result = convert_string(input_string)
print(result)
