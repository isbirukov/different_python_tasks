"""
Имеется файл с данными по успеваемости абитуриентов.
Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и
для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке,
соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и
добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику
и одной строкой со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
"""


def create_lst(path_in):
    """
    Func reads strings from file and creates list
    :param path_in: path to file
    :return: list, based on data from file
    """
    un_lst = []
    lst= []
    with open(path_in) as file:
        for line in file:
            un_lst.append(line.strip().split(";"))
    for el in un_lst:
        tmp = []
        tmp.append(el[0])
        tmp.extend(list(map(int, el[1:])))
        lst.append(tmp)
    return lst

def write_to_file(path_out, lst):
    """
    Func writes to file
    :param path_out: path to output file
    :param lst: list with data for computing
    :return:
    """
    with open(path_out, 'w') as file:
        for el in lst:                              # count avg for student
            avg_student = sum(el[1:])/len(el[1:])
            file.write(str(avg_student) + '\n')
        subj1 = 0
        subj2 = 0
        subj3 = 0
        for el in lst:                              # count sum for column                  
            subj1 += el[1]
            subj2 += el[2]
            subj3 += el[3]
        avg_subj1 = subj1 / len(lst)
        avg_subj2 = subj2 / len(lst)
        avg_subj3 = subj3 / len(lst)
        fin_s = f'{avg_subj1} {avg_subj2} {avg_subj3}'
        file.write(fin_s)

def main():
    path_in = "path_to_in"
    path_out = "path_to_putput"
    lst = create_lst(path_in)        # create unsorted list from data from file
    write_to_file(path_out, lst)


if __name__ == "__main__":
    main()

