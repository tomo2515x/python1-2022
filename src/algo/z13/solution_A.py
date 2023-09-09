<<<<<<< Updated upstream

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
    
=======
def recur(deconumber, remaining, valid):

    if remaining == 0:
        return 1
    else:
        ans = []
        for number in valid:
            if remaining-number >= 0:
                new_deco = deconumber[:]
                print(new_deco)
                new_deco.append(number)
                print(new_deco)
                cand = recur(new_deco, remaining-number, valid)
                
                if cand:
                    ans.append(cand)
                    
            if len(ans) > 0:
            
                return ans

    



def get_decomposition(n, k, x) -> list[int]:
    valid = [a for a in range(1,k+1)]
    if x in valid:
        valid.remove(x)
    valid = sorted(valid, reverse=True)

    recur([], n, valid)

print(get_decomposition(19, 5, 1))
>>>>>>> Stashed changes
