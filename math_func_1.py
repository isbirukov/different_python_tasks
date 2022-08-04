"""
�������� ������� f(x), ������� ���������� �������� ��������� �������, ����������� �� ���� �������� ������:
1 - ( x + 2) **2, ��� � <= -2
-x/2, ��� -2 < x <= 2
(x - 2)**2 + 1, ��� 2 < x
"""

def f(x):
    # put your python code here
    if x <= -2:
        return 1 - (x + 2)**2
    elif -2 < x <= 2:
        return -x/2
    else:
        return (x - 2)**2 + 1

def main():
    print(f(1))


if __name__ == '__main__':
    main()
