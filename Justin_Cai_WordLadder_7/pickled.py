import pickle

def putFileIntoArray():
   myFile = open("dictionary.txt")
   wordList = []
   for line in myFile:
      wordList.append(line.rstrip("\n"))
   return wordList

def findNeighbors(word, wordList):
   neighbors = []
   for w in wordList:
      count = 0
      for index in range(0, 6):
         if(word[index] != w[index]):
            count = count + 1
      if(count == 1):
         neighbors.append(w)
   return neighbors

def createDictionary(wordList):
   dictionary = {}
   for str in wordList:
      dictionary[str] = findNeighbors(str, wordList)
   return dictionary
      
def putDictIntoFile(dictionary):
   dictFile = open("wordhash.txt", "wb")
   pickle.dump(dictionary, dictFile)
   dictFile.close()

def main():
   wordList = putFileIntoArray()
   dictionary = createDictionary(wordList)
   print(dictionary)
   putDictIntoFile(dictionary)
   print("Done!")
   
main()
