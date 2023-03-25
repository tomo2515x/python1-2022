# from adir.f import foo
# from f import foo
# export PYTHONPATH=~/Documents/python1-2022

# from src.algo.z4.libs.f import foo
from libs.f import foo
import os

print (os.getcwd())


# foo(10)

# print('ok')

# print('-------------')
# with open('src/algo/z4/kadabra.txt') as f:
#     print(f.readlines())
# print('-------------')

# print('uruchamiam funkcje')
# print(foo(10))

from gen_train_data import generate_data
   


def get_city_most_connections(train_data: list[tuple[int,int]]) -> int:
    source = []
    for conn in train_data: source.append(conn[0])
    mostconnections = {i:source.count(i) for i in source}

    return int(max(mostconnections, key=mostconnections.get))


print(get_city_most_connections(generate_data(10)))