class Unit:
    """
        Base class representing a unit in a 2D coordinate system.

        A unit is typically represented as a point on the map.

        Attributes:
        -----------
        - name (str): The name of the unit.
        - pos_x (float): The x-coordinate position of the unit.
        - pos_y (float): The y-coordinate position of the unit.

        Methods:
        --------
        - in_area(x1, y1, x2, y2): Checks if the unit (as a point) is within a specified rectangular area.
        """

    def __init__(self, name, pos_x, pos_y):
        """
        Initializes a Unit object.

        Parameters:
        -----------
        - name (str): Name of the unit.
        - pos_x (float): The x-coordinate position of the unit.
        - pos_y (float): The y-coordinate position of the unit.
        """
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        """
        Determines whether the unit is inside a given rectangular area.

        Parameters:
        -----------
        - x1, y1 (float): Coordinates of the bottom-left corner of the area.
        - x2, y2 (float): Coordinates of the top-right corner of the area.

        Returns:
        --------
        - bool: True if the unit is within the given area, False otherwise.
        """
        pass


class Dragon(Unit):
    """
    Represents a Dragon unit, which extends the Unit class.

    Unlike regular units represented as points, a Dragon is represented as a rectangle
    due to its larger size on the map.

    Attributes:
    -----------
    - fire_range (float): The range within which the dragon can attack using fire.
    - height (float): The height of the dragon.
    - width (float): The width of the dragon.
    - __hit_box (Rectangle): A rectangle defining the dragon’s occupied space based on its position and size.

    Methods:
    --------
    - in_area(x1, y1, x2, y2): Checks if the dragon's hitbox overlaps with another rectangular area (e.g., another dragon).
    """

    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        """
        Initializes a Dragon object.

        Parameters:
        -----------
        - name (str): The name of the dragon.
        - pos_x (float): The x-coordinate of the dragon (center of its hitbox).
        - pos_y (float): The y-coordinate of the dragon (center of its hitbox).
        - height (float): The height of the dragon.
        - width (float): The width of the dragon.
        - fire_range (float): The range within which the dragon can attack using fire.
        """
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(pos_x - self.width / 2, pos_y - self.height / 2, pos_x + self.width / 2,
                                   pos_y + self.height / 2)

    def in_area(self, x1, y1, x2, y2):
        """
        Determines whether the dragon's hitbox overlaps with a given rectangular area.

        This function can be used to check collisions with another Dragon, interaction
        with an attack zone, or movement restrictions.

        Parameters:
        -----------
        - x1, y1 (float): Bottom-left corner coordinates of the area.
        - x2, y2 (float): Top-right corner coordinates of the area.

        Returns:
        --------
        - bool: True if the dragon's hitbox overlaps with the area, False otherwise.
        """
        r1 = Rectangle(x1, y1, x2, y2)
        return r1.overlaps(self.__hit_box)


class Rectangle:
    """
    Represents a rectangle in a 2D coordinate system.

    This is used to represent areas occupied by dragons and to check for overlaps
    (e.g., collision detection or area control).

    Attributes:
    -----------
    - __x1, __y1 (float): Coordinates of the first corner.
    - __x2, __y2 (float): Coordinates of the opposite corner.

    Methods:
    --------
    - overlaps(rect): Checks if the rectangle overlaps with another rectangle.
    - get_left_x(): Returns the leftmost x-coordinate.
    - get_right_x(): Returns the rightmost x-coordinate.
    - get_top_y(): Returns the highest y-coordinate.
    - get_bottom_y(): Returns the lowest y-coordinate.
    """
    def overlaps(self, rect):
        """
        Determines if this rectangle overlaps with another rectangle.

        This function is used for collision detection between dragons or checking
        interactions with specific map regions.

        Parameters:
        -----------
        - rect (Rectangle): Another rectangle to check for overlap.

        Returns:
        --------
        - bool: True if the rectangles overlap, False otherwise.
        """
        return (
                self.get_left_x() <= rect.get_right_x()
                and self.get_right_x() >= rect.get_left_x()
                and self.get_top_y() >= rect.get_bottom_y()
                and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        """Returns the leftmost x-coordinate of the rectangle."""
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        """Returns the rightmost x-coordinate of the rectangle."""
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        """Returns the highest y-coordinate of the rectangle."""
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        """Returns the highest y-coordinate of the rectangle."""
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2


if __name__ == '__main__':
    run_cases = [
        (Dragon("Green Dragon", -1, -2, 1, 2, 1), -2, -3, 0, 0, True),
        (Dragon("Red Dragon", 2, 2, 2, 2, 2), 0, 1, 1, 0, True),
        (Dragon("Blue Dragon", 4, -3, 2, 1, 1), -5, -5, 5, 5, True),
        (Dragon("Silver Dragon", 0, 0, 5, 5, 10), 4, 0, 5, 1, False),
        (Dragon("Gold Dragon", 0, 0, 5, 5, 10), 4, 0, 5, 1, False),
        (Dragon("Gold Dragon", 0, 0, 20, 20, 20), 10, 10, 20, 20, True),
    ]
