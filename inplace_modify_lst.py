"""
�������� ������� modify_list(l), ������� ��������� �� ���� ������ ����� �����,
������� �� ���� ��� �������� ��������, � ������ ������ ����� �� ���.
������� �� ������ ������ ����������, ��������� ������ ��������� ����������� ������, ��������:
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
"""

def modify_list(l):
    # put your python code here
    a = []
    for el in l:
        if el % 2 == 0:
            a.append(el//2)
    l.clear()
    l.extend(a)




def main():
    lst = [10, 5, 8, 3]
    print(modify_list(lst))
    print(lst)


if __name__ == '__main__':
    main()



