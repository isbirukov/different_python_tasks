"""
Реализации функции Фибоначчи
"""
import functools


def fib_recurs(n):
    """
    Реализация в виде рекурсии
    Неэффективная реализация!
    """
    if n in (0, 1):
        return 1
    return fib_recurs(n-1) + fib_recurs(n - 2)

@functools.lru_cache
def fib_recurs2(n):
    """
    Реализация в виде рекурсии
    Неэффективная реализация, но в разы быстрая чем предыдущая за счет кэширования!
    """
    if n in (0, 1):
        return 1
    return fib_recurs(n-1) + fib_recurs(n - 2)


def main():
    # recurs = [fib_recurs(n) for n in range(10)]
    # print(recurs)

if __name__ == "__main__":
    main()
