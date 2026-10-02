def area(a: float, b: float) -> float:
    """
    Считает площадь прямоугольника по длинам двух смежных сторон a и b.

    Формула: S = a * b

    Args:
        a (float): длина прямоугольника
        b (float): ширина прямоугольника

    Returns:
        float: площадь прямоугольника

    Example:
        >>> area(3, 4)
        12
    """
    return a * b


def perimeter(a: float, b: float) -> float:
    """
    Считает периметр прямоугольника по длинам двух смежных сторон a и b.

    Формула: P = 2(a + b)

    Args:
        a (float): длина прямоугольника
        b (float): ширина прямоугольника

    Returns:
        float: периметр прямоугольника

    Example:
        >>> perimeter(3, 4)
        14
    """
    return 2 * (a + b)
