class Rectangle:

    def overlaps(self, rect):
        cond_1 = False
        cond_2 = False
        cond_3 = False
        cond_4 = False

        if self.get_left_x() <= rect.get_right_x():
            cond_1 = True
        if self.get_right_x() >= rect.get_left_x():
            cond_2 = True
        if self.get_top_y() >= rect.get_bottom_y():
            cond_3 = True
        if self.get_bottom_y() <= rect.get_top_y():
            cond_4 = True
        return cond_1 and cond_2 and cond_3 and cond_4

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"