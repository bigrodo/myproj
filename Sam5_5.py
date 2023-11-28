list_1 = [1, 1, 3, 3, 1] 
list_2 = [5, 5, 5, 5, 5, 5, 5] 
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def update_list(old_list):
    result_set = set()
    for i in old_list:
        set_1 = old_list.count(i)
        result_set.add(i)
        for i_2 in range(2, set_1 + 1):
            result_set.add(int(str(i) * i_2))
    return result_set
        
if __name__ == "__main__":
    print("Обновленный list_1: ", update_list(list_1))
    print("Обновленный list_2: ", update_list(list_2))
    print("Обновленный list_3: ", update_list(list_3))
