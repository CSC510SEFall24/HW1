"""This module implements merge sort algorithm and demonstrates its usage"""

import rand


def merge_sort(input_arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        input_arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left sorted array.
        right_arr (list): The right sorted array.

    Returns:
        list: The merged and sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
