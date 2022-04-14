import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *




class TopBar(ttk.Frame):

    def __init__(self, container):
        super(TopBar, self).__init__(container)
        # Them buttons
        self.scan_button = MenuButton(master=self, text="Scan")
        self.scan_button.pack(side="left")
        self.scan_button = MenuButton(master=self, text="Run")
        self.scan_button.pack(side="left")
        self.scan_button = MenuButton(master=self, text="Add Mapping")
        self.scan_button.pack(side="left")
        self.scan_button = MenuButton(master=self, text="Quit")
        self.scan_button.pack(side="right")


class MainContainer(ttk.Frame):

    def __init__(self, container):
        super(MainContainer, self).__init__(container)
        self.job = Job("foo.avi", "foo_discord.mp4", 50)
        self.job.pack(side="top")


class MenuButton(ttk.Button):

    def __init__(self, *args, **kwargs):
        super(MenuButton, self).__init__(*args, **kwargs)


class OpenFolderButton(ttk.Button):

    def __init__(self, *args, **kwargs):
        super(OpenFolderButton, self).__init__(*args, **kwargs)


class JobGauge(ttk.Floodgauge):

    def __init__(self, *args, **kwargs):
        super(JobGauge, self).__init__(*args, **kwargs, bootstyle=INFO,
                                       font=(None, 13, 'bold'))

    def update_gauge(self, val):
        self.configure(value=50)



class Job(ttk.Frame):

    def __init__(self, from_file: str, to_file: str, percent: int, *args, **kwargs):
        super().__init__(*args, **kwargs, padding=(10, 10, 10, 10))
        self.percent = percent
        self.to_file = to_file
        self.from_file = from_file

        self.open_folder_button = OpenFolderButton(master=self, text="Open Source Folder")
        self.open_folder_button.pack(side="left", fill="y")

        self.open_folder_button = OpenFolderButton(master=self, text="Open Target Folder")
        self.open_folder_button.pack(side="left", fill="y")

        self.gauge = JobGauge(master=self, mask=f"{percent}%")
        self.gauge.pack(side="left", fill="y")

        self.description = ttk.Label(master=self, text=f"{from_file} => {to_file}",
                                     font=(None, 18, "normal"),
                                     padding=(20, 0, 0, 0))
        self.description.pack(side="left")

        self.gauge.update_gauge(percent)


class VideoConvertor(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = ttk.Style("darkly")

        self.title("VideoConvertor")
        self.geometry("1024x768")

        self.top_bar = TopBar(self)
        self.top_bar.pack(side="top", anchor="n")

        self.top_bar = MainContainer(self)
        self.top_bar.pack(side="top")


