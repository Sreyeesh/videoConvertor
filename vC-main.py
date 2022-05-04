from ttkbootstrap.utility import enable_high_dpi_awareness
from src.Gui import VideoConvertor
from tkinter import *

if __name__ == "__main__":
    enable_high_dpi_awareness()
    root_window = VideoConvertor()
    root_window.mainloop()
