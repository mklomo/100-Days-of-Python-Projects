"""
    This script implements a python project to extract the colors from
    the flumequine Painting by Hirst

"""

import colorgram

# This function returns a named tuple
flumequine_colors = colorgram.extract("Damien-Hirst-spots-Flumequine.jpeg", 34)


# Creating a list of the named_color_tuples

flumequine_colors_list = []

for color_index in range(1, 34):
    color = flumequine_colors[color_index].rgb
    r = color.r
    g = color.g
    b = color.b
    color_tuple = (r, g, b)
    flumequine_colors_list.append(color_tuple)

# Output GLOBAL Variables

# Background color RGB
BACKGROUND_COLOR = (flumequine_colors[0].rgb.r, flumequine_colors[0].rgb.g, flumequine_colors[0].rgb.b)

# List of Dot Colors
DOT_COLORS_LIST = flumequine_colors_list
