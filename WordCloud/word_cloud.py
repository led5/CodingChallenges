import html

# Creates list which contains the text file

f = open("wonderland.txt", "r")

wholeStory = []

for line in f:
    excerpts = line.split()
    wholeStory += excerpts
    

# Count how many words in wordSpeech

mostFrequent = {}

for word in wholeStory:
    if word in mostFrequent: mostFrequent[word] +=1
    else: mostFrequent[word] = 1

        
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

for word, size in mostFrequent.items():
     if size >= .8*maximum: 
         mostFrequent[word] = 42
     elif size >= .6*maximum:
         mostFrequent[word] = 38
     elif size >= .3*maximum:
         mostFrequent[word] = 34
     else:
         mostFrequent[word] = 30
        


#Creates word cloud

def _main():
    cloudString = '' 
    for word,size in mostFrequent.items():
            cloudString += htmlhelper.make_HTML_word(word, size)
    outstring = htmlhelper.make_HTML_box(cloudString,700)
    f = open('cloud.html','w')
    f.write(outstring)
    f.close()

if __name__ == '__main__':
    _main()
