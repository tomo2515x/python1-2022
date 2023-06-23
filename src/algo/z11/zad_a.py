M = 1000
data: list[list]


def get_new_bag(data_size: int):
    return [[] for _ in range(data_size)]


def insert_element(bag: list[list], element: int):
 
    bag[element.__hash__() % len(bag)].append(element)


def contains_element(bag: list[list], element: int) -> bool:
   
    return bag[element.__hash__() % len(bag)].__contains__(element)

    # todo: sprawdzić czy `x` z hashem `h` jest w `bag`
    # odpowiednio zawężony (do [0...M-1] hash ma być numerem listy)
    # wyliczyć "indeks listy" z hasha,
    # sprawdzić czy bag[idx] zawiera `element`


def remove_element(bag: list[list], element: int) -> bool:
    bag[element.__hash__() % len(bag)].remove(element)
    # wyliczyć "indeks listy" z hasha,
    # usunąć z listy bag[idx] element `element`

# def hashKey(listId, bagCapacity):
#     keyvar1 = [listId[0], listId[1]]
#     return ''.join(keyvar1).__hash__() % bagCapacity

# name1 = ["Matt", "Stone"]


if __name__ == '__main__':
    bag = get_new_bag(1000)  # np. bag[0] jest listą... i bag[999]...
 
    for a in range(10000):
        insert_element(bag, a)
    
    insert_element(bag, 17)
    insert_element(bag, 32)
    insert_element(bag, "amon")
    insert_element(bag, "amom")
    print(bag)

    print(contains_element(bag, 17))
    # print(contains_element(bag, 18), False)
    # remove_element(bag, 32)
    print(contains_element(bag, 32))
    # remove_element(bag, 17)
    # print(contains_element(bag, 17))
