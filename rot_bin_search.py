from random import randint


def find(l, e):
    """

    :param l: List of sorted unique integers possibly rotated by an unknown amount
    :param e: Element in the list to find the index of
    :return: Index of e in l
    """
    return search(l, start=0, end=len(l)-1, e=e)


def search(l, start, end, e):

    if start > end:
        # We need the stat to be lower than the end for the method to work
        return -1

    # integer division to get the mid point
    mid = (start + end) // 2

    # If the element is at the mid point then return this
    if l[mid] == e:
        return mid

    # If l[start, ..., mid] is sorted
    if l[start] <= l[mid]:

        # As this sub list is sorted, we can quickly check if e lies in this half or the other half
        if l[start] <= e <= l[mid]:
            return search(l, start, mid - 1, e)

        return search(l, mid + 1, end, e)

    # If l[start, ..., mid] is not sorted, then l[mid, ..., end] must be sorted
    elif l[mid] <= e <= l[end]:
        return search(l, mid + 1, end, e)

    return search(l, start, mid - 1, e)


def run_simple_tests():
    simple_test(calculated_result=find([5, 6, 8, 13, 21, 1, 3], 13), expected_result=3)
    simple_test(calculated_result=find([5, 6, 8, 13, 21, 1, 3], 6), expected_result=1)

    def rotate(l, x):
        """
        rotate array l by x elements to the right
        :param l: list of integers
        :param x: number of elements to rotate l by to the right
        :return: rotated list
        """
        return l[-x % len(l):] + l[:-x % len(l)]

    # Generate fairly large rotated lists and use the python index method on the list to check the result
    for _ in range(10):
        start = 0
        size = 100000
        long_list = list(range(start, size))
        element = randint(start, size)
        rotation = randint(-1*size, size)
        rotated_long_list = rotate(long_list, x=rotation)
        index_value = rotated_long_list.index(element)
        simple_test(calculated_result=find(rotated_long_list, element), expected_result=index_value)

    # For repeated elements the solution is sub-optimal in that for this case:
    simple_test(calculated_result=find([5, 6, 6, 6, 13, 21, 1, 3], 6), expected_result=3)
    # it finds the last repeated element, but for this case:
    simple_test(calculated_result=find([5, 6, 13, 21, 1, 1, 1, 3], 1), expected_result=5)
    # it finds the second repeated element


def simple_test(calculated_result, expected_result):
    print("Testing {} == {}".format(calculated_result, expected_result))
    assert calculated_result == expected_result, "Calculated: <{calculated}> does not equal expected <{expected}>".format(
        calculated=calculated_result, expected=expected_result
    )
    print("Test successful !")


if __name__ == "__main__":
    run_simple_tests()
