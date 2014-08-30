from pprint import pprint
import json
from twit import query
import os.path

#ruthlovestantony=0
#if ruthlovestantony>1:
   # print(ruthlovestantony)
#else: 
   # print('no')

#cats=['ruth', 'tantony', 'pheobe']
#for cat in cats: 
   # if 'o' in cat:
       # print('meow')
   # else:
       # print('purr')

# catnoise={'ruth':'purr',
#           'tantony':'meow',
#           'pheobe':'meow'}

# for cat in catnoise:
#     print("----")
#     print("cat name: " + cat)
#     print("cat noise: " + catnoise[cat])
# print(catnoise['ruth'])


#def catlady(cat):
   # print('homer loves '+cat)


#catlady('tantony')

#sentences=['ruth purrs loudly', 'eats tuna tonight', 'purrs with tantony', 'breakfast is early', 'loudly eats breakfast', 'tantony eats dinner', 'tantony eats breakfast']

if os.path.exists(query):
   f=open(query)
   lms=f.read()
   lm=json.loads(lms)
else:
   lm={}


from twit import tweets
sentences=tweets

for sentence in sentences:
#  print(sentence.split(' '))
   sentence=sentence.lower().split(' ')
#  print([[sentence[i], sentence[i+1]] for i in range(len(sentence)-1)])

##The above splits sentences in an array into arrays of bigrams.
  
   bigrams=[[sentence[i], sentence[i+1]] for i in range(len(sentence)-1)]
   for bigram in bigrams:
#     print bigram
      counts=lm.get(bigram[0], {})
      count=counts.get(bigram[1], 0)
      counts[bigram[1]]=count+1
      lm[bigram[0]]=counts


#      print counts
#     print count




#   print('--------------')

#pprint(lm)


##Markov chain time

from random import randint
randkey=lm.keys()[randint(0, len(lm.keys())-1)]
#print('___________')
#print(randkey)

#print(lm[randkey])

randval=lm[randkey]

words=[randkey]

while randkey in lm:
   randval=lm[randkey]
   randkey2=randval.keys()[randint(0, len(randval.keys())-1)]
   randkey=randkey2
   words=words+[randkey]

pprint(' '.join(words)+'!'+' '+'#'+words[randint(0, len(words)-1)])

f=open(query, "w")
f.write(json.dumps(lm))
f.close()
