def number(num):
    str_num = str(num)
    rev_num = int(str_num[::-1])
    sum_num_rev = num + rev_num
    return all(int(digit) % 2 != 0 for digit in str(sum_num_rev))


def count_reversible_numbers(limits):
    count = 0
    for num in range(1, limits):
        if num % 10 != 0 and number(num):
            count += 1
    return count


limit = 10000000
result = count_reversible_numbers(limit)
print("Количество обратимых чисел <1000000000:", result)
