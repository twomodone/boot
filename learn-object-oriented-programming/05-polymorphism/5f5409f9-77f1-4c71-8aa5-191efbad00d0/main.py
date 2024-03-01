class Rectangle:
    def overlaps(self, rect):
        return (
            rect.get_left_x() <= self.get_right_x() and
            rect.get_right_x() >= self.get_left_x() and
            rect.get_bottom_y() <= self.get_top_y() and 
            rect.get_top_y() >= self.get_bottom_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        if self.x1 < self.x2:
            return self.x1
        return self.x2

    def get_right_x(self):
        if self.x1 > self.x2:
            return self.x1
        return self.x2

    def get_top_y(self):
        if self.y1 > self.y2:
            return self.y1
        return self.y2

    def get_bottom_y(self):
        if self.y1 < self.y2:
            return self.y1
        return self.y2
