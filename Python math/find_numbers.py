
# Finds numbers from range 0 - 200 that can be divided by 5 and cannot by 7.

numbers = []

for number in range(0, 200, 1):
    if number % 5 == 0 and number % 7 != 0:
        numbers.append(number)

print(numbers)
