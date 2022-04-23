import os.path
import platform
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.Auxialiry import get_settings_json_path
from src.FTAwareDirMapper import FTAwareDirMapper
from src.DirsSettings import DirsSettings
from src.GuiCb import JobRunner


class MenuBar(ttk.Frame):

    def __init__(self, container):
        super(MenuBar, self).__init__(container)

        self.scan_button = MenuButton(master=self, text="Scan",
                                      command=lambda: self.event_generate("<<Scan>>"))
        self.scan_button.grid(column=0, row=0)

        self.run_button = MenuButton(master=self, text="Run",
                                     command=lambda: self.event_generate("<<RunAll>>"))
        self.run_button.grid(column=1, row=0)

        self.add_mapping_button = MenuButton(master=self,
                                             text="Add Mapping",
                                             command=lambda: AddMappingDialog(
                                                 self,
                                                 "Add mapping.."))
        self.add_mapping_button.grid(column=2, row=0)

        self.quit_button = MenuButton(master=self, text="Quit",
                                      command=lambda: self.event_generate("<<Quit>>"))
        self.quit_button.grid(column=3, row=0)


class AddMappingDialog(simpledialog.Dialog):

    def __init__(self, parent, title):
        super().__init__(parent, title)

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
            "output_video_resolution": self.video_res.get(),
            "output_fps": self.fps_textvar.get(),
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
        d = DirsSettings(get_settings_json_path())
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
        self.audio_bitrate_input.grid(column=1, row=3, sticky="W", columnspan=2, pady=pad, padx=pad)
        self.audio_bitrate_label2.grid(column=2, row=3, sticky="W", padx=pad, pady=pad)

        # Video bitrate
        self.video_bitrate_label = ttk.Label(frame, text="Video bitrate: ")
        self.video_bitrate = tk.StringVar()
        self.video_bitrate.set("0.4")
        self.video_bitrate_input = ttk.Spinbox(frame, textvariable=self.video_bitrate,
                                               from_=0.1, to=8,
                                               values=tuple((str(x / 10) for x in range(1, 81))))
        self.video_bitrate_label2 = ttk.Label(frame, text="Mbps")
        self.video_bitrate_label.grid(column=0, row=4, sticky="W", padx=pad, pady=pad)
        self.video_bitrate_input.grid(column=1, row=4, sticky="W", columnspan=2, pady=pad, padx=pad)
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

        # Frames per second
        self.fps_label = ttk.Label(frame, text="Output FPS")
        self.fps_textvar = tk.IntVar()
        self.fps_textvar.set(30)
        self.fps = ttk.Spinbox(frame, textvariable=self.fps_textvar, from_=1, to=144)
        self.fps_label.grid(column=0, row=8, sticky="W", padx=pad, pady=pad)
        self.fps.grid(column=1, row=8, sticky="W", padx=pad, pady=pad)

        # Configuration name
        self.config_name_label = ttk.Label(frame, text="Unique configuration name: ")
        self.config_name_strvar = tk.StringVar()
        self.config_name_strvar.set("My SomeProfile")
        self.config_name = ttk.Entry(frame, textvariable=self.config_name_strvar)
        self.config_name_label.grid(column=0, row=9, sticky="W", padx=pad, pady=pad)
        self.config_name.grid(column=1, row=9, sticky="W", padx=pad, pady=pad)


class JobsContainer(ttk.Frame):

    def __init__(self, container):
        super(JobsContainer, self).__init__(container)
        self.jobs = []

    def initiate_jobs(self, event, job_runner: JobRunner):
        self.scan()
        job_runner.run_all(self.jobs)

    def scan(self):
        self.free_job(*self.jobs)
        self.jobs = []
        settings = DirsSettings(get_settings_json_path()).get_settings()
        mappings = FTAwareDirMapper(settings).get_dir_mappings()
        mappings = [x for x in mappings if not x[1].exists()]
        self.jobs = [Job("..." + str(x[0].parts[-1]), str(x[1]), 0, master=self) for x in mappings]
        for i in range(len(self.jobs)):
            self.jobs[i].pack(side="top", anchor="w")

    def free_job(self, *jobs):
        for job in jobs:
            job.destroy()


class MenuButton(ttk.Button):

    def __init__(self, *args, **kwargs):
        super(MenuButton, self).__init__(*args, **kwargs)


class OpenFolderButton(ttk.Button):

    def __init__(self, *args, **kwargs):
        super(OpenFolderButton, self).__init__(*args, **kwargs)


class JobGauge(ttk.Meter):

    def __init__(self, *args, **kwargs):
        super(JobGauge, self).__init__(*args, **kwargs,
                                       metersize=60,
                                       padding=5,
                                       metertype="full",
                                       showtext=False,
                                       bootstyle=INFO)

    def update_gauge(self, val):
        self.configure(amountused=int(val))


class Job(ttk.Frame):

    def __init__(self, from_file: str, to_file: str, percent: int, *args, **kwargs):
        super().__init__(*args, **kwargs, padding=(10, 10, 10, 10))
        self.open_folder_button = OpenFolderButton(master=self, text="Open Source Folder")
        self.open_folder_button.grid(column=0, row=0, sticky="NS")

        self.open_folder_button = OpenFolderButton(master=self, text="Open Target Folder")
        self.open_folder_button.grid(column=1, row=0, sticky="NS")

        self.gauge = JobGauge(master=self)
        self.gauge.grid(column=2, row=0, sticky="NS")

        self.description = ttk.Label(master=self, text=f"{from_file} => {to_file}",
                                     font=(None, 18, "normal"),
                                     padding=(10, 0, 0, 0))
        self.description.grid(column=3, row=0, sticky="NS")


class VideoConvertor(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = ttk.Style("darkly")

        self.title("VideoConvertor")

        self.menu_bar = MenuBar(self)
        self.menu_bar.pack(side="top", anchor="nw", fill="none", pady=(0, 10))
        self.scrollbar = ttk.Scrollbar(self, orient=ttk.VERTICAL)

        # Scrollable Frame
        self.canvas = tk.Canvas(self)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>",
                                   lambda ev: self.canvas.configure(
                                       scrollregion=self.canvas.bbox("all")
                                   ))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.canvas.yview)

        self.jobs = JobsContainer(self.scrollable_frame)
        self.scrollbar.pack(side="right", fill=ttk.Y)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.jobs.pack(side="left")

        self.geometry("1024x400")

        self.job_runner = JobRunner()
        self.bind("<<RunAll>>", lambda ev: self.jobs.initiate_jobs(ev, job_runner=self.job_runner))
        self.bind("<<Scan>>", lambda ev: self.jobs.scan())
        self.bind("<<Quit>>", lambda ev: self.destroy())
        match platform.system():
            case "Windows":
                self.bind("<MouseWheel>", lambda ev: self.canvas.yview_scroll(-(ev.delta // 80),
                                                                              what="units"))
            case "Linux":
                self.bind("Button-4"), lambda ev: self.canvas.yview_scroll(ev.delta // 80,
                                                                           what="units")
                self.bind("Button-5"), lambda ev: self.canvas.yview_scroll(-ev.delta // 80,
                                                                           what="units")
            case _:  # Mac Os
                self.bind("<MouseWheel>", lambda ev: self.canvas.yview_scroll(ev.delta,
                                                                              what="units"))


