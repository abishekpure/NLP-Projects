# -*- coding: utf-8 -*-
"""Document__Similarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qk7INoPnt8na-OoYRf05mdp95C65v-rX
"""

#import necessary modules
import math
import re
from collections import Counter

#the increment operator is used to match more than one repetition of the regular expression
WORD = re.compile(r'\w+')

def TEXT2VECTOR(text):
    words = WORD.findall(text)
    #unsorted collection in which elements are stored as dictionary keys and counts as dictionary values
    return Counter(words)

#calculate cosine distance to find the similarity between both the text documents
def CosineDistance(vect1, vect2):
    # a collection of unsorted unique items
    intersection = set(vect1.keys()) & set(vect2.keys())  # return set with elements in intersection
    num = sum([vect1[x] * vect2[x] for x in intersection])

    sum1 = sum([vect1[x] ** 2 for x in vect1.keys()])
    sum2 = sum([vect2[x] ** 2 for x in vect2.keys()])
    den = math.sqrt(sum1) * math.sqrt(sum2)

    if not den:
        return 0.0
    else:
        return float(num) / den

def readFile(fileName):
  return open("../content/" + fileName, 'r').read() #reads the name of the file

Text1 = readFile("txt1.txt") #accepts text document 1
Text2 = readFile("txt2.txt") #accepts text document 2

vect1 = TEXT2VECTOR(Text1) #converts text doc 1 to vector 1
vect2 = TEXT2VECTOR(Text2) #converts text doc 2 to vector 2

cosine_dist = CosineDistance(vect1, vect2) #calculates cosine distance between text docs 1 and 2

print("The cosine distance is:\t", cosine_dist) #displays the cosine distance