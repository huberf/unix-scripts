import sys

f = open('/Users/noah/docs/piratelist.txt')

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

index = 0
for i in items:
  if not i == '':
    print str(index) + ": " + i
    index+=1
