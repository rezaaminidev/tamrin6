list_1 = ["milk", "sugar", "butter", "yogurt", "cheese"]
list_2 = [5, 2, 10, 1, 3]

total_needed = {item: quantity for item, quantity in zip(list_1, list_2)}

print("مقدار کلی مورد نیاز برای هر آیتم:")
for item, quantity in total_needed.items():
    print(item + ":", quantity)
