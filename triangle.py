def perimeter(a: float, b: float, c: float) -> float:
    """
    Считает периметр треугольника по всем его сторонам.

    Формула: P = a + b + c

    Args:
        a (float): первая сторона треугольника
        b (float): вторая сторона треугольника
        c (float): третья сторона треугольника

    Returns:
        float: периметр треугольника

    Example:
        >>> perimeter(1, 1, 1)
        3
    """
    return a + b + c


def area(a: float, h: float) -> float:
    """
    Считает площадь треугольника по стороне и высоте, опущенной на эту сторону.

    Формула: S = (a * h) / 2

    Args:
        a (float): сторона треугольника
        h (float): высота, опущенная на a

    Returns:
        float: площадь треугольника

    Example:
        >>> area(1, 2)
        1.0
    """
    return (a * h) / 2
