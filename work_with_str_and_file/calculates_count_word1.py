"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит
самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
"""

from collections import Counter

def create_lst(path_in):
    """
    Func reads strings from file and creates list
    :param path_in: path to file
    :return: list, based on data from file
    """
    un_lst = []
    with open(path_in) as file:
        for line in file:
            un_lst.extend(line.split())
    return un_lst



def main():
    path_in = "path_to_file"
    unsort_lst = create_lst(path_in)                                    # create unsorted list from data from file
    unsort_lst = list(map(str.lower, unsort_lst))                       # lowercase
    sort_dct = Counter(unsort_lst)                                      # Counter creates calculated dict
    print(sort_dct.most_common(1)[0][0], sort_dct.most_common(1)[0][1]) # take first key and value


if __name__ == "__main__":
    main()
