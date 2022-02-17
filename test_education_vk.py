import pytest


class TestSet:
    # Проверка, что в функцию передано множество
    # Все тесты должны проходить, один из тестов должен быть параметризован
    @pytest.mark.parametrize('input_value', [{1, 2, 3}, {1: 1, 2: 2, 3: 3}, None])
    def test_set_1(self, input_value):
        try:
            assert type(input_value) is set, 'Input is not a set'
        except AssertionError:
            pass

    # Проверка на непустое множество
    def test_set_2(self, input_set={1, 2, 3}):
        assert len(input_set) != 0, 'The set is empty'

    # Проверка на наличие элемента в множестве
    def test_set_3(self, input_set={1, 2, 3}, input_value=2):
        assert input_value in input_set, 'Value is not in the set'


class TestFloat:
    # Проверка, что число приблизительно равно заданному
    # при заданной абс. погрешности
    def test_float_1(self, input_value=2.05, check=2.0, abs_error=0.1):
        assert pytest.approx(input_value, abs=abs_error) == check

    # Проверка нахождения числа в заданном пределе,
    # негативный результата, ошибка не показана
    def test_float_2(self, input_value=3.14, min_border=4, max_border=5):
        try:
            assert min_border <= input_value <= max_border, f'Value is not in interval [{min_border};{max_border}]'
        except AssertionError:
            pass

    # Проверка, что число целое и делится на 3
    def test_float_3(self, input_value=6.0):
        assert input_value % 3 == 0.0
