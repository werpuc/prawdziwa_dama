# 1
import re

def get_url (word, start, end, language = 'pl'):
   pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}")
   assert pattern.match(start)
   assert pattern.match(end)
   assert end > start
   url = url = u'https://twitter.com/search?q='+word+'%20since%3A'+start+'%20until%3A'+end+'&l='+language+'&src=typd&f=tweets'
   return url

# 2