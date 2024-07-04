from graphics import Window, Line, Point

if __name__ == "__main__":
  win = Window(800, 600)
  line_a = Line(
    Point(250, 250),
    Point(500, 500)
  )
  line_b = Line(
    Point(350, 150),
    Point(720, 400)
  )
  win.draw_line(line_a, "black")
  win.draw_line(line_b, "red")
  win.wait_for_close()