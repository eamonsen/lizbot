from TwitterAPI import TwitterAPI

keys = open('keys.liz').readlines()

api=TwitterAPI(keys[0],keys[1],keys[2],keys[3])
from pprint import pprint
query='#springbreak'
r = api.request('search/tweets', {'q':query})
#r = api.request('search/tweets', {'locations':'-74,40,-73,41'})

tweets=[]

for item in r.get_iterator():
   # pprint(item[u'text'])
    tweets=tweets+[item[u'text']]



