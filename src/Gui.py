import os.path
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.DirsSettings import DirsSettings


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
        #self.geometry("600x400")

    def select_in_dir(self):
        dirname = filedialog.askdirectory(
            title='Open in folder',
            initialdir=os.path.expanduser("~"))
        self.in_dir = dirname
        self.in_dir_text_var.set(self.in_dir or "In dir..")

    def select_out_dir(self):
        dirname = filedialog.askdirectory(
            title='Open out folder',
            initialdir=os.path.expanduser("~"))
        self.out_dir = dirname
        self.out_dir_text_var.set(self.out_dir or "Out dir..")

    def get_settings(self):
        return {
            "in_dir": str(self.in_dir_text_var.get()),
            "out_dir": str(self.out_dir_text_var.get()),
            "out_ftype": "mp4",
            "audio_bitrate_kbps": int(str(self.audio_bitrate.get())),
            "video_bitrate_mbps": float(self.video_bitrate.get()),
            "output_file_postfix": str(self.video_name_postfix.get()),
            "name": self.config_name_strvar.get()
        }

    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="right")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="left")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())

    def ok_pressed(self):
        d = DirsSettings("settings.json")
        d.save_new_entry(self.get_settings())
        self.destroy()

    def cancel_pressed(self):
        self.destroy()

    def body(self, frame):
        pad = 5

        # Input folder
        self.in_dir_label = ttk.Label(frame, text="Input folder: ")
        self.in_dir_label.grid(column=0, row=0, sticky="W", padx=pad, pady=pad)
        self.in_dir_text_var = tk.StringVar()
        self.in_dir_text_var.set("In dir..")
        self.in_dir_select = ttk.Button(frame,
                                        textvariable=self.in_dir_text_var,
                                        command=self.select_in_dir)
        self.in_dir_select.grid(column=1, row=0, sticky="W", padx=pad, pady=pad)

        # Output folder
        self.out_dir_label = ttk.Label(frame, text="Output folder: ")
        self.out_dir_label.grid(column=0, row=1, sticky="W", padx=pad, pady=pad)
        self.out_dir_text_var = tk.StringVar()
        self.out_dir_text_var.set("Out dir..")
        self.out_dir_select = ttk.Button(frame,
                                         textvariable=self.out_dir_text_var,
                                         command=self.select_out_dir)
        self.out_dir_select.grid(column=1, row=1, sticky="W", padx=pad, pady=pad)

        self.out_filetype_label = ttk.Label(frame, text="Out file type is always MP4.")
        self.out_filetype_label.grid(column=0, row=2,
                               columnspan=2, sticky="W",
                               padx=pad, pady=pad)

        # Audio bitrate
        self.audio_bitrate_label = ttk.Label(frame, text="Audio bitrate: ")
        self.audio_bitrate = tk.StringVar()
        self.audio_bitrate.set("64")
        self.audio_bitrate_input = ttk.Spinbox(frame, textvariable=self.audio_bitrate,
                                               from_=64, to=320, values=("64", "128", "192",
                                                                         "256", "320"))
        self.audio_bitrate_label2 = ttk.Label(frame, text="kbps")
        self.audio_bitrate_label.grid(column=0, row=3, sticky="W", padx=pad, pady=pad)
        self.audio_bitrate_input.grid(column=1, row=3, sticky="W", pady=pad, padx=pad)
        self.audio_bitrate_label2.grid(column=2, row=3, sticky="W", padx=pad, pady=pad)

        # Video bitrate
        self.video_bitrate_label = ttk.Label(frame, text="Video bitrate: ")
        self.video_bitrate = tk.StringVar()
        self.video_bitrate.set("0.4")
        self.video_bitrate_input = ttk.Spinbox(frame, textvariable=self.video_bitrate,
                                               from_=0.1, to=8,
                                               values=tuple((str(x/10) for x in range(1, 81))))
        self.video_bitrate_label2 = ttk.Label(frame, text="Mbps")
        self.video_bitrate_label.grid(column=0, row=4, sticky="W", padx=pad, pady=pad)
        self.video_bitrate_input.grid(column=1, row=4, sticky="W", pady=pad, padx=pad)
        self.video_bitrate_label2.grid(column=2, row=4, sticky="W", padx=pad, pady=pad)

        # Video name postfix
        self.video_name_postfix_label = ttk.Label(frame, text="Video names postfix: ")
        self.video_name_postfix = tk.StringVar()
        self.video_name_postfix.set("_example")
        self.video_name_postfix_entry = ttk.Entry(frame, textvariable=self.video_name_postfix,
                                                  width=20)
        self.video_name_postfix_label.grid(column=0, row=5, sticky="W", padx=pad, pady=pad)
        self.video_name_postfix_entry.grid(column=1, row=5, sticky="W", padx=pad, pady=pad)

        # Video resolution
        self.video_res_label = ttk.Label(frame, text="Video output resolution:")
        self.video_res = ttk.Spinbox(frame, values=("Original", "256x144", "427x240", "640x360",
                                                    "853x480", "1280x720", "1920x1080", "2560x1440",
                                                    "3840x2160", "4096x2160"))
        self.video_res_label.grid(column=0, row=6, sticky="W", padx=pad, pady=pad)
        self.video_res.grid(column=1, row=6, sticky="W", padx=pad, pady=pad)

        self.video_encoding_preset_label = ttk.Label(
            frame,
            text="Encoding preset is always on placebo for smallest file size.")
        self.video_encoding_preset_label.grid(column=0, row=7, padx=pad, pady=pad, sticky="W")

        # Configuration name
        self.config_name_label = ttk.Label(frame, text="Unique configuration name: ")
        self.config_name_strvar = tk.StringVar()
        self.config_name_strvar.set("My SomeProfile")
        self.config_name = ttk.Entry(frame, textvariable=self.config_name_strvar)
        self.config_name_label.grid(column=0, row=8, sticky="W", padx=pad, pady=pad)
        self.config_name.grid(column=1, row=8, sticky="W", padx=pad, pady=pad)







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


