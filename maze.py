import time
from cell import Cell

class Maze:
  def __init__(self,
    x1,
    y1,
    num_rows,
    num_cols,
    cell_size_x,
    cell_size_y,
    win=None,
  ):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win

    self.create_cells()
    self.break_entrance_and_exit()

  def create_cells(self):
    for i in range(self._num_cols):
      col = []
      for j in range(self._num_rows):
        col.append(Cell(self._win))
      self._cells.append(col)

    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self.draw_cell(i, j)

  def draw_cell(self, i, j):
    if self._win is None:
      return

    x1 = self._x1 + (i * self._cell_size_x)
    y1 = self._y1 + (j * self._cell_size_y)
    x2 = x1 + self._cell_size_x
    y2 = y1 + self._cell_size_y
    self._cells[i][j].draw(x1, y1, x2, y2)
    self.animate()
  
  def animate(self):
    if self._win is None:
      return
    self._win.redraw()
    time.sleep(0.05)

  def break_entrance_and_exit(self):
    maze_entrance = self._cells[0][0]
    maze_exit = self._cells[self._num_cols - 1][self._num_rows - 1]

    maze_entrance.has_top_wall = False
    maze_exit.has_bottom_wall = False

    self.draw_cell(0, 0)
    self.draw_cell(self._num_cols - 1, self._num_rows - 1)



