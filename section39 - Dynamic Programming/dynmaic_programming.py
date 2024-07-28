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