# Определить, сколько в введенном пользователем числе четных цифр, а сколько нечетных.
if __name__ == "__main__":
    a = (input())
    odd = 0
    even = 0
    list_ = [int(x) for x in str(a)]
    for i in list_:
        if i != 0:
            if i % 2 == 0:
                even += 1
            elif i % 2 != 0:
                odd += 1.
    print('Количество нечетных символов:', int(odd), sep=' ')
    print('Количество четных символов:', int(even), sep=' ')
