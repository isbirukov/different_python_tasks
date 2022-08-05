"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку
ещё какое-то количество монет, не превышая ее вместимость.

Класс должен иметь следующий вид

class MoneyBox:
    def __init__(self, capacity):
    # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        # положить v монет в копилку
"""


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_volume = 0

    def can_add(self, v):
        if (self.current_volume + v) > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        self.current_volume = self.current_volume + v

def main():
    c = MoneyBox(10)
    c.add(5)
    c.add(5)
    print(c.current_volume)


if __name__ == '__main__':
    main()
