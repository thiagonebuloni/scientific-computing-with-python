def merge_sort(array: list[int | float]) -> None:
    """Merge sort algorithm.

    Args:
        array: list[int | float]
    Returns:
        None
    """
    if len(array) <= 1:
        return

    middle_point: int = len(array) // 2
    left_part: list[int | float] = array[:middle_point]
    right_part: list[int | float] = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index: int = 0
    right_array_index: int = 0
    sorted_index: int = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == "__main__":
    numbers = [4, 10.5, 6, 14, 2, 1, 8, 5]
    print("Unsorted array: ")
    print(numbers)
    merge_sort(numbers)
    print("Sorted array: " + str(numbers))
