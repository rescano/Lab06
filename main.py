# example input
# 12345555
# example output
# 45678888

# Rona Escano
def encode(code1):
    encoded = ''
    dcode = list(code1)
    for i in range(0, len(dcode)):
        value = str(int(dcode[i]) + 3)
        encoded = encoded + value
    return encoded


if __name__ == "__main__":

    while True:
        # print Menu
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))

        # encoder
        if option == 1:
            code = input("Please enter your password to encode: ")
            encode = encode(code)
            print("Your password has been encoded and stored!")

        # decoder
        if option == 2:
            pass

        # exit program
        if option == 3:
            exit()
