import winsound
import wave

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


audio = wave.open('Morse_test_file.wav', 'rb')

length = audio.getnframes()

data_list = []

for frame in range(length):
    audiodata = audio.readframes(1)
    data_list.append(audiodata.decode()) # Produces an error idk what happened
print(data_list)

audio.close()    