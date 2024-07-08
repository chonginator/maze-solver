import time
import random
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
    seed=None,
  ):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win

    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)

    if seed:
      random.seed(seed)

  def _create_cells(self):
    for i in range(self._num_cols):
      col = []
      for j in range(self._num_rows):
        col.append(Cell(self._win))
      self._cells.append(col)

    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._draw_cell(i, j)

  def _draw_cell(self, i, j):
    if self._win is None:
      return

    x1 = self._x1 + (i * self._cell_size_x)
    y1 = self._y1 + (j * self._cell_size_y)
    x2 = x1 + self._cell_size_x
    y2 = y1 + self._cell_size_y
    self._cells[i][j].draw(x1, y1, x2, y2)
    self._animate()
  
  def _animate(self):
    if self._win is None:
      return
    self._win.redraw()
    time.sleep(0.005)

  def _break_entrance_and_exit(self):
    maze_entrance = self._cells[0][0]
    maze_exit = self._cells[self._num_cols - 1][self._num_rows - 1]

    maze_entrance.has_top_wall = False
    maze_exit.has_bottom_wall = False

    self._draw_cell(0, 0)
    self._draw_cell(self._num_cols - 1, self._num_rows - 1)

  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True

    while True:
      unvisited = []

      if i > 0 and not self._cells[i - 1][j].visited:
        unvisited.append((i - 1, j))
      if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
        unvisited.append((i + 1, j))
      if j > 0 and not self._cells[i][j - 1].visited:
        unvisited.append((i, j - 1))
      if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
        unvisited.append((i, j + 1))

      if len(unvisited) == 0:
        self._draw_cell(i, j)
        return

      next_i, next_j = random.choice(unvisited)

      self._break_wall(i, j, next_i, next_j)
      self._break_walls_r(next_i, next_j)
  
  def _break_wall(self, i, j, next_i, next_j):
    if next_i == i - 1:
      self._cells[i][j].has_left_wall = False
      self._cells[next_i][next_j].has_right_wall = False
    if next_i == i + 1:
      self._cells[i][j].has_right_wall = False
      self._cells[next_i][next_j].has_left = False
    if next_j == j - 1:
      self._cells[i][j].has_top_wall = False
      self._cells[next_i][next_j].has_bottom_wall = False
    if next_j == j + 1:
      self._cells[i][j].has_bottom_wall = False
      self._cells[next_i][next_j].has_top_wall = False
