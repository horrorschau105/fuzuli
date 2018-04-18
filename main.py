from sys import argv, exit
from window import Window

if __name__ == '__main__':
    if len(argv) < 3:
        print('Using: python3 main.py <#symbols> <#holes>')
        exit(0)

    # Get parameters
    symbols, holes = int(argv[1]), int(argv[2])
    grid_length = symbols + holes

    # Call the window
    h_window = Window(grid_length, symbols, holes)
    h_window.mainloop()
