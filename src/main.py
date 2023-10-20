import random
import math

from img2text import img2text
from text2img import text2img

def calculateStatistics(text):
  sampleCount = {}
  wordCounts = {}
  words = text.split(" ")

  for i in range(1, len(words)):
    last_word = words[i-1]
    cur_word = words[i]

    if last_word not in wordCounts:
      wordCounts[last_word] = {}
      sampleCount[last_word] = 0
    
    if cur_word not in wordCounts[last_word]:
      wordCounts[last_word][cur_word] = 0
    
    wordCounts[last_word][cur_word] += 1
    sampleCount[last_word] += 1
  
  return (wordCounts, sampleCount)

def createModel(wordCounts, sampleCount):
  model = {}
  for ngram in sampleCount:
    samples = sampleCount[ngram]

    probabilities = []
    for key in wordCounts[ngram]:
      probability = wordCounts[ngram][key] / samples
      probabilities.append((probability, key))
    probabilities.sort(key=lambda x: x[0])

    summedProbability = []
    _prob = 0
    for (p, val) in probabilities:
      _prob += p
      summedProbability.append((_prob, val))

    model[ngram] = summedProbability
  return model

def applyModel(model, letter: str, probability: float):
  if letter not in model:
    letter = randomKey(model)
  probabilities = model[letter]
  chosenLetter = probabilities[0][1]

  for (prob, val) in probabilities:
    if prob <= probability:
      chosenLetter = val
    else:
      break
  
  return chosenLetter

def randomKey(model):
  availableKeys = [key for key in model]
  randomKey = availableKeys[math.floor(random.random() * len(availableKeys))]
  return randomKey

def createString(model, initial: str, length: int, separator=""):
  lastLetter = initial
  outStr = initial + separator
  for i in range(length-1):
    newLetter = applyModel(model, lastLetter, random.random())
    outStr += newLetter + separator
    lastLetter = newLetter

  return outStr

import sys
def readAllInput():
  return " ".join(sys.stdin.readlines())

def getInputFromFile():
  if len(sys.argv) < 1:
    print("This program requires a file name")
  return img2text(sys.argv[1])

if __name__ == "__main__":
  # text = readAllInput()
  text = getInputFromFile()
  (wc, sc) = calculateStatistics(text)
  model = createModel(wc, sc)
  
  for i in range(1):
    output = createString(model, randomKey(model), 32, " ")
    img = text2img(output)
    img.show()
