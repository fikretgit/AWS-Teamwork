def readFileToStr(filename):
  myFile = open(filename+".txt", "r")
  print(filename+".txt is opened")
  fileStr = myFile.read()
  myFile.close()
  print(filename+".txt is closed")
  return fileStr

def findEndSentIndex(myStr):
  endings = ["...", ".", ":", "!", "?"]
  idxFirstPunc = 10000 # some arbitrarily large number   
  for item in endings:
    if item in myStr:
      idx = myStr.index(item)
      if idx < idxFirstPunc:
        idxFirstPunc = idx
  return idxFirstPunc
    
def avrSentLen(myStr):
  lenSent = 0 # number of words in a sentence
  numSent = 0 # total number of sentences

  while len(myStr) > 0:
    endIndex = findEndSentIndex(myStr)   # find the end of the first sentence
    sent = myStr[:endIndex]             # retrieve the first sentence
    words = sent.split(" ")             # split the sentence into words
    lenSent += len(words)               # update the number of words
    numSent += 1                        # increment the number of  sentences
    myStr = myStr[endIndex+1:]          # discard the considered sentence
    if myStr[0:2] == "..":              # if the punc mark was "..."
      myStr = myStr[2:]                 # discard the remaining ".." in the beginning
      
  avrSentLen = lenSent / numSent        # calculate the average word lenght
  return avrSentLen 

# MAIN
text1 = readFileToStr("text1")
text2 = readFileToStr("text2")

avrSentLen1 = avrSentLen(text1)
avrSentLen2 = avrSentLen(text2)

print(avrSentLen1, avrSentLen2)

if avrSentLen1 > avrSentLen2:
  firstText = "Charles Dickens"
  secondText = "Hemingway"
else:
  firstText = "Hemingway"
  secondText = "Charles Dickens"

print("The first text belongs to ", firstText," and the second one belongs to ", secondText, ".")
