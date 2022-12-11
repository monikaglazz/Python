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


# Function to get rectangle area
def rectangle_area(first_side, second_side):
    return first_side * second_side


# Function to get rectangle circuit
def rectangle_circuit(first_side, second_side):
    return first_side * 2 + second_side * 2


# Function to get square area
def square_area(side_length):
    return side_length * side_length


# Function to get square circuit
def square_circuit(side_length):
    return side_length * 4


# Function to get triangle area
def triangle_area(first_side_length=0, height_to_first_side=0, 
                  second_side_length=0, third_side_length=0,
                  angle_between_sides_rad=0, second_angle_rad=0, 
                  third_angle_rad=0, radius_out_circle=0,
                  radius_in_circle=0):
    if first_side_length != 0 and height_to_first_side != 0:
        return first_side_length * 0.5 * height_to_first_side
    elif first_side_length != 0 and second_side_length != 0 and third_side_length != 0:
        p = (first_side_length + second_side_length + second_side_length) * 0.5
        return (p * (p - first_side_length) * (p - second_side_length) * (p - second_side_length)) ** 0.5
    elif first_side_length != 0 and second_side_length != 0 and angle_between_sides_rad != 0:
        return (first_side_length * second_side_length * math.sin(angle_between_sides_rad)) * 0.5
    elif first_side_length != 0 and second_side_length != 0 and second_side_length != 0 and radius_out_circle != 0:
        return (first_side_length * second_side_length * second_side_length) / (4 * radius_out_circle)
    elif angle_between_sides_rad != 0 and second_angle_rad != 0 and third_angle_rad != 0 and radius_out_circle != 0:
        return 2 * (radius_out_circle ** 2) * math.sin(angle_between_sides_rad) * math.sin(second_angle_rad) * math.sin(
            third_angle_rad)
    elif first_side_length != 0 and second_side_length != 0 and second_side_length != 0 and radius_in_circle != 0:
        return radius_in_circle * ((first_side_length + second_side_length + second_side_length) / 2)
    else:
        return 0


# Function to get triangle circuit
def triangle_circuit(first_side_length, second_side_length, third_side_length):
    return first_side_length + second_side_length + third_side_length


# Function to get trapeze area
def trapeze_area(first_basis_length, second_basis_length, height):
    return (first_basis_length + second_basis_length) * height / 2


# Function to get trapeze area
def trapeze_circuit(first_side_length, first_basis_length, second_basis_length=0, second_side_length=0):
    if (second_basis_length == 0 and second_side_length == 0):
        return first_basis_length * 2 + first_side_length * 2
    elif (second_side_length == 0):
        return first_basis_length + second_basis_length + first_side_length * 2
    else:
        return first_basis_length + second_basis_length + first_side_length + second_side_length


# Function to get circle area
def circle_area(radius):
    return math.pi * radius * radius


# Function to get circle circuit
def circle_circuit(radius):
    return math.pi * 2 * radius


# Function to get polygon area
def polygon_area(number_of_sides=0, polygon_side_length=0, diagonal_length=0, polygon_height=0):
    if number_of_sides != 0 and polygon_side_length != 0 and diagonal_length != 0:
        p = (polygon_side_length + diagonal_length) * 0.5
        return number_of_sides * ((p * (p - polygon_side_length) * ((p - diagonal_length / 2) ** 2)) ** 0.5)
    elif number_of_sides != 0 and polygon_side_length != 0 and polygon_height != 0:
        return number_of_sides * polygon_side_length * polygon_height * 0.25
    else:
        return 0


# Function to get polygon circuit
def polygon_circuit(number_of_sides=0, polygon_side_length=0):
    return number_of_sides * polygon_side_length
