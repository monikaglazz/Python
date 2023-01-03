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


def rectangle_area(first_side, second_side):
    """Function returns rectangle area"""
    return first_side * second_side


def rectangle_circuit(first_side, second_side):
    """Function returns rectangle circuit"""
    return first_side * 2 + second_side * 2


def square_area(side_length):
    """Function returns square area"""
    return side_length * side_length


def square_circuit(side_length):
    """Function returns square circuit"""
    return side_length * 4


def triangle_area(first_side_length=0, height_to_first_side=0,
                  sec_side_len=0, third_side_len=0,
                  first_angle_rad=0, second_angle_rad=0,
                  third_angle_rad=0, radius_out_circle=0,
                  radius_in_circle=0):
    """Function returns triangle area in one of six different ways:
    1. a * h
    2. a * b * c
    3. a * b * angle(ab)
    4. (a * b * c) / (4 * R)
    5. 2 * R^2 * sin(a) * sin(b) * sin(c)
    6. r * ((a + b + c) / 2)"""

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


def triangle_circuit(first_side_length, second_side_length, third_side_length):
    """Function returns triangle circuit"""
    return first_side_length + second_side_length + third_side_length


def trapeze_area(first_basis_length, second_basis_length, height):
    """Function returns trapeze area"""
    return (first_basis_length + second_basis_length) * height / 2


def trapeze_circuit(first_side_length, first_basis_length,
                    second_basis_length=0, second_side_length=0):
    """Function returns trapeze circuit"""
    if (second_basis_length == 0 and second_side_length == 0):
        return first_basis_length * 2 + first_side_length * 2
    elif (second_side_length == 0):
        return first_basis_length + second_basis_length + first_side_length * 2
    else:
        return first_basis_length + second_basis_length + \
            first_side_length + second_side_length


def circle_area(radius):
    """Function returns circle area"""
    return math.pi * radius * radius


def circle_circuit(radius):
    """Function returns circle circuit"""
    return math.pi * 2 * radius


def polygon_area(num_of_sides=0, polygon_side_len=0,
                 diagonal_len=0, polygon_height=0):
    """Function returns polygon area"""
    if num_of_sides != 0 and polygon_side_len != 0 and diagonal_len != 0:
        p = (polygon_side_len + diagonal_len) * 0.5
        d = (p * (p - polygon_side_len) * ((p - diagonal_len / 2) ** 2))
        return num_of_sides * (d ** 0.5)
    elif num_of_sides != 0 and polygon_side_len != 0 and polygon_height != 0:
        return num_of_sides * polygon_side_len * polygon_height * 0.25
    else:
        return 0


def polygon_circuit(number_of_sides=0, polygon_side_length=0):
    """Function returns polygon circuit"""
    return number_of_sides * polygon_side_length
