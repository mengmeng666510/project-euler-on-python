def fib(limit):
    a, b = 0, 1
    c = a + b
    while c <= limit:
        yield c
        a, b = b, c
        c = a + b


print(sum(filter(lambda n: n % 2 == 0, fib(4_000_000))))
