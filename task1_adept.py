word1 = list(input('Word 1: '))
word2 = list(input('Word 2: '))

if len(word1) > len(word2):
    for i in range(len(word1) - len(word2)):
        word2.append(0)
elif len(word1) < len(word2):
    for i in range(len(word2) - len(word1)):
        word1.append(0)

# Checking which letters are common
same_letters = []
common_letters = []
diff_case_letters = []

for i in range(len(word1)):
    letter = word1[i]
    
    # Common letter
    if letter in word2:
        word1_freq, word2_freq = word1.count(letter), word2.count(letter)

        # Same letter in same place
        if letter == word2[i]:
            same_letters.append(letter)
            same_letters.append(letter)
            word1_freq -= 1
            word2_freq -= 1

        # Stop counting if already in common_letters
        if letter in common_letters:
            word1_freq, word2_freq = 0, 0
            
        for j in range(word1_freq + word2_freq):
            common_letters.append(letter)
     
    # Not bothering with testing if the letter is 0        
    try:
        # Different case letter
        if letter.isupper() and letter.lower() in word2:
            word1_freq, word2_freq = word1.count(letter.lower()), word2.count(letter.lower())
            for j in range(word1_freq + word2_freq):
                diff_case_letters.append(letter)

        if letter.islower() and letter.upper() in word2:
            word1_freq, word2_freq = word1.count(letter.upper()), word2.count(letter.upper())
            for j in range(word1_freq + word2_freq):
                diff_case_letters.append(letter)

    except:
        pass

# Calculation 
total_len = len(word1) + len(word2)
similarity = (len(same_letters) + 0.5*len(common_letters) + 0.33*len(diff_case_letters)) / total_len

# Output
print(f'Same letters: {same_letters}')
print(f'Common letters: {common_letters}')
print(f'Different case letters: {diff_case_letters}')
if similarity >= 1:
    print('100%')
else:
    print(f"{similarity * 100}%")