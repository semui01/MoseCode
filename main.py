# ------------------ create morse code dictionary --------------------#
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}
# ------------------------Encoding -------------------------------------#
def encoding(message):
    code = ''
    for letter in message:
        if letter != ' ':
            code += MORSE_CODE_DICT[letter] + ' '
        else:
            # code += '/'
            code += ' '
    print(code)
# ---------------------Decoding -------------------------------------#
def decoding(message):
    message += ' '
    decode = ''
    morse_code = ''
    for letter in message:
        if letter != ' ':
            i = 0
            morse_code += letter
        else:
            i += 1
            if i == 2 :
                decode += ' '
            else:
                decode += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_code)]
                morse_code = ''
    print(decode.capitalize())  # return a string with the first character in the capital.

# ----------------------------------main------------------------------#
message = input('Please enter your message:').upper()
if message[0] in list(MORSE_CODE_DICT.keys())[:36]:
    encoding(message)
else:
    decoding(message)












