IterableGroup = list | tuple | set
num = int | float


def mult(*numbers: IterableGroup | num) -> num:
    """
    TODO: docstrings

    :param numbers:
    :return:
    """
    if len(numbers) == 1:
        numbers = numbers[0]
    total: num = 1
    for item in numbers:
        if isinstance(item, num):
            total *= item
            continue
        if isinstance(item, IterableGroup):
            total *= mult(item)
            continue
        types = str(type(item)).split()[1][:-1:], str(type(total)).split()[1][:-1:]
        types_error = f"unsupported operand type(s) for *: {types[0]} and {types[1]}"
        raise TypeError(types_error)
    return total
