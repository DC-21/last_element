def find_last_element(lst):
    if len(lst) > 0:
        last_element = lst[-1]
        return last_element
    else:
        return None

# Example usage:
my_list = [1, 2, 3, 4, 5]
last_element = find_last_element(my_list)
print("Last element of the list:", last_element)

