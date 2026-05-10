import tkinter as tk

from interfaz import Aplicacion


def main():

    root = tk.Tk()

    app = Aplicacion(root)

    root.mainloop()


if __name__ == "__main__":
    main()