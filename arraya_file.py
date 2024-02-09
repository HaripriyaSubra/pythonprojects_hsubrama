numbers = [1, 2, 3, 3, 5, 6, 2, 1]


def remove_duplicates(numbers_array_with_duplicates):
    non_dup_array = []
    for num in numbers_array_with_duplicates:
        if num not in non_dup_array:
            non_dup_array.append(num)
    return non_dup_array


