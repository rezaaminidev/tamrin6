def merge_dicts(d1, d2):

    merged_dict = {}

    for key in d1.keys():
        if key in d2:
            merged_dict[key] = d1[key] + d2[key]
        else:
            merged_dict[key] = d1[key]

    for key in d2.keys():
        if key not in merged_dict:
            merged_dict[key] = d2[key]

    return merged_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
merged_dict = merge_dicts(d1, d2)
print("دیکشنری :", merged_dict)
