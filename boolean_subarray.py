def find_substring(s: str, substring_length: int):
    # Spit it straight back out if it is the substring
    if len(s) == substring_length:
        return s
    
    # Loop through and check all substrings
    for i in range(len(s) - substring_length + 1):
        substring = s[i : i+substring_length] # Non-inclusive for end
        if substring.count('1') == substring_length/2:
            return substring

    # If not found, do the whole thing again with decreased substring length
    return(find_substring(s, substring_length-2))


array = input('Input binary separated by space: ').split()

zeros = array.count('0')
ones = array.count('1')

if zeros < ones:
    substring_length = zeros * 2
elif ones <= zeros:
    substring_length = ones * 2

print(find_substring(array, substring_length))
