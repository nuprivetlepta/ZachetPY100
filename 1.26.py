if __name__ == "__main__":

    vklad = int(input('Введите сумму вклада в рублях:'))
    term = int(input('Введите срок вклада в месяцах:'))
    koef = 0
    if term == 6:
        koef = 0.06
    elif term == 12:
        koef = 0.08
    percent = vklad * koef
    print("Сумма ежемесячного начисления:", percent, "рублей", sep=' ')
