import asyncio
import itertools
import math


def isPrime(number):
    return number > 1 and all(number % i for i in itertools.islice(itertools.count(2), int(math.sqrt(number) - 1)))    # noqa


async def number_is_prime(start_num, end_num, ):
    prime_sum = 0

    for number in range(start_num, end_num + 1):
        if isPrime(number):
            prime_sum += number
    return prime_sum


async def get_prime_sum(start_num, end_num, ):
    return await number_is_prime(start_num, end_num, )


if __name__ == '__main__':
    start_num = 1
    end_num = 10

    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(get_prime_sum(start_num, end_num)))
    loop.close()
