import tkinter as tk

import settings


class Cell:
  def __init__(self, parent: tk.Tk, row: int, column: int, alive: bool=False) -> None:
    self.alive: bool = alive
    self.nbrs: list[Cell] = []
    self.coords = (row, column)
    self.obj = tk.Button(parent, bg=getColour(alive))
    self.obj.config(command=self.buttonClicked)
    self.obj.grid(row=row, column=column)

  def buttonClicked(self) -> None:
    print(f"Button @ {self.coords} clicked.")
    print(f"Current state: {self.alive}")
    self.alive = not self.alive
    print(f"New state: {self.alive}")
    self.obj.config(bg=getColour(self.alive))

  def changeState(self, alive: bool) -> None:
    self.alive = alive
    self.obj.config(bg=getColour(self.alive))

  def update(self) -> None:
    alive: int = 0
    
    for nbr in self.nbrs:
      try:
        if nbr.alive: alive += 1
      except Exception as e:
        continue

    if self.alive and alive > 3:
      self.changeState(alive=False)
      print("Changed state: " + str(self))
      return
    if self.alive and alive < 2:
      self.changeState(alive=False)
      print("Changed state: " + str(self))
      return
    if self.alive and alive in (2, 3):
      return
    if not self.alive and alive == 3:
      print("Changed state: " + str(self))
      self.changeState(alive=True)
      return
    return

  def __str__(self) -> str:
    return f"Cell @ {self.coords}: Alive = {self.alive}"
    


def getColour(alive: bool = False) -> str:
  if settings.custom_colour_mode and settings.dark_mode:
    return settings.custom_dark_dead if not alive else settings.custom_dark_alive

  if not settings.custom_colour_mode and settings.dark_mode:
    return "#231942" if not alive else "#84C4EB"

  if settings.custom_colour_mode and not settings.dark_mode:
    return settings.custom_light_dead if not alive else settings.custom_light_alive

  if not settings.custom_colour_mode and not settings.dark_mode:
    return "#FFEEDD" if not alive else "#38686A"
    
  raise ValueError("Settings are invalid")


def main() -> None:
  root = tk.Tk()
  cells = []
  for row in range(25):
    cells.append([])
    for column in range(50):
      cells[row].append(Cell(root, row, column))

  setNbrs(cells)

  submitBtn = tk.Button(root, text="Save and start")
  submitBtn.config(command=lambda: run(root, cells, submitBtn))
  submitBtn.grid(row=settings.maxHeight-1, column=settings.maxWidth)

  root.mainloop()


def run(root, cells, submitBtn):
  for row in cells:
    for cell in row:
      cell.obj.config(state=tk.DISABLED)

  submitBtn.destroy()
  
  
  while True:
    for row in cells:
      for cell in row:
        root.after(1000, cell.update)




def setNbrs(cells: list[Cell]) -> None:
  for rowIndex, row in enumerate(cells):
    for colIndex, cell in enumerate(row):
      for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
          adj_row = rowIndex + dy
          adj_col = colIndex + dx

          if adj_row == rowIndex and adj_col == colIndex:
            continue
          
          # Check if adjacent cell indices are within bounds
          if 0 <= adj_row < settings.maxHeight and 0 <= adj_col < settings.maxWidth:
            cell.nbrs.append(cells[adj_row][adj_col])
    


def getAlive(cells: list[Cell]) -> list[Cell]:
  alive = []
  for row in cells:
    for cell in row:
      if cell.alive:
        alive.append(cell)

  return alive
  
main()
      