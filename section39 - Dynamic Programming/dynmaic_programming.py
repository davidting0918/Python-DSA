def fib(n: int):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_memo(n: int):
    memo = {}
    def _fib(n: int):
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return n

        memo[n] = _fib(n - 1) + _fib(n - 2)
        return memo[n]

    return _fib(n)


def fib_bottom_up(n: int):
    num_list = [0, 1]
    for index in range(2, n + 1):
        next_fib = num_list[index - 1] + num_list[index - 2]
        num_list.append(next_fib)
    return num_list[n]


def remove_element(nums: list, value: int):
    i = 0
    while i < len(nums):
        if nums[i] == value:
            nums.pop(i)
        else:
            i += 1
    return len(nums)
    

def find_max_min(nums: list):
    minimum = nums[0]
    maximum = nums[0]
    
    for num in nums:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    
    return (maximum, minimum)


def find_longest_string(strings: list):
    longest = ""
    
    for string in strings:
        if len(string) > len(longest):
            longest = string
    
    return longest
    

def remove_duplicates(nums: list):
    index = 0
    while index < len(nums):
        if nums[index] in nums[:index]:
            nums.pop(index)
    
        else:
            index += 1
    return len(nums)


def max_profit(prices: list):
    mp = 0
    for i in range(len(prices) - 1):
        p = [prices[j] - prices[i] for j in range(i + 1, len(prices))]
        mp = max(mp, max(p))
    return mp
    
    
def rotate(nums: list, k: int):
    for i in range(k):
        nums.insert(0, nums.pop())
    return nums


def max_subarray(nums: list):
    if not nums:
        return 0
    maximum = float("-inf")
    
    for index in range(len(nums)):
        for sub_index in range(index + 1, len(nums) + 1):
            maximum = max(maximum, sum(nums[index:sub_index]))
    
    return maximum