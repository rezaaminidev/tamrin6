def find_max_min(dictionary):
    max_value = max(dictionary.values())
    min_value = min(dictionary.values())
    return min_value, max_value

my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
min_value, max_value = find_max_min(my_dict)
print("مقدار مینیمم:", min_value)
print("مقدار ماکزیمم:", max_value)
