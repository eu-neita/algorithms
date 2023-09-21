def find_duplicate(nums):

    set_nums = set()

    for num in nums:
        if type(num) != int or num < 0:
            return False
        if num in set_nums:
            return num
        set_nums.add(num)
    return False
