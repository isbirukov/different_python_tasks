"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:

Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.
"""


def lst_2_num(lst):
    """
    Change to int numbers in list in game
    :param lst:
    :return:
    """
    new_lst = []
    for i in range(len(lst)):
        if i in (1, 3):
            new_lst.append(int(lst[i]))
        else:
            new_lst.append(lst[i])
    return new_lst


def add_points(dict_teams, team, point):
    # првоерка на то, существует ли команда в словаре
    if team not in dict_teams.keys():
        dict_teams[team] = [0, 0, 0, 0, 0]
    if point == 3:      # если команда победила
        dict_teams[team][0] += 1
        dict_teams[team][1] += 1
        dict_teams[team][4] += 3
    elif point == 1:    # если ничья
        dict_teams[team][0] += 1
        dict_teams[team][2] += 1
        dict_teams[team][4] += 1
    else:               # если команда проиграла
        dict_teams[team][0] += 1
        dict_teams[team][3] += 1




def compute_result_game(dict_teams, team_win, team_fall, draw):
    if draw == 1:   # если ничья, то добавляем каждо йкоманде по 1 очку
        add_points(dict_teams, team_win, 1)
        add_points(dict_teams, team_fall, 1)
    else:
        add_points(dict_teams, team_win, 3)     # иначе побеждившей команде - 3 очка
        add_points(dict_teams, team_fall, 0)    # проигравшей команде - 0 очков



def main():
    finished_games = int(input())
    teams = {}
    for i in range(finished_games):
        tmp = input().split(";")
        lst_with_numbers = lst_2_num(tmp)
        if lst_with_numbers[1] > lst_with_numbers[3]:
            compute_result_game(teams, lst_with_numbers[0], lst_with_numbers[2], 0)
        elif lst_with_numbers[3] > lst_with_numbers[1]:
            compute_result_game(teams, lst_with_numbers[2], lst_with_numbers[0], 0)
        else:
            compute_result_game(teams, lst_with_numbers[0], lst_with_numbers[2], 1)
    for k, v in teams.items():
        print(k, end=':')
        print(*v)


if __name__ == "__main__":
    main()