"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
aba_baba
ab_aba_ba
abab_aba

Sample Input 1:
abababa
aba
Sample Output 1:
3

Sample Input 2:
abababa
abc
Sample Output 2:
0

Sample Input 3:
abc
abc
Sample Output 3:
1

Sample Input 4:
aaaaa
a
Sample Output 4:
5
"""


def main():
    s = input()
    t = input()
    count = 0
    ind = 0
    while True:
        if s.find(t, ind) >= 0:
            ind = s.find(t, ind) + 1
            count += 1
        else:
            break
    print(count)


if __name__ == "__main__":
    main()
