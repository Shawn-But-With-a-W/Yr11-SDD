import string

PUNCTUATION = string.punctuation

def decrypt(s: str, shift: int) -> str:
    output = []
    for letter in s:
        if letter == ' ' or letter in PUNCTUATION:
            output.append(' ')
        else:
            new_ascii = ord(letter) + shift
            try:
                int(letter)
            except:
                # Is a letter
                if letter.isupper():
                    if new_ascii > 90:
                        new_ascii = new_ascii - 90 + 64
                elif letter.islower():
                    if new_ascii > 122:
                        new_ascii = new_ascii - 122 + 96
            else:
                if new_ascii > 57:
                    new_ascii = new_ascii - 57 + 47
            
            output.append(chr(new_ascii))

    return ''.join(output)


s = input('Provide a Caesar cipher encrypted string: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

for shift in range(0, 27):
    decrypted_s = decrypt(s, shift).split()

    valid_sentence = True
    for word in decrypted_s:
        valid_word = False
        for vowel in vowels:
            if vowel in word:
                valid_word = True
                
        if valid_word == False:
            valid_sentence = False

    if valid_sentence == True:
        print(' '.join(decrypted_s))

    

