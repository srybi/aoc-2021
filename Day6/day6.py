DAYS = 265

def get_nums():
    with open("input.txt") as input:
        return [int(num) for num in input.readline().split(",")]

def do_one_day(nums) -> list[int]:
    for i in range(len(nums)):
        nums[i] -= 1
        if nums[i] == -1:
            nums[i] = 6
            nums.append(8)   
    return nums

def main():
    nums = get_nums()
    for i in range(DAYS):
        nums = do_one_day(nums)
        if i < 17:
            print(nums)
    print(len(nums))

if __name__ == "__main__": 
    main()