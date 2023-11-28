def remove_element_from_tuple(my_tuple, element):
    if element in my_tuple:
        index = my_tuple.index(element)
        new_tuple = my_tuple[:index] + my_tuple[index + 1:]
        return new_tuple
    else:
        return my_tuple

tuple1 = (1, 2, 3)
result1 = remove_element_from_tuple(tuple1, 1)
print(result1)

tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
result2 = remove_element_from_tuple(tuple2, 3)
print(result2)

tuple3 = (2, 4, 6, 6, 4, 2)
result3 = remove_element_from_tuple(tuple3, 9)
print(result3)
