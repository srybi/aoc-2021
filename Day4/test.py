import unittest

from Day4.day4 import Board

class TestDay4(unittest.TestCase):

    def test_init_board_array(self):
        #given:
        board_str = "49  0  9 90  8\n41 88 56 13 6\n17 11 45 26 75\n29 62 27 83 36\n31 78  1 55 38\n"
        board_array = [ [49, 0, 9, 90, 8], 
                        [41, 88, 56, 13, 6], 
                        [17, 11, 45, 26, 75],
                        [29, 62, 27, 83, 36],
                        [31, 78,  1, 55, 38] ]
        
        #when
        b = Board(board_str)

        #than
        self.assertEqual(board_array, b.board_array)

    def test_init_bool_board_array(self):
        #given:
        board_str = "49  0  9 90  8\n41 88 56 13 6\n17 11 45 26 75\n29 62 27 83 36\n31 78  1 55 38"
        board_bool_array = [[False, False, False, False, False], 
                            [False, False, False, False, False], 
                            [False, False, False, False, False],
                            [False, False, False, False, False],
                            [False, False, False, False, False] ]
        
        #when
        b = Board(board_str)

        #than
        self.assertEqual(board_bool_array, b.bool_board_array)

    def test_mark_board(self):
        #given:
        test_board = Board("49  0  9 90  8\n41 88 56 13 6\n17 11 45 26 75\n29 62 27 83 36\n31 78  1 55 38")
        num = 88
        result_board = [[False, False, False, False, False], 
                        [False, True, False, False, False], 
                        [False, False, False, False, False],
                        [False, False, False, False, False],
                        [False, False, False, False, False]]
        result = True
        
        #when
        yo = test_board.mark_board(num)
        #than
        self.assertEqual(result, yo)
        self.assertEqual(result_board, test_board.bool_board_array)

    def test_mark_board_edge(self):
        #given:
        test_board = Board("49  0  9 90  8\n41 88 56 13 6\n17 11 45 26 75\n29 62 27 83 36\n31 78  1 55 38")
        num = 38
        result_board = [[False, False, False, False, False], 
                        [False, False, False, False, False], 
                        [False, False, False, False, False],
                        [False, False, False, False, False],
                        [False, False, False, False, True]]
        result = True
        
        #when
        yo = test_board.mark_board(num)
        #than
        self.assertEqual(result, yo)
        self.assertEqual(result_board, test_board.bool_board_array)

    def test_mark_board_failed(self):
        #given:
        test_board = Board("49  0  9 90  8\n41 88 56 13 6\n17 11 45 26 75\n29 62 27 83 36\n31 78  1 55 38")
        num = -1
        result_board = [[False, False, False, False, False], 
                        [False, False, False, False, False], 
                        [False, False, False, False, False],
                        [False, False, False, False, False],
                        [False, False, False, False, False]]
        result = False
        
        #when
        yo = test_board.mark_board(num)
        #than
        self.assertEqual(result, yo)
        self.assertEqual(result_board, test_board.bool_board_array)    
        
    def test_check_board_rows(self):
        #given
        test_board = Board("52 53 19 56 80\n94 33  3 78 32\n10 89 66 48 55\n99 23 88  8 39\n76 75 44 79 14")
        num = 99
        nums = [94, 33,  3, 78, 32, 52, num] 
        #when
        for n in nums:
            test_board.mark_board(n)
        result = test_board.check_board(num)
        #than
        self.assertEqual(result, sum(nums)*num)

    def test_check_board_columns(self):
        #given
        test_board = Board("52 53 19 56 80\n94 33  3 78 32\n10 89 66 48 55\n99 23 88  8 39\n76 75 44 79 14")
        num = 88
        nums = [52, 94, 10, 99, 76, 33, num]
        #when
        for n in nums:
            test_board.mark_board(n)
        result = test_board.check_board(num)
        #than
        self.assertEqual(result, sum(nums) * num)
    
    def test_check_board_failed(self):
        test_board = Board("52 53 19 56 80\n94 33  3 78 32\n10 89 66 48 55\n99 23 88  8 39\n76 75 44 79 14")
        num = 88
        nums = [52, 94, 10, num]

        for n in nums:
            test_board.mark_board(n)
        result = test_board.check_board(num)

        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()


