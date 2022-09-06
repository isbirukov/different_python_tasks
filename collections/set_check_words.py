"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов,
после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста
для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
"""

def main():
    set_words = set()
    num_words = int(input())
    lst_words = set([input().lower() for i in range(num_words)])            # список проверочных слов

    num_strings = int(input())
    check_strings = [input().lower().split() for i in range(num_strings)]   # список проверяемых строк

    for el in check_strings:
        set_str = set(el)
        set_words = set_words.union(set_str.difference(lst_words))

    print(" \n".join([i for i in set_words]))


if __name__ == "__main__":
    main()