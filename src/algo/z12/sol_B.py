
def get_best_value_package(costs: list[int], values: list[int], max_total_cost: int) -> int:
    
    wyn = 0

    for k in range(2 ** len(costs)):
        cst = 0
        vle = 0

        for i in range(len(costs)):

            if k & (1 << i):
                cst += costs[i]
                vle += values[i]

        if cst <= max_total_cost and vle > wyn:
            wyn = vle
            
    return wyn
