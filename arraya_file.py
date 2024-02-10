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


def sum_average_elements_array(numbers):
    sum_elements = sum(numbers)
    average = sum(numbers) / len(numbers)
    return sum_elements, average


def has_greater_element(numbers, value):
    if len(numbers) == 0:
        return False
    for number in numbers:
        if number > value:
            return True
    return False


def are_sum_two_lists_equal(list1, list2):
    if not list1 or not list2:
        return False
    return sum(list1) == sum(list2)