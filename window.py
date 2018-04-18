import tkinter
from translator import fuzuli


class Window:
    window = None
    grid_size = 0
    symbols = 0
    holes = 0
    textboxes = []

    def __init__(self, grid_size, symbols, holes):
        self.window = tkinter.Tk()
        self.window.geometry('600x400+60+30')
        self.generate_controls(grid_size)
        self.symbols = symbols
        self.holes = holes

    # Create all textboxes and buttons
    def generate_controls(self, length):
        margin = 40
        for i in range(length):
            for j in range(length):
                tbox = tkinter.Entry(self.window)
                tbox.place(x=margin + j * 40, y=margin + i * 40,
                           height=25, width=25)
                self.textboxes.append(tbox)

        button = tkinter.Button(text="Generate")
        button.place(x=length * 40 + margin + 60, y=margin + 40,
                     width=100, height=25)

        # Add event to the button
        button.bind('<Button 1>', lambda event: self.fuzuli(event))

    def mainloop(self):
        self.window.mainloop()

    # Call an outside function to create a script
    def fuzuli(self, event):
        sym, hol, grid = self.get_data()
        fuzuli(sym + hol, sym, grid)

    # Retrieve data from grid
    def get_data(self):
        grid = [x.get() for x in self.textboxes]
        return self.symbols, self.holes, grid
