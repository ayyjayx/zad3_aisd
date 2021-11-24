import math


def numbers(n: int):
    if n < 0:
        return
    print(n)
    numbers(n - 1)


def fib(n: int) -> int:
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n - 2)


def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    return number * power(number, n - 1)


def reverse(txt: str) -> str:
    if len(txt) == 0:
        return ""
    return txt[len(txt) - 1] + reverse(txt[0: len(txt) - 1])


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


# def prime(n: int) -> bool:
#     if n in {0, 1}:
#         return False
#     if n == 2:
#         return True
#
#     sqrt = math.sqrt(n)
#     if n % math.ceil(sqrt) == 0:
#         return False
#     # return prime(n, math.ceil(sqrt))
#     return prime(n - 1)


def prime(n: int, div=-1) -> bool:
    if n <= 1:
        return False
    if div == 1 or n == 2:
        return True

    sqrt: float = math.sqrt(n)

    if div == -1:
        return prime(n, math.ceil(sqrt))

    if n % div == 0:
        return False

    return prime(n, div - 1)


def remove_duplicates(txt: str) -> str:
    if len(txt) in {0, 1}:
        return txt
    if txt[0] == txt[1]:
        return remove_duplicates(txt[1:])
    return txt[0] + remove_duplicates(txt[1:])

# numbers(10)
# print(fib(4))
# print(power(2, 4))
# print(reverse('asdf'))
# print(factorial(5))
print([prime(n) for n in range(15)])
# print(remove_duplicates('aaassdddaa'))
