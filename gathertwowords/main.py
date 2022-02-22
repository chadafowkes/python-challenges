def mainMenu():
  print()
  print("Please enter your first word...")
  word1Input = input()

  print("Please enter your second word...")
  word2Input = input()

  if createWordWithTwoWords(word1Input, word2Input):
    print()
    print("The word " + word1Input + " can be formed from the word " + word2Input)
  else:
    print()
    print("The word " + word1Input + " cannot be formed from the word " + word2Input)

def createWordWithTwoWords(word1, word2):
  count = 0

  for word1Count in range(0, len(word1)):
    for word2Count in range(len(word2)):
      if word1[word1Count] == word2[word2Count]:
        count += 1
      if count == len(word1):
        return True

  return False

mainMenu()