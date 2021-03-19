from collections import Counter 

# A string is valid if all characters of the string appear the same number of times. 
# It is also valid if you can remove just 1 character at 1 index in the string and the remaining 
# characters will occur the same number of times. 

def valid_string(s):
    # Count occurrences of characters in s
    char = Counter(s)
    # Tally occurrences of each char
    freq = Counter(char.values())

    if (len(freq) == 1): # All characters appear same number of times 
        return "YES"
    elif len(freq) == 2: 
        ch_max = max(freq.keys())
        ch_min = min(freq.keys())
        if ((ch_max - ch_min) == 1 and freq[ch_max] == 1): # Check if removal of 1 character possible to make valid str 
            return "YES"
        elif (ch_min == 1 and freq[ch_min] == 1):
            return "YES"
    return "NO"
        