from graphics import Point, Line

class Cell:
  def __init__(self, win=None):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._y1 = None
    self._x2 = None
    self._y2 = None
    self._win = win

  def draw(self, x1, y1, x2, y2):
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2

    if self.has_left_wall:
      self._win.draw_line(
        Line(Point(x1, y1), Point(x1, y2))
      )

    if self.has_right_wall:
      self._win.draw_line(
        Line(Point(x2, y1), Point(x2, y2))
      )

    if self.has_top_wall:
      self._win.draw_line(
        Line(Point(x1, y1), Point(x2, y1))
      )

    if self.has_bottom_wall:
      self._win.draw_line(
        Line(Point(x1, y2), Point(x2, y2))
      )

  def draw_move(self, to_cell, undo=False):
    from_x = (self._x2 + self._x1) / 2
    from_y = (self._y2 + self._y1) / 2

    to_x = (to_cell._x2 + to_cell._x1) / 2
    to_y = (to_cell._y2 + to_cell._y1) / 2


    fill_colour = "gray" if undo else "red"

    self._win.draw_line(Line(Point(from_x, from_y), Point(to_x, to_y)), fill_colour)
