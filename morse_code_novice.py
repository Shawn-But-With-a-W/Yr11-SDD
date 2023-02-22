import winsound
import time

def text_to_morse(s:str):
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

    morse = ''

    for letter in s.upper():
        if letter == ' ':
            morse += ' '*2
        else:
            morse += MORSE_CODE_DICT[letter]
            morse += ' '

    return morse


text = input('Input a text: ')

print(text_to_morse(text))

for symbol in text_to_morse(text):
    if symbol == '-':
        winsound.Beep(3000, 1200)
        time.sleep(2)
    elif symbol == '.':
        winsound.Beep(3000, 400)
    elif symbol == ' ':
        time.sleep(0.4)