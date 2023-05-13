
"""
****     #
*     ####
*       ##
***     ##
*     ####
**     ###

jeśli długości *'ek klucza + długości #'ów zamka są dla wszystkich takie same, to klucz otwiera zamek


"""




def open_lock(key: list[int], lock: list[int]) -> int:
    longest_key = key[1]
    shortest_lock = lock[1]
    i = 0
    match = 0

    for k in range(len(key)):
        if key[k] > longest_key:
            longest_key = key[k]
        if lock[k] < shortest_lock:
            shortest_lock = lock[k]
    
    for teeth in key:

        if teeth + lock[i] != longest_key+shortest_lock:
            i+=1

        else:
            i+=1
            match +=1

    if match == len(lock):
        print("im opening")
        return 0
    print("im not opening")
    return 1
