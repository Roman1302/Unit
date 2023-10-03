class Numeric_lists:
    def __init__(self, lst1: list[int | float], lst2: list[int | float]):
        self.lst1 = lst1
        self.lst2 = lst2

    def get_lists_averages(self) -> tuple[float, float]:
        avg1 = 0
        if self.lst1:
            avg1 = sum(self.lst1) / len(self.lst1)

        avg2 = 0
        if self.lst2:
            avg2 = sum(self.lst2) / len(self.lst2)

        return avg1, avg2

    def compare_averages(self) -> None:
        avg1, avg2 = self.get_lists_averages()
        if avg1 > avg2:
            print('Список 1 имеет большее среднее значение')
        elif avg1 < avg2:
            print('Список 2 имеет большее среднее значение')
        else:
            print('Значения списков равны')
