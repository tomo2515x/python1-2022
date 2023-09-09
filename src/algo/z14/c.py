import b, a

def gen_new_positions(position: tuple[int], max_dim: tuple[int,int]) -> list[tuple[int,int]]:
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    possible_moves = []
    valid_moves = []
    
    for x in moves:
        possible_moves.append(b.make_move(position, x))
        
    print(possible_moves)
    for x in possible_moves:
        if a.is_on_board(x, max_dim):
            valid_moves.append(x)

    return valid_moves



import unittest

from c import gen_new_positions


def equals_any_order(list1: list, list2: list) -> bool:
    return sorted(list1) == sorted(list2)


class TaskCTests(unittest.TestCase):

    def test_1(self):
        pos = (0, 0)
        n_pos = gen_new_positions(pos, (8, 8))
        self.assertTrue(n_pos, [(1,2), (2,1)])

    def test_2(self):
        pos = (1, 1)
        n_pos = gen_new_positions(pos, (8, 8))
        self.assertTrue(n_pos, [(0,3), (2,3), (3,0), (3,2)])

 
if __name__ == '__main__':
    unittest.main()

        
    