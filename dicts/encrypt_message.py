"""
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики:
они говорили каким-то странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр,
т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ
к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы
исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка,
которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:

*d*%*d*#*d*
dacabac
Sample Input 2:

dcba
badc
dcba
badc
Sample Output 2:

badc
dcba
"""


def encryption(dict_enc, string_enc):
    """
    Func for string encryption
    :param dict_enc: dict with set for enc
    :param string_enc: string for encryption
    :return: encryption string
    """
    enc_s = []
    for i in string_enc:
        enc_s.append(dict_enc[i])
    enc_s = ''.join(enc_s)
    return enc_s


def decryption(dict_enc, string_dec):
    """
    Func for string decryption
    :param dict_enc: dict with set for dec
    :param string_dec: string for encryption
    :return: decryption string
    """
    dec_s = []
    for i in string_dec:
        for k, v in dict_enc.items():
            if i == v:
                dec_s.append(k)
    dec_s = ''.join(dec_s)
    return dec_s


def main():
    source_alphabet = list(input())
    final_alphabet = list(input())
    string_for_enc = list(input())
    string_for_dec = list(input())

    dict_4_enc_dec = dict(zip(source_alphabet, final_alphabet))  # словарь, определяющий шифр
    enc_string = encryption(dict_4_enc_dec, string_for_enc)  # шфирование строки
    dec_string = decryption(dict_4_enc_dec, string_for_dec)  # дешфирование строки
    print(enc_string)
    print(dec_string)


if __name__ == "__main__":
    main()
