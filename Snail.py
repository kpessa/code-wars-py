def snail(snail_map):
    """

    >>> snail([[1,2,3],[4,5,6],[7,8,9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

    >>> snail([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    """
    import numpy as np

    res = []

    array = np.array(snail_map)

    while array.size > 0:
        res.extend(array[0])
        array = np.rot90(array[1:])

    return res


# def snail(snailmap):
#     """
#     :param snailmap: list of lists
#     :return: list of integers

#     >>> snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     [1, 2, 3, 6, 9, 8, 7, 4, 5]

#     >>> snail([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#     [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

#     """

#     result = []
#     while snailmap:
#         result.extend(snailmap.pop(0))
#         if snailmap:
#             for row in snailmap:
#                 result.append(row.pop())
#             result.extend(snailmap.pop()[::-1])
#             if snailmap:
#                 for row in snailmap[::-1]:
#                     result.append(row.pop(0))
#     return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
