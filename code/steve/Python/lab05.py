import string

letters = list(string.ascii_lowercase)

code_decode = input("If you want to create a code enter 1, if you want to decode a message enter 2: ")

if code_decode == "1":

    code = input("Please enter your secret code:  ")
    letter_mover = int(input("Please enter the number of letters you want shifted in the code: "))
    if letter_mover > 25:
        shift = letter_mover % 26
    else:
        shift = letter_mover
    decode = 26 - shift

    code = list(code)

    letters2 = letters[shift:] + letters[:shift]

    cipher2 = dict(zip(letters, letters2))

    coded_word = []

    coded_word.append(code)
    replaced_list = [x if x not in cipher2 else cipher2[x] for x in code]

    print(f"your code is: {''.join(replaced_list)}.")

else:
    decode = input("Please enter the message you would like to decode: ")
    origin_code = int(input("Please enter the number the message was coded with: "))
    decoder = 26 - origin_code
    decode = list(decode)

    letters2 = letters[decoder:] + letters[:decoder]

    cipher3 = dict(zip(letters, letters2))

    coded_word = []

    coded_word.append(decode)
    decoded_message = [x if x not in cipher3 else cipher3[x] for x in decode]

    print(f"your code is: {''.join(decoded_message)}.")


