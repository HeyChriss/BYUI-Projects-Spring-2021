Number = int(input('How many columns and rows do you want in your multiplication table? '))
range_size = Number + 1

for row_number in range(1, range_size):
    for col_number in range(1, range_size):
        result = row_number * col_number
        print(f'{result:3}', end=' ')
    print()
