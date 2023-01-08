# Here you can find functions to calculate:
# Rectangle: area and circuit
# Square: area and circuit
# Triangle: area and circuit
#   b * h * 0.5
#   (s * (s - a) * (s - b) * (s - c)) ** 0.5
#   a * b * sin(ab) * 0.5
#   (a * b * c) / 4 * R
#   2 * R * R * sin(ab) * sin(bc) * sin(ca)
#   r * ((a + b + c) / 2)
# Trapeze: area and circuit
# Circle: area and circuit
# Polygon: area and circuit


import math


def rectangle_area(first_side=1, second_side=1):
    """Get the rectangle area.

    Args:
        first_side (int): length of shorter side of rectangle
        second_side (int): length of longer side of rectangle

    Returns:
        int: rectangle area
    """
    return first_side * second_side


def rectangle_circuit(first_side=1, second_side=1):
    """Get the rectangle circuit.

    Args:
        first_side (int): length of shorter side of rectangle
        second_side (int): length of longer side of rectangle

    Returns:
        int: rectangle circuit
    """
    return first_side * 2 + second_side * 2


def square_area(side_length=1):
    """Get the square area.

    Args:
        side_length (int): length of side of square

    Returns:
        int: square area
    """
    return side_length * side_length


def square_circuit(side_length=1):
    """Get the square circuit.

    Args:
        side_length (int): length of side of square

    Returns:
        int: square circuit
    """
    return side_length * 4


def triangle_area(first_side_length=0, height_to_first_side=0,
                  sec_side_len=0, third_side_len=0,
                  first_angle_rad=0, second_angle_rad=0,
                  third_angle_rad=0, radius_out_circle=0,
                  radius_in_circle=0):
    """Get the triangle area.

    Function uses 6 different ways:
    1. a * h
    2. a * b * c
    3. a * b * angle(ab)
    4. (a * b * c) / (4 * R)
    5. 2 * R^2 * sin(ab) * sin(bc) * sin(ca)
    6. r * ((a + b + c) / 2)

    Args:
        first_side_length (int, optional):
            length of first side of triangle (a). Defaults to 0.
        height_to_first_side (int, optional):
            length of height of triangle (h). Defaults to 0.
        sec_side_len (int, optional):
            length of second side of triangle (b). Defaults to 0.
        third_side_len (int, optional):
            length of third side of triangle (c). Defaults to 0.
        first_angle_rad (int, optional):
            length of first angle of triangle (ab). Defaults to 0.
        second_angle_rad (int, optional):
            length of second angle of triangle (bc). Defaults to 0.
        third_angle_rad (int, optional):
            length of third angle of triangle (ca). Defaults to 0.
        radius_out_circle (int, optional):
            length of outer circle radius (R). Defaults to 0.
        radius_in_circle (int, optional):
            length of inner circle radius (r). Defaults to 0.

    Returns:
        int or float: triangle area
    """

    # a * h
    if first_side_length != 0 and height_to_first_side != 0:
        return first_side_length * 0.5 * height_to_first_side
    # a * b * c
    elif first_side_length != 0 and sec_side_len != 0 and third_side_len != 0:
        p = (first_side_length + sec_side_len + sec_side_len) * 0.5
        return (p * (p - first_side_length) * (p - sec_side_len)
                * (p - sec_side_len)) ** 0.5
    # a * b * angle(ab)
    elif first_side_length != 0 and sec_side_len != 0 \
            and first_angle_rad != 0:
        return (first_side_length * sec_side_len *
                math.sin(first_angle_rad)) * 0.5
    # (a * b * c) / (4 * R)
    elif first_side_length != 0 and sec_side_len != 0 and third_side_len != 0 \
            and radius_out_circle != 0:
        return (first_side_length * sec_side_len *
                sec_side_len) / (4 * radius_out_circle)
    # 2 * R^2 * sin(a) * sin(b) * sin(c)
    elif first_angle_rad != 0 and second_angle_rad != 0 \
            and third_angle_rad != 0 and radius_out_circle != 0:
        return 2 * (radius_out_circle ** 2) * math.sin(first_angle_rad) * \
            math.sin(second_angle_rad) * math.sin(third_angle_rad)
    # r * ((a + b + c) / 2)
    elif first_side_length != 0 and sec_side_len != 0 and third_side_len != 0 \
            and radius_in_circle != 0:
        return radius_in_circle * \
            ((first_side_length + sec_side_len + sec_side_len) / 2)
    # other
    else:
        return 0


def triangle_circuit(first_side_len=1, second_side_len=1, thr_side_len=1):
    """Gets the triangle circuit.

    Args:
        first_side_len (int, optional): length of first side. Defaults to 1.
        second_side_len (int, optional): length of second side. Defaults to 1.
        thr_side_len (int, optional): length of third side. Defaults to 1.

    Returns:
        int: triangle circuit
    """
    return first_side_len + second_side_len + thr_side_len


def trapeze_area(first_basis_length=1, second_basis_length=1, height=1):
    """Gets the trapeze area.

    Args:
        first_basis_length (int, optional):
            length of top basis. Defaults to 1.
        second_basis_length (int, optional):
            length of bottom basis. Defaults to 1.
        height (int, optional):
            height of trapeze. Defaults to 1.

    Returns:
        int: trapeze area
    """
    return (first_basis_length + second_basis_length) * height / 2


def trapeze_circuit(first_side_length=1, first_basis_length=1,
                    second_basis_length=1, second_side_length=1):
    """Gets the trapeze circuit.

    Args:
        first_side_length (int, optional):
            length of left side. Defaults to 1.
        first_basis_length (int, optional):
            length of top basis. Defaults to 1.
        second_basis_length (int, optional):
            length of bottom basis. Defaults to 1.
        second_side_length (int, optional):
            length of right side. Defaults to 1.

    Returns:
        int: trapeze circuit
    """
    if (second_basis_length == 1 and second_side_length == 1):
        return first_basis_length * 2 + first_side_length * 2
    elif (second_side_length == 0):
        return first_basis_length + second_basis_length + first_side_length * 2
    else:
        return first_basis_length + second_basis_length + \
            first_side_length + second_side_length


def circle_area(radius=1):
    """Gets the circle area.

    Args:
        radius (int, optional): radius of circuit. Defaults to 1.

    Returns:
        float: circle area
    """
    return math.pi * radius * radius


def circle_circuit(radius=1):
    """Gets the circle circuit.

    Args:
        radius (int, optional): radius of circuit. Defaults to 1.

    Returns:
        float: circle circuit
    """
    return math.pi * 2 * radius


def polygon_area(num_of_sides=4.0, polygon_side_len=1.0,
                 diagonal_len=1.42, polygon_height=1.0):
    """Gets the polygon area.

    Args:
        num_of_sides (float, optional):
            number of all sides. Defaults to 4.0.
        polygon_side_len (float, optional):
            length of single side. Defaults to 1.0.
        diagonal_len (float, optional):
            length of diagonal. Defaults to 1.42.
        polygon_height (float, optional):
            length of height. Defaults to 1.0.

    Returns:
        float: polygon area
    """
    if num_of_sides != 0 and polygon_side_len != 0 and diagonal_len != 0:
        p = (polygon_side_len + diagonal_len) * 0.5
        d = (p * (p - polygon_side_len) * ((p - diagonal_len / 2) ** 2))
        return num_of_sides * (d ** 0.5)
    elif num_of_sides != 0 and polygon_side_len != 0 and polygon_height != 0:
        return num_of_sides * polygon_side_len * polygon_height * 0.25
    else:
        return 0


def polygon_circuit(number_of_sides=3, polygon_side_length=1):
    """Gets the polygon circuit.

    Args:
        number_of_sides (int, optional):
            number of all sides. Defaults to 3.
        polygon_side_length (int, optional):
            length of single side. Defaults to 1.

    Returns:
        int: polygon circuit
    """
    return number_of_sides * polygon_side_length
