class Color:
    """
    A class representing a color in RGB format.
    """
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def format(self, string):
        """
        Return the given string formatted with the RGB color values.
        """
        return f"\033[38;2;{self.r};{self.g};{self.b}m{string}\033[0m"


# Define a dictionary of color objects for convenience
style_colors = {
    "lilac": Color(204, 204, 255),
    "pink": Color(255, 204, 255),
    "pale_red": Color(255, 102, 102),
    "bright_green": Color(178, 255, 102)
}