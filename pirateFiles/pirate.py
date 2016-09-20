import webbrowser
import sys

f = open('/Users/noah/docs/piratelist.txt')
item = int(sys.argv[1])
items = ['']
curr = 0
for i in f.read():
  if not i == '\n':
    items[curr] += i
  elif i == ' ':
    items[curr] += '%20'
  else:
    curr += 1
    items.append('')

url = 'https://thepiratebay.org/search/' + items[item] + '/'
webbrowser.open(url)
