#Create the new list and variable for the input. 
numbers = []
user_input = 1

while user_input != 0:
    user_input = int(input('Enter a list of numbers, type 0 when finished '))
    if user_input != 0:
        numbers.append(user_input)

#Create the variables for the next requirements
total = 0
average = 0
largest_number = max(numbers)
smallest_number = 99999999
count = len(numbers)

for number in numbers:
    total += number
    average = total / count 
print(f'The total is: {total}')
print(f'The average is: {average:.2f}')
print(f'The largest number is: {largest_number}')

# This is for the smallest number. 
for number in numbers:
    if number > 0 and number < smallest_number:
        smallest_number = number
print(f'The smallest positive number is: {smallest_number}')

#This is the strech challenge.
#The list is sorted out. 

List = sorted(numbers)

print("The list of numbers are:")
for number in List:
    print(number)



