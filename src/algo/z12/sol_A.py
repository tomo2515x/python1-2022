def remove_items(test_list, item):
 
    res = [i for i in test_list if i != item]
 
    return res

def get_min_number_of_operations(a: list[int]) -> int:

    streak = 0
    operat = []

    for num_index in range(len(a)):

        if a[num_index] <= 0:
            streak += 1
            
        else: 
            operat.append(streak)
            streak = 0
            
    operat.append(streak)    
    return len(remove_items(operat, 0))

