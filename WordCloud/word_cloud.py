import html

#Open file
#Creates list which contains the text file

f = open('wonderland.txt', "r")

wholeStory = []

for line in f:
    excerpts = line.split()
    wholeStory += excerpts
    

#Open stopwords.txt
#Uses dictionary to count how many words in wordSpeech

mostFrequent = {}

for word in wholeStory:
    if word in mostFrequent: mostFrequent[word] +=1
    else: mostFrequent[word] = 1

        
#Reads stop words into list
#Loop over mostFrequent dictionary to remove stop words        
        
s = open('stopwords2.txt', "r")

stopList = []

for line in s:
    stopWord = line.split()
    stopList += stopWord
    
#print(stopList)
    
for stopWord in stopList:
     if stopWord in mostFrequent:
         del mostFrequent[stopWord]
        
print(mostFrequent)

#Converts frequent word and count in dictionary to font size

maximum = max(mostFrequent.values())
print(maximum)
#print(len(mostFrequent))

for word, size in mostFrequent.items():
     if size >= .8*maximum: 
         mostFrequent[word] = 42
     elif size >= .6*maximum:
         mostFrequent[word] = 38
     elif size >= .3*maximum:
         mostFrequent[word] = 34
     else:
         mostFrequent[word] = 30
        

# maximum = 24
# count = 291 


#Creates word cloud

def _main():
    cloudString = '' 
    for word,size in mostFrequent.items():
            cloudString += htmlhelper.make_HTML_word(word, size)
    #print(cloudString[0:100])
    outstring = htmlhelper.make_HTML_box(cloudString,700)
    f = open('cloud.html','w')
    f.write(outstring)
    f.close()
    #print(outstring)

if __name__ == '__main__':
    _main()
