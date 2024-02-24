def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def bug():
    while True:
        number = input("введите число : ")
        if not number.isdecimal() or int(number) < 2:
            print("вы ввели либо букву, либо числа < 2!")
            continue
        else:
            number = int(number)
            break

    if is_prime(number):
        print(f'{number} - простое число')
    else:
        print(f'{number} - составное число')


bug()
