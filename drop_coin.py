import random as rd

def get_lottery_numbers():
    numbers = set()
    while len(numbers) < 7:  # пока в списке меньше 7 чисел
        num = rd.randint(1, 49)
        numbers.add(num)
    return numbers

sort_numbers = sorted(get_lottery_numbers())

print(*sort_numbers)