"""
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Sample Input 1:
2016 4 20
14

Sample Output 1:
2016 5 4
"""
import datetime


def main():
    a = [int(i) for i in input().split()]
    dt = datetime.date(*a)
    delta2 = datetime.timedelta(days=int(input()))
    result = dt + delta2
    print(f"{result.year} {result.month} {result.day}")


if __name__ == "__main__":
    main()
