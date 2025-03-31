def generator_str_in_len(text_list: list) -> list:
    '''
    функция преобразует записи списка в их длины
    '''
    lengths_text_list = [len(text) for text in text_list]
    return lengths_text_list


def avg_length_list(lengths_text_list: list) -> float:
    '''
    функция находит среднеарифметическое значение списка
    '''
    return sum(lengths_text_list) / len(lengths_text_list)


def min_diff(avg_length_list, text_list: list) -> float:
    '''
    функция находит мин разницу в списке от переданного значения
    '''
    min_diff = min(abs(lenght - avg_length_list) for lenght in text_list)
    return min_diff


def list_generator(text_list, avg_length_list, min_diff):
    '''
    функция фильтрует список относительно числа
    '''
    return [name for name in text_list if abs(len(name) - avg_length_list) == min_diff]
