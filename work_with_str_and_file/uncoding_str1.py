"""
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
"""

def extract_symbols(path_to_file):
    """
    Func extract from file 2 lists
    :return:
    lst_alpha - list with alpha
    lst_digit - list with digits
    """
    lst_alpha = []
    lst_digit = []
    s1 = ''
    with open(path_to_file) as f:
        s = f.readline()
        print(s)
        for i in range(len(s)):
            if s[i].isalpha():
                lst_alpha.append(s[i])
                if i == 0:
                    continue
                else:
                    lst_digit.append(s1)
                    s1 = ""
            else:
                if s[i] == s[-1]:
                    lst_digit.append(s1)
                else:
                    s1 += s[i]
    return lst_alpha, lst_digit

def construct_str(alpha, digits):
    """
    Func construct final string, based on two lists
    :param alpha: list with letters
    :param digits: list with digits
    :return: s: final string
    """
    s = ''
    for i in range(len(alpha)):
        s += alpha[i] * digits[i]
    return s

def write_str_2file(path_out, fin_str):
    """
    Write final string to file
    :param path_out: path to output file
    :param fin_str:  final string
    :return:
    """
    with open(path_out, 'w') as file:
        file.write(fin_str)

def main():
    path_in = "path_to_input_file"
    path_out = "path_to_output_file"
    alpha, digits = extract_symbols(path_in)   # extract separate lists with letters and numbers
    digits = list(map(int, digits))            # convert list values to numbers
    print(alpha)
    print(digits)
    fin_str = construct_str(alpha, digits)     # construct final string
    print(fin_str)
    write_str_2file(path_out, fin_str)


if __name__ == "__main__":
    main()

