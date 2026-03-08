def prime_factors(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            yield i
            n //= i
        i += 1
    if n > 1:
        yield n


print(max(prime_factors(600851475143)))
