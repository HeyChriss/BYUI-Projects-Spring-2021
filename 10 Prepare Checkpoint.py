items = []
item = ''

while item != 'Quit':
    item = input('Please enter the items of the shopping list (type: quit to finish):').capitalize()
    if item != 'Quit':
        items.append(item)
print ()
for list in items:
    print (f'Item: {list}')
print ()
print ('The shopping list is:')
for i in range (len(items)):
    k = items[i]
    print (k)
print ()
print ('The shopping list with indexes is:')
for j in range (len(items)):
    k = items[j]
    print (f'{j}. {k}')


delete = int(input ('Which item would you like to change?'))
new_item = input('What is the new item?')
items[delete] = new_item 
print ()
print ('The shopping list with indexes is:')
for o in range (len(items)):
    k = items[o]
    print (f'{o}. {k}')
