n = 1000


def sum_of_multiples(k: int) -> int:
    m = n // k
    return k * m * (m + 1) // 2


print(sum_of_multiples(3) + sum_of_multiples(5) - sum_of_multiples(15))
