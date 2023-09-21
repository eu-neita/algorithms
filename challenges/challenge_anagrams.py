def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


def custom_sort(s):
    return merge_sort(list(s))


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return first_string, second_string, False

    first_normalized = custom_sort(first_string.lower().replace(" ", ""))
    second_normalized = custom_sort(second_string.lower().replace(" ", ""))

    return (
        ''.join(first_normalized),
        ''.join(second_normalized),
        first_normalized == second_normalized,
    )
