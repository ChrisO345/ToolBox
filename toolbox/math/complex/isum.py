IterableGroup = list | tuple | set
i_Num = int | float | complex


def isum(*numbers: IterableGroup | i_Num) -> i_Num:
    """
    TODO: docstrings

    :param numbers:
    :return:
    """
    if len(numbers) == 1:
        numbers = numbers[0]
    total: i_Num = 0
    for item in numbers:
        if isinstance(item, i_Num):
            total += item
            continue
        if isinstance(item, IterableGroup):
            total += isum(item)
            continue
        types = str(type(item)).split()[1][:-1:], str(type(total)).split()[1][:-1:]
        types_error = f"unsupported operand type(s) for +: {types[0]} and {types[1]}"
        raise TypeError(types_error)
    return total
