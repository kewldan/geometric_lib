import math


def area(r: float) -> float:
    """
    Считает площадь круга по радиусу r.

    Формула: S = πR²

    Args:
        r (float): радиус круга

    Returns:
        float: площадь круга

    Example:
        >>> area(2)
        12.566370614359172
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Считает длину окружности (периметр круга) по радиусу r.

    Формула: P = 2πR

    Args:
        r (float): радиус круга

    Returns:
        float: периметр круга

    Example:
        >>> perimeter(2)
        12.566370614359172
    """
    return 2 * math.pi * r
