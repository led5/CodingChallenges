"""

Find the most common prefix of a given DNA string.

"""

import numbers 


def countCommonPrefix(strSeq, prefix):
    
    """ Take any sequence of strings, strSeq, and return the count of
        element strings that start with the given prefix.

        >>> countCommonPrefix(('ab', 'ac', 'ad'), 'a')
        3
        >>> countCommonPrefix(['able', 'baker', 'adam', 'ability'], 'ab')
        2
        >>> countCommonPrefix([], 'a')
        0
        >>> countCommonPrefix(['a', 'a', 'ab'], 'a')
        3
        >>> countCommonPrefix(['a', 'a', 'ab'], '')
        3
    """

    count = 0

    for element in strSeq:
        if element.startswith(prefix):
            count += 1
    return count 


def getNumbers(sequence):
    
    """ Take any sequence and return a list of all elements that are
        numbers.

        >>> getNumbers(range(10))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> getNumbers([1, 2.5, '3'])
        [1, 2.5]
        >>> getNumbers('abc123.4xyz')
        []
        >>> getNumbers((1, 2.5, complex(3, 4), '5'))
        [1, 2.5, (3+4j)]
        
    """
    ret = []

    for element in sequence:
        if isinstance(element, numbers.Number):
            ret.append(element)
    return ret 



def sumNumbers(sequence):
    
    """ Take any sequence and return the sum of all elements that are
        numbers. Non-numbers are ignored.

        >>> sumNumbers(range(10))
        45
        >>> sumNumbers([1, 2.5, '3'])
        3.5
        >>> sumNumbers('abc123.4xyz')
        0
        >>> sumNumbers((1, 2.5, complex(3, 4), '5'))
        (6.5+4j)
        
    """
    ret = getNumbers(sequence) 
    return sum(ret)
            

def dnaDigit(bp):
    
    """ Take a character (a string of length one) and return a
        0 for 'a', 1 for 'c', 2 for 'g', and 3 for 't'. For any
        other string, raise a ValueError. Capital or lowercase letters
        are acceptable.

        >>> dnaDigit('a')
        0
        >>> dnaDigit('C')
        1
        >>> dnaDigit('g')
        2
        >>> dnaDigit('t')
        3
        >>> dnaDigit('abc')
        Traceback (most recent call last):
            ...
        ValueError: only 'a', 'c', 'g', or 't' accepted
        >>> dnaDigit("")
        Traceback (most recent call last):
            ...
        ValueError: only 'a', 'c', 'g', or 't' accepted
    """
    
    bpMap = {'a': 0, 'c': 1, 'g': 2, 't': 3}

    try:
        ret = bpMap[bp.lower()]
        
    except KeyError:
        raise ValueError("only 'a', 'c', 'g', or 't' accepted")
    
    return ret

    
    
def bpFromDigit(digit):
    
    """ Inverse of dnaDigit.

        >>> bpFromDigit(3)
        't'
        >>> bpFromDigit(7)
        Traceback (most recent call last):
            ...
        ValueError: only 0, 1, 2, or 3 accepted
    """
    
    bpMap = {0: 'a', 1: 'c', 2: 'g', 3: 't'}           

    try:
        ret = bpMap[digit]
    except KeyError:
        raise ValueError("only 0, 1, 2, or 3 accepted") 
    return ret

    



def dnaNumber(bpSeq):
    
    """ Take a dna string, bpSeq, (a string of a's, c's, g's, and t's)
        and interpret that as a base-4 number using dnaDigit for each
        basepair. A ValueErorr is raised if there are any characters besides
        those accepted by dnaDigit.

        >>> dnaNumber('')
        0
        >>> dnaNumber('aaa')
        0
        >>> dnaNumber('t')
        3
        >>> dnaNumber('ca')
        4
        >>> dnaNumber('CAA')
        16
        >>> dnaNumber('cgt')
        27
        >>> dnaNumber('cggaattAGGTtttacgtactggatcaat')
        117360495799280451
        >>> dnaNumber('whatever')
        Traceback (most recent call last):
            ...
        ValueError: only 'a', 'c', 'g', or 't' accepted
        >>> dnaNumber(['c', 'g', 't'])  # should work for any sequence type
        27
    """
    previous = 0
    result = 0 
    
    for bp in bpSeq:
        result = dnaDigit(bp) + previous*4
        previous = result            
    return result




def chunks(sequence, chunkSize):
    
    """ Take any sequence and a chunk size, and return a list of the chunks
        from the given sequence.
        
        >>> chunks('cgtcgtcgtaaa', 3)
        [['c', 'g', 't'], ['c', 'g', 't'], ['c', 'g', 't'], ['a', 'a', 'a']]
        >>> chunks('cgtcgtcgtaaa', 5)
        [['c', 'g', 't', 'c', 'g'], ['t', 'c', 'g', 't', 'a'], ['a', 'a']]
        >>> chunks(range(7), 2)
        [[0, 1], [2, 3], [4, 5], [6]]
        >>> chunks(((1,2), ['a','b','c'], 'xyz'), 1)
        [[(1, 2)], [['a', 'b', 'c']], ['xyz']]
    """

    ret = []
    sequence2 = []
    
    for i in sequence:
        sequence2.append(i)
    for i in range(0, len(sequence2), chunkSize):
        ret.append(sequence2[i:i+chunkSize])

    return ret


def substringList(s, k):
    
    """ Takes a string, s, and and length, k, and returns a list of all
        the substrings in s of length k (including overlap).

        >>> substringList('abcdefg', 2)
        ['ab', 'bc', 'cd', 'de', 'ef', 'fg']
    """
    
    ret = []
    retString = ''

    for i in range(0, len(s) - k+1):
        retString = s[i:i+k]
        ret.append(retString)
        
    return ret 


def maxValue(d):
    
    """ Takes a dictionary d and returns the maximum element value and its
        corresponding key. Raises a TypeError if any of the values are not
        comparable to each other.

        >>> maxValue({'a': 12, 3: 45})
        (3, 45)
        >>> maxValue({}) is None
        True
        >>> maxValue({33: 34, -1: 600, 'xyz': 2000.4})
        ('xyz', 2000.4)
        >>> maxValue({1: 'abc', 2: 'xyz', 3: 'ghijkl'})
        (2, 'xyz')
        >>> maxValue({1:'a', 2:3})
        Traceback (most recent call last):
            ...
        TypeError: unorderable types: int() > str()
    """

    values = d.values()

    if len(values) == 0:
        return None

    maxValue = max(values)

    for i in d:
        try:
            if maxValue == d[i]:
                return i, maxValue
        except:
            raise TypeError("unorderable types: int() > str()")


def dnaMostCommon(bpSeq, k):
    
    """ Takes a sequence of dna base pairs, bpSeq, and a substring size, k,
        and returns the most common substring of length k in bpSeq and also
        the count.

        >>> dnaMostCommon('cccgggaaatatctgtttt', 1)
        ('t', 7)
        >>> dnaMostCommon('cgagttatgagacgacgacga', 3)
        ('cga', 4)
        >>> dnaMostCommon('ttttttt', 4)
        ('tttt', 4)
    """
  

    ret = {}

    subStrings = substringList(bpSeq,k)

    for i in subStrings:
        if i in ret:
            ret[i] += 1
        else:
            ret[i] = 1
    return maxValue(ret) 

    
    
    

