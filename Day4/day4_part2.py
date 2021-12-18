class Board:
    def __init__(self, board_str):
        self.board_array = [[int(num) for num in row.split()] for row in board_str.split("\n") if row != []]
        self.bool_board_array = [[False for i in range(5)] for j in range(5)]
        self.done = False
    
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
        for c in range(5):
            if sum(transpose[c]) == 5:
                return self.get_total() * number
        
        return -1


    def get_total(self) -> int:
        sum = 0
        for r in range(5):
            for c in range(5):
                if not self.bool_board_array[r][c]:
                    sum += self.board_array[r][c]
        return sum

    def set_done(self) -> None:
        self.done = True

#TODO  interate over boards
#      mark -> check (-> get total)


def get_bingo_numbers() -> list[int]:
    with open("input.txt") as input:
        return [int(n) for n in input.readline().rstrip("\n").split(",")] 

def get_bingo_boards() -> list[Board]:
    result = []
    with open("input.txt") as input:
        #skip bingo numbers & new lines
        lines = [line for line in input.readlines()[2:] if line != "\n"]
        line_counter = 0
        board_str = ""
        for line in lines:
            line_counter += 1
            board_str += line
            if line_counter % 5 == 0:
                result.append(Board(board_str))
                board_str = ""
    return result

def main():
    done_boards = 0
    boards = get_bingo_boards()
    number = get_bingo_numbers()
    for num in number:
        for board in boards:
            if board.mark_board(num):
                score = board.check_board(num)
                if score != -1:
                    if not board.done:
                        done_boards +=1
                        board.set_done()
                    if done_boards == len(boards):
                        return score
                

if __name__ == "__main__":
    print(main())

