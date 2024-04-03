def is_sorted_ascending(lst):
    return lst == sorted(lst)

my_list = [1, 2, 3, 4, 5]
print(is_sorted_ascending(my_list))  

my_list = [5, 4, 3, 2, 1]
print(is_sorted_ascending(my_list))  
