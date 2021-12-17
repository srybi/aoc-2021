class Board:
    def __init__(self, board_str):
        self.board_array = [[int(num) for num in row.split()] for row in board_str.split("\n")]
        self.bool_board_array = [[False for i in range(5)] for j in range(5)]
    
    def mark_board(self, number) -> bool:
        for r in range(5):
            for c in range(5):
                if self.board_array[r][c] == number:
                    self.bool_board_array[r][c] = True
                    return True
        return False

    def check_board(self, number) -> int:
        #check rows
        for r in range(5):
            if sum(self.bool_board_array[r]) == 5:
                return self.get_total() * number

        #check columns
        transpose = list(map(list, zip(*self.bool_board_array)))
        print(transpose)
        for c in range(5):
            if sum(transpose[c]) == 5:
                return self.get_total() * number


    def get_total(self) -> int:
        sum = 0
        for r in range(5):
            for c in range(5):
                if self.bool_board_array[r][c]:
                    sum += self.board_array[r][c]
        return sum

#TODO: init all boards from input.txt
#      iterate over bingo nums
#      interate over boards
#      mark -> check (-> get total)


def get_bingo_numbers():
    with open("input.txt") as input:
        nums = input.readline().rstrip("\n")
        return nums.split(",")

