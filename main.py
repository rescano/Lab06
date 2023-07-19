# example input
# 12345555
# example output
# 45678888

# Rona Escano
def encode(code1):  # encoder - Rona Escano
    encoded = ''
    dcode = list(code1)
    for i in range(0, len(dcode)):
        value = str(int(dcode[i]) + 3)
        encoded = encoded + value
    return encoded

def decode(encoded):   # decoder - Ben Schiller
    decoded = ''
    dcode = list(encoded)
    for i in range(0, len(encoded)):
        value = str(int(dcode[i]) - 3)
        decoded = decoded + value
    return decoded


if __name__ == "__main__":  # main function - Rona Escano

    while True:
        # print Menu - Rona Escano
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))

        # encoder - Rona Escano
        if option == 1:
            code = input("Please enter your password to encode: ")
            encode = encode(code)
            print("Your password has been encoded and stored!")

        # decoder - Ben Schiller
        if option == 2:
            decode = decode(encode)
            print("The encoded password is", encode, "and the original password is", decode + ".")

        # exit program - Rona Escano
        if option == 3:
            exit()
