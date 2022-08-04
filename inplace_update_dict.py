"""
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа:
keykey и valuevalue.

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь и сопоставить ему список из
переданного элемента [value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}"""

def update_dictionary(d, key, value):
    # put your python code here
    if key not in d:
        if 2*key not in d:
            d[2 * key] = [value]
        else:
            lst = d[2 * key]
            lst.append(value)
            d[2 * key] = lst
    else:
        lst = d[key]
        lst.append(value)
        d[key] = lst


def main():
    d = {}
    print(update_dictionary(d, 1, -1))  # None
    print(d)  # {2: [-1]}
    update_dictionary(d, 2, -2)
    print(d)  # {2: [-1, -2]}
    update_dictionary(d, 1, -3)
    print(d)  # {2: [-1, -2, -3]}


if __name__ == '__main__':
    main()



