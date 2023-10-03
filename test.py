import pytest

from average import Numeric_lists


@pytest.fixture
def list1():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list2():
    return [2, 3, 4, 5, 6]


def test_init(list1, list2):
    """Проверка корректной класса"""
    nums_list = Numeric_lists(list1, list2)
    assert nums_list.lst1 == list1
    assert nums_list.lst2 == list2


def test_get_lists_averages(list1, list2):
    """Проверка средних значений больше единицы"""
    nums_list = Numeric_lists(list1, list2)
    assert nums_list.get_lists_averages() == (3, 4)


@pytest.mark.parametrize('lst1, lst2, result', [([1, 2, 3], [], (2, 0)), ([], [1, 2, 3], (0, 2)), ([], [], (0, 0))])
def test_get_empty_lists_averages(lst1, lst2, result):
    """Проверка средних значений списка на пустые"""
    nums_list = Numeric_lists(lst1, lst2)
    assert nums_list.get_lists_averages() == result


@pytest.mark.parametrize('lst1, lst2, result', [([1, 2, 3], [5], (2, 5)), ([5], [1, 2, 3], (5, 2)), ([5], [5], (5, 5))])
def test_get_one_elemented_lists_averages(lst1, lst2, result):
    """Проверка средних значений только один элемент"""
    nums_list = Numeric_lists(lst1, lst2)
    assert nums_list.get_lists_averages() == result


def test_first_average_more(list1, list2, capfd):
    """Проверка сообщения значение списка 1 больше списка 2"""
    nums_list = Numeric_lists(list2, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Список 1 имеет большее среднее значение'


def test_second_average_more(list1, list2, capfd):
    """Проверка сообщения, когда среднее значение списка 2 больше списка 1"""
    nums_list = Numeric_lists(list1, list2)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Список 2 имеет большее среднее значение'


def test_equal_averages(list1, capfd):
    """Проверка сообщения, когда средние значения списков равны"""
    nums_list = Numeric_lists(list1, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Значения списков равны'