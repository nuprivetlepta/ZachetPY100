# Гипотеза Сиракуз гласит, что любое натуральное число сводимо к единице при следующих действиях над ним:
# а) если число четное, то разделить его пополам,
# б) если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.
# Над вновь полученным числом вновь повторить действия
# a) или б) в зависимости от его четности. Рано или поздно число станет равным 1.
if __name__ == "__main__":
    a = int(input())
    counter = 0
    while a != 1:
        if a % 2 == 0:
            a /= 2
            counter += 1
        elif a % 2 != 0:
            a = (a * 3 + 1) / 2
            counter += 1

    print('Количество действий до приведения:', counter, sep=' ')