def sum_of_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_of_numbers(numbers[1:])

print(sum_of_numbers([1,2,3,4,5]))