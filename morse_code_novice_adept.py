import winsound
import time

def morse_to_text(s:str):
    MORSE_CODE_DICT = {
        'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-'
    }

    MORSE_CODE_DICT_reversed = {value:key for key, value in MORSE_CODE_DICT.items()}

    text = ''

    for morse in s:
        text += MORSE_CODE_DICT_reversed[morse]

    return text


morse = input('Input morse code: ').split()
print(morse)

print(morse_to_text(morse))
