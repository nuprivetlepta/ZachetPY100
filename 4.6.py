# Дан одномерный массив. Переставить в обратном порядке элементы массива,
# расположенные между минимальным и максимальным элементами.
if __name__ == "__main__":

    mass = [1, 2, 3, 5, 16, 88, 2]
    max_ = max(mass)
    min_ = min(mass)
    min_index = 0
    max_index = 0
    for index, value in enumerate(mass):   # Находим индексы максимального и минимального значения
        if value == max_:
            max_index = index
        elif value == min_:
            min_index = index
    if max_index < min_index:               # Выполняем условие, чтобы диапазон индексов был возрастающим.
        min_index, max_index = max_index, min_index
    part_1 = mass[:min_index+1]     # Создаём список элементов до первой границы включительно
    part_2 = mass[max_index-1: min_index: -1]     # Создаём список элементов между границами
    part_3 = mass[max_index::]     # Создаём список элементов после второй границы включительно

    print(part_1 + part_2 + part_3)
