def area(a: float) -> float:
    """
    Считает площадь квадрата по длине стороны a.

    Формула: S = a²

    Args:
        a (float): длина стороны

    Returns:
        float: площадь квадрата

    Example:
        >>> area(5)
        25
    """
    return a * a


def perimeter(a: float) -> float:
    """
    Считает периметр квадрата по длине стороны a.

    Формула: P = 4a

    Args:
        a (float): длина стороны

    Returns:
        float: периметр квадрата

    Example:
        >>> perimeter(5)
        20
    """
    return 4 * a
