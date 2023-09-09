def is_on_board(position: tuple[int, int], max_dim: tuple[int, int] = (8, 8)):
   """
   :param position: position of a piece on the chessboard 
   :param max_dim: max dimensions of the board
   :return: True if the piece is on the board
   """
   A = int(position[0])
   B = int(position[1])
   B2 = int(max_dim[1])
   A2 = int(max_dim[0])

   if A > A2 and B < B2:
       return False
   elif A == 8 or B == 8:
       return False
   elif A < 0 or B < 0:
       return False
   else:
       return True