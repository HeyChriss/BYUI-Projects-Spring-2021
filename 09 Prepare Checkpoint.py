Friends = []
name = ""


while name !="End":
    name = input ('Please type the name of your friend (type END when you are done)').capitalize()
    if name != "End":
        Friends.append(name)
print ()
for names in Friends:
    print (names)

# friends = []
# name = None
# 
# while name != "end":
#     name = input("Type the name of a friend: ")
#     if name != "end":
#         friends.append(name)
# print()
# print("Your friends are:")
# 
# for friend in friends:
##     print(friend)
## 
#
#
#Items = []
#Price = []
#Input_items = '1'
#Input_Price = 0.00
#Delete_Items = 0
#Delete_Price = 0
#Option = 6
#
#
#
#while Option != 5:
#    print ('Welcome to the Shopping Cart Program')
#    print ('Please select one of the following:')
#    print ('1. Add item')
#    print ('2. View cart')
#    print ('3. Remove item')
#    print ('4. Compute total')
#    print ('5. Quit')
#    Option = int(input ('Please enter an action:'))
#    if Option == 1:
#        Input_items = input('What item would you like to add? ')
#        Input_Price = float(input(f'What is the price of {Input_items}?'))
#        Items.append(Input_items)
#        Price.append(Input_Price)
#        print (f'{Input_items} has been added to the list')
#    elif Option == 2:
#        print ('The contents of the shopping cart are:')
#        for i in range (len(Items)):
#            item = Items[i]
#        for number in range (len(Items)):
#            item = Items[number]
#        for j in range (len(Price)):
#            price_number  = Price[j]
#            print (f'{number}. {item} - ${price_number}')
#    elif Option == 3:
#        Delete_Items = int(input('Which item would you like to remove? '))
#        Items.pop(Delete_Items)
#        Price.pop(Delete_Items)
#        print ('The item has been deleted')
#    # elif Option == 4:
#
#print ('Thank you, Goodbye')
#    
#
#
#
