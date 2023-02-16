import string

PUNCTUATION = string.punctuation

def encrypt(s: str, shift: int) -> str:
    """
    Just chuck in opposite shift of original shift if you want to decrypt I'm not bothered to write it
    """
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


print(encrypt('xyZ', 1))