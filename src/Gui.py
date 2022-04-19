import os.path
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MenuBar(ttk.Frame):

    def __init__(self, container):
        super(MenuBar, self).__init__(container)

        self.scan_button = MenuButton(master=self, text="Scan")
        self.scan_button.grid(column=0, row=0)

        self.scan_button = MenuButton(master=self, text="Run")
        self.scan_button.grid(column=1, row=0)

        self.scan_button = MenuButton(master=self,
                                      text="Add Mapping",
                                      command=lambda: AddMappingDialog(self, "Add mapping.."))
        self.scan_button.grid(column=2, row=0)

        self.scan_button = MenuButton(master=self, text="Quit")
        self.scan_button.grid(column=3, row=0)


class AddMappingDialog(simpledialog.Dialog):

    def __init__(self, parent, title):
        super().__init__(parent, title)
        self.in_dir = None
        self.out_dir = None
        self.video_output_resolution = None
        self.audio_bitrate = None
        self.video_bitrate = None
        self.encoding_preset = None
        self.output_file_ext = None
        self.input_file_types = []
        self.postfix_filenames_with = None
        self.mapping_name = None
        #self.geometry("600x400")

    def select_in_dir(self):
        dirname = filedialog.askdirectory(
            title='Open a dir',
            initialdir=os.path.expanduser("~"))
        self.in_dir = dirname
        self.in_dir_text_var.set(self.in_dir or "In dir..")

    def select_out_dir(self):
        dirname = filedialog.askdirectory(
            title='Open a dir',
            initialdir=os.path.expanduser("~"))
        self.out_dir = dirname
        self.out_dir_text_var.set(self.in_dir or "Out dir..")

    def body(self, frame):
        pad = 5

        self.in_dir_label = ttk.Label(frame, text="Input folder: ")
        self.in_dir_label.grid(column=0, row=0, sticky="W", padx=pad, pady=pad)
        self.in_dir_text_var = tk.StringVar()
        self.in_dir_text_var.set("In dir..")
        self.in_dir_select = ttk.Button(frame,
                                        textvariable=self.in_dir_text_var,
                                        command=self.select_in_dir)
        self.in_dir_select.grid(column=1, row=0, sticky="W", padx=pad, pady=pad)

        self.out_dir_label = ttk.Label(frame, text="Output folder: ")
        self.out_dir_label.grid(column=0, row=1, sticky="W", padx=pad, pady=pad)
        self.out_dir_text_var = tk.StringVar()
        self.out_dir_text_var.set("Out dir..")
        self.out_dir_select = ttk.Button(frame,
                                         textvariable=self.out_dir_text_var,
                                         command=self.select_out_dir)
        self.out_dir_select.grid(column=1, row=1, sticky="W", padx=pad, pady=pad)



class JobsContainer(ttk.Frame):

    def __init__(self, container):
        super(JobsContainer, self).__init__(container)
        self.job = Job("foo.avi", "foo_discord.mp4", 50)
        self.job.grid(column=0, row=1, columnspan=4)


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
        self.open_folder_button.grid(column=0, row=0, sticky="NS")

        self.open_folder_button = OpenFolderButton(master=self, text="Open Target Folder")
        self.open_folder_button.grid(column=1, row=0, sticky="NS")

        self.gauge = JobGauge(master=self, mask=f"{percent}%")
        self.gauge.grid(column=2, row=0, sticky="NS")

        self.description = ttk.Label(master=self, text=f"{from_file} => {to_file}",
                                     font=(None, 18, "normal"),
                                     padding=(20, 0, 0, 0))
        self.description.grid(column=3, row=0, sticky="NS")

        self.gauge.update_gauge(percent)


class VideoConvertor(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = ttk.Style("darkly")

        self.title("VideoConvertor")
        self.geometry("1024x768")

        self.menu_bar = MenuBar(self)
        self.menu_bar.grid(column=0, row=0, sticky="EW")

        self.top_bar = JobsContainer(self)
        self.top_bar.grid(column=0, row=1)


