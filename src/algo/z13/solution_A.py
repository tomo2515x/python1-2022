
import random

def get_decomposition(n, k, x) -> list[int]:
    index = 1
    list_size = k
    ent_number = n
    exclusion = x
    available_numbers = []
    tries = 0

    while list_size >= index:
        available_numbers.append(index)
        index += 1
    
    available_numbers.remove(exclusion)
    randomized = 0
    used_numbers = []
    if available_numbers != []:
        while tries <= 1000000:
            tries += 1
            used_numbers.append(random.choice(available_numbers))
            randomized = sum(used_numbers)
            
            if randomized > ent_number:
                used_numbers.pop()
            if randomized == ent_number:
                break
        randomized = sum(used_numbers)
        if randomized != ent_number:
            used_numbers.pop()
        return used_numbers
    else:
        return []
    
