from htmlFunctions import makeHTMLword, makeHTMLbox 

# Creates list which contains the text file
f = open("wonderland.txt", "r")

wholeStory = []

for line in f:
    excerpts = line.split()
    wholeStory += excerpts

# Count how many words in wholeStory
mostFrequent = {}

for word in wholeStory:
    if word in mostFrequent: 
        mostFrequent[word] +=1
    else: 
        mostFrequent[word] = 1

        
# Loop over mostFrequent dictionary to remove stop words        
s = open("stopwords.txt", "r")

stopList = []

for line in s:
    stopWord = line.split()
    stopList += stopWord
      
for stopWord in stopList:
     if stopWord in mostFrequent:
         del mostFrequent[stopWord]
        
maximum = max(mostFrequent.values())
minimum = min(mostFrequent.values())

#Create word cloud
def _main():
    cloudString = '' 
    for word,size in mostFrequent.items():
             cloudString += makeHTMLword(word, size, maximum, minimum)
    outstring = makeHTMLbox(cloudString)
    f = open('cloud.html','w')
    f.write(outstring)
    f.close()
    

if __name__ == '__main__':
    _main()
