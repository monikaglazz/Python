# Ways to get a descending and ascending list of numbers

# Descending order with while:
num = 5
numbers = []
while (num > 0):
    numbers.append(num)
    num -= 1

# Descending order with for:
numbers = []
for x in range(200, 0, -1):
    print(x)

# Descending order with for and list comprehension:
descending = [x for x in range(200, 0, -1)]
print('descending: ', descending)

# Ascending order with while:
num = 1
numbers = []
while num < 101:
    numbers.append(num)
    num += 1

# Ascending order with for:
numbers = []
for num in range(1, 101, 1):
    numbers.append(num)

# Ascending order with for and list comprehension:
ascending = [x for x in range(1, 101, 1)]
print('ascending: ', ascending)
