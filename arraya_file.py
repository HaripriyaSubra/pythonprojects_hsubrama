def remove_duplicates(numbers_array_with_duplicates):
    non_dup_array = []
    for num in numbers_array_with_duplicates:
        if num not in non_dup_array:
            non_dup_array.append(num)
    return non_dup_array


def sort_ascending(numbers):
    sorted_array = sorted(numbers)
    return sorted_array


def sort_descending(numbers):
    sorted_array = sorted(numbers, reverse=True)
    return sorted_array



