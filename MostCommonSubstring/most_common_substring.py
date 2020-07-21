"""
A function that finds and returns the most common sub-sequence in a
larger sequence of DNA. DNA is composed of a string of 'a', 'g', 'c', and 't's.

"""

def mostCommonK(dna, k):
    
    best = '' # the longest string
    bestCount = 0 # the highest frequency 
    
    for i in range(len(dna)-k+1):       
            canidate = dna[i:i+k]
            count = 1             
            for j in range(i+1, len(dna)-k+1):
                check = dna[j: j+k]
                if check == canidate:
                    count += 1
            if count > bestCount:
                best = canidate
                bestCount = count
                
    return (best, bestCount)

         
def mostCommonSubstring(dna, k, m):
    
     """ 
      Running: For example, mostCommonSubstring('gactctcagc', 2, 6) returns
     'ctc' since it occurs twice and is longer than 'ct' and 'tc' which each
      also occur twice, and all other substrings of length 2, 3, 4, 5, or 6
      only occur once. Note that the occurrences can overlap.
    """
     
     commonString = '' # most common string overall 
     highestCount = 0 # greatest frequency overall 
     
     for i in range(k,m):
            x, y = mostCommonK(dna, i) # best, bestCount 
            if y > highestCount:
                commonString = x
                highestCount = y
     return commonString 

def runMostCommonSubstring():
    
    filename = input("Please enter filename:")
    infile = open(filename, "r")
    dna = infile.read()
    mostCommonSubstring(dna, 2, 6)
    
runMostCommonSubstring()


            
            
            
    
    
                
                
        


        
    
        
        
        
