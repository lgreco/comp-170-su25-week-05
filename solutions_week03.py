def draw_diamond(height: int, mark: str = "#", space: str = " ") -> None:
    """Nothing is as simple as it appears!

    Consider two diamond shapes with heights 5 and 6 respectively:
      #                  #
     ###                ###
    #####              #####
     ###               #####
      #                 ###
                         #
    (height = 5)      (height = 6)

    We notice that when the diamond's height is an odd number, the shape is
    shaper. When the height is even the diamond has two middle lines. With
    the exception of the middle line(s), the rest of the shape looks easy to
    code. Otherwise the two shapes are identical. This observation allows a
    simple design: to treat even heights as odd heights with an additional
    middle line. In other words, a diamond 6 lines in height is the same as
    a diamong 5 lines in height plus an additional middle line.
    """
    # Determine if height is even
    double_middle = height % 2 == 0
    if double_middle:
        # if height is even, reduce it to odd.
        height -= 1  # show-off way to wright height = height-1

    # Find half point
    half = height // 2

    # Top half (excluding middle line)
    for line in range(0, half):
        spaces = space * (half - line)
        marks = mark * (2 * line + 1)
        print(spaces + marks + spaces)

    # Print an extra middle line if needed (when height even)
    if double_middle:
        print(mark * height)

    # Bottom half (incuding one middle line)
    for line in range(half, height):
        spaces = space * (line - half)
        marks = mark * (2 * (height - line - 1) + 1)
        print(spaces + marks + spaces)
    # end draw_diamond


def draw_right_triangle(height: int, mark: str = "#", space: str = " ") -> None:
    """This is quite simple. But it may get a bit more complex if the user wishes
    to select which side of the triangles base will have the right angle. For example:

    #        Easy to                     A bit more       #
    ##       draw                      difficult to      ##
    ###      triangle                     draw with     ###
    ####     with right                 right angle    ####
    #####    angle to                        to its   #####
    ######   its left                         right  ######

    If you had to, how would you change the code to provide an option for right
    angle on the left or the right of the triangle's base?
    """
    for line in range(height):
        spaces = space * (height - 1 - line)
        marks = mark * (1 + line)
        print(marks + spaces)
    # end draw_right_triangle


def compound_interest(principal: float, rate: float, years: int) -> float:
    """Straight forward! For every year, we multiply the principal by itself
    plus the interest rate:
    principal = (1 + rate)
    and this becomes the new principal for the next iteration"""
    for year in range(years):
        principal = (1 + rate) * principal
    return principal
    # end compound_interest


def draw_hollow_square(
    size: int = 8, thickness: int = 2, mark: str = "#", space: str = " "
) -> None:
    """The simplicity of this method is based on the realization that we use
    just two types of line to pring. For example, using a (4,2) hollow square:

    ****    <-- full line
    *  *    <-- hollow line
    *  *    <-- hollow line
    ****    <-- full line

    Our task then becomes to compute the two types of lines and determine which
    one to print when during a for-loop.
    """
    # Compute print elements once -- no need to compute these inside the loop as they are remain unchanged.
    full_line = mark * size
    hollow_line = (
        (mark * thickness) + (space * (size - 2 * thickness)) + (mark * thickness)
    )
    # Iterate over the height of the shape
    for line in range(size):
        # Check if we are priting full or edge lines
        if line < thickness or line >= size - thickness:
            # Print full line
            print(full_line)
        else:
            # Print hollowed out line
            print(hollow_line)
    # end draw_hollow_square

# Test diamond shape:
draw_diamond(-1)  # nothing to see
draw_diamond(0)  # nothing to see
draw_diamond(1)  # single character diamond
draw_diamond(10)  # double middle line with 4 lines above and below
draw_diamond(11)  # single middle line with 5 lines above and below
draw_diamond(
    11, mark=" ", space="+"
)  # should be invert diamond but right side spaces usually are misssing

# Test right triangle
draw_right_triangle(10)

# Test compound interest
print(compound_interest(1000, 0.05, 5))

# Test holllow square
draw_hollow_square()
