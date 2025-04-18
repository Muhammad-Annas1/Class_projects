def add_many_numbers(numbers)-> int:

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    number: list[int] = [1, 2, 3, 4, 5]
    sum_of_number: int = add_many_numbers(number)
    print (sum_of_number)


if __name__ == '__main__':
    main()