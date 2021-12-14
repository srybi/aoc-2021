def get_bingo_numbers():
    with open("input.txt") as input:
        nums = input.readline().rstrip("\n")
        return nums.split(",")

class Board:
    def __init__(self, board_str):
        # init 2d-array with board str numbers
        pass
        # init 2d-array only false
    
    #TODO: def checkboard(self, number):
    #TODO: def markboard(self, number):
    #TODO: def getTotal(self):

#TODO: init all boards from input.txt
#      iterate over bingo nums
#      interate over boards
#      mark -> check (-> get total)