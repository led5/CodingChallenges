def makeAnagram(a, b):
    # Minimum deletions for a and b to be anagrams
    for ch in a:
        if ch in b: 
            b = b.replace(ch, '', 1)
            a = a.replace(ch, '', 1)
    return len(a) + len(b)