def sieve(limit, maybe_prime_nums, prime_num=3):
    if prime_num ** 2 <= limit:
        for num in maybe_prime_nums:
            if num % prime_num == 0 and num != prime_num:
                maybe_prime_nums.remove(num)

    elif prime_num ** 2 > limit:
        return maybe_prime_nums


    return sieve(limit, maybe_prime_nums, maybe_prime_nums[maybe_prime_nums.index(prime_num) + 1])


n = int(input('Provide a number: '))

if n in sieve(n+1, [num for num in range(3, n+1, 2)]):
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')