"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""

def create_lst(path_in):
    """
    Func reads strings from file and creates list
    :param path_in: path to file
    :return: list, based on data from file
    """
    lst = []
    with open(path_in) as file:
        for line in file:
            lst.append(line.strip())
    return lst

def write_to_file(path_out, lst):
    """
    Func writes to file
    :param path_out: path to output file
    :param lst: list with data for computing
    :return:
    """
    reverse_lst = lst[::-1]
    with open(path_out, 'w') as file:
        for el in reverse_lst:                              # count avg for student
            file.write(el + '\n')


def main():
    path_in = "path_to_in"
    path_out = "path_to_putput"
    lst = create_lst(path_in)        # create unsorted list from data from file
    write_to_file(path_out, lst)


if __name__ == "__main__":
    main()