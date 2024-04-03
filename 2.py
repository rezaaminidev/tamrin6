numbers = []
for i in range(51):
    if i % 2 != 0:
        numbers.append(i)

for num in numbers[:]:  
    if num % 3 == 0 or num % 5 == 0:
        numbers.append(num)

print(numbers)
