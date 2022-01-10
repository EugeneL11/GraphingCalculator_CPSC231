# COURSE: CPSC 231 FALL 2021
# Name: Eugene Lee
# INSTRUCTOR: Jonathan Hudson
# Tutorial: Zack Hassan - T04
# ID: 30137489
# Date: Oct. 22nd, 2022
# Description: This code will take the x,y coordinates of an origin, the ratio of pixels per step,
# and various arithmetic expressions and graph them on a cartesian plane with axis and labelled ticks

from math import *
import turtle

# Constants
BACKGROUND_COLOR = "white"
WIDTH = 800
HEIGHT = 600
AXIS_COLOR = "black"
TICK = 5
DELTA = 0.1
LABEL_SIZE = 7
# These following constants are each there to fix the offset of the labels on the axis, found through trial and error
X_AXIS_OFFSET_FIX = 20
Y_AXIS_OFFSET_FIX_X = 15
Y_AXIS_OFFSET_FIX_Y = -7


def get_color(equation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """
    # Dividing using % 3 to make this if statement work for infinitely many expressions, alternating colors accordingly
    equation_number = equation_counter % 3
    if equation_number == 0:
        color = "red"
    elif equation_number == 1:
        color = "green"
    else:
        color = "blue"
    return color


def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    # This function converts the calculator coordinate value into a value on the actual screen, for various upcoming uses
    screen_x = x_origin + ratio * x
    screen_y = y_origin + ratio * y
    return screen_x, screen_y


def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """
    # This is derived by doing reverse algebra on the calc_to_screen_coord calculation
    x_min = int(floor((0 - x_origin) / ratio))
    x_max = int(ceil((WIDTH - x_origin) / ratio))
    return x_min, x_max


def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """
    # This is also derived by doing reverse algebra on the calc_to_screen_coord calculation
    y_min = int(floor((0 - y_origin) / ratio))
    y_max = int(ceil((HEIGHT - y_origin) / ratio))
    return y_min, y_max


def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between tow pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """
    # This function will be used to draw a line between two points when called, so just have to make the pointer
    # move from initial point to final point with pen down
    pointer.penup()
    pointer.goto(screen_x1, screen_y1)
    pointer.pendown()
    pointer.goto(screen_x2, screen_y2)
    pointer.penup()


def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    pointer.pencolor(AXIS_COLOR)
    # Adding and subtracting TICK from the screen_y will allow a straight line to be drawn as
    # an actual tick ultimately the size of 2 * TICK in each screen_x value
    draw_line(pointer, screen_x, screen_y + TICK, screen_x, screen_y - TICK)


def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.pencolor(AXIS_COLOR)
    # This function is meant to write the appropriate x values as text, which will be the labels to the ticks
    pointer.goto(screen_x, screen_y - X_AXIS_OFFSET_FIX)
    pointer.write(label_text, align="center", font=("Arial", LABEL_SIZE, "normal"))


def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    pointer.pencolor(AXIS_COLOR)
    # Adding and subtracting TICK from the screen_x will allow a straight line to be drawn as
    # an actual tick ultimately the size of 2 * TICK in each screen_y value
    draw_line(pointer, screen_x - TICK, screen_y, screen_x + TICK, screen_y)


def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.pencolor(AXIS_COLOR)
    # This function is meant to write the appropriate y values as text, which will be the labels to the ticks
    pointer.goto(screen_x + Y_AXIS_OFFSET_FIX_X, screen_y + Y_AXIS_OFFSET_FIX_Y)
    pointer.write(label_text, align="center", font=("Arial", LABEL_SIZE, "normal"))


def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    # This is a very important function that takes the functions created up to this point in order to create the
    # actual x axis that will show up on the turtle screen, with ticks and labels following the correct ratio

    # Two local variables introduced to represent the return values of the called function, so that we can use them
    min_x_value, max_x_value = calc_minmax_x(x_origin, ratio)
    # Need to convert the calculator coordinates into the actual screen coordinates so they can be used in the
    # following functions. Can't just use calculator values as its proportions are completely different
    screen_cord_x1, screen_cord_y1 = calc_to_screen_coord(min_x_value, 0, x_origin, y_origin, ratio)
    screen_cord_x2, screen_cord_y2 = calc_to_screen_coord(max_x_value, 0, x_origin, y_origin, ratio)
    draw_line(pointer, screen_cord_x1, screen_cord_y1, screen_cord_x2, screen_cord_y2)
    # A for loop is called in order to draw the ticks and labels evenly without having to code each one
    # separately within the specified interval
    for i in range(0, screen_cord_x2 + ratio, ratio):
        draw_x_axis_tick(pointer, screen_cord_x1, y_origin)
        draw_x_axis_label(pointer, screen_cord_x1, y_origin, min_x_value)
        screen_cord_x1 += ratio
        min_x_value += 1


def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    # This is a very important function that takes the functions created up to this point in order to create the
    # actual y axis that will show up on the turtle screen, with ticks and labels following the correct ratio

    # Two local variables introduced to represent the return values of the called function, so that we can use them
    min_y_value, max_y_value = calc_minmax_y(y_origin, ratio)
    # Need to convert the calculator coordinates into the actual screen coordinates so they can be used in the
    # following functions. Can't just use calculator values as its proportions are completely different
    screen_cord_x1, screen_cord_y1 = calc_to_screen_coord(0, min_y_value, x_origin, y_origin, ratio)
    screen_cord_x2, screen_cord_y2 = calc_to_screen_coord(0, max_y_value, x_origin, y_origin, ratio)
    draw_line(pointer, screen_cord_x1, screen_cord_y1, screen_cord_x2, screen_cord_y2)
    # A for loop is called in order to draw the ticks and labels evenly without having to code each one
    # separately within the specified interval
    for i in range(0, screen_cord_y2 + ratio, ratio):
        draw_y_axis_tick(pointer, x_origin, screen_cord_y1)
        draw_y_axis_label(pointer, x_origin, screen_cord_y1, min_y_value)
        screen_cord_y1 += ratio
        min_y_value += 1


def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    pointer.pencolor(colour)
    # Two local variables introduced to represent the return values of the called function, so that we can use them
    min_x_value, max_x_value = calc_minmax_x(x_origin, ratio)
    # The while loop is called here, which will allow us to draw many small lines the size of DELTA, and they
    # connect with one another to make a curve that looks as smooth as one continuous line
    while min_x_value <= max_x_value:
        x1 = min_x_value
        x2 = x1 + DELTA
        y1 = calc(expr, x1)
        y2 = calc(expr, x2)
        # Need to convert calculator coordinates into screen coordinates once again to draw each tiny lines properly
        screen_x1, screen_y1 = calc_to_screen_coord(x1, y1, x_origin, y_origin, ratio)
        screen_x2, screen_y2 = calc_to_screen_coord(x2, y2, x_origin, y_origin, ratio)
        draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2)
        min_x_value += DELTA


# YOU SHOULD NOT NEED TO CHANGE ANYTHING BELOW THIS LINE UNLESS YOU ARE DOING THE BONUS


def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)
    """
    return eval(expr)


def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    # turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))
    ratio = int(input("Enter ratio of pixels per step: "))
    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    # turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while expr != "":
        # Get colour and draw expression
        colour = get_color(equation_counter)
        draw_expression(pointer, expr, colour, x_origin, y_origin, ratio)
        # turtle.update()
        expr = input("Enter an arithmetic expression: ")
        equation_counter += 1


main()
turtle.exitonclick()
