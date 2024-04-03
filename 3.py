import random

strings = ["hello", "yello", "mello", "hallo"]

items = []

for _ in range(100):
    items.append(random.choice(strings))
print(items)
