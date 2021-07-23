import numpy as np
from colormap import rgb2hex


def find_top_colors(image):
    data = np.asarray(image)
    # Get all color data
    color_data = []
    for row in data:
        for column in row:
            color_data.append(column)

    # Count number of different colors
    color_dict = {}
    for color in color_data:
        color = tuple(color.tolist())
        if color not in color_dict:
            color_dict[color] = 1
        else:
            color_dict[color] = color_dict[color] + 1

    # Get Top 10 Colors
    top_colors = sorted(color_dict, key=color_dict.get, reverse=True)[:10]
    print(top_colors)

    # Covert colors from RGB to HEX
    top_colors_hex = [rgb2hex(color[0], color[1], color[2]) for color in top_colors]
    print(top_colors_hex)

    return top_colors_hex