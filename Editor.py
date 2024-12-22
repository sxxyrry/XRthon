import os
import tkinter as tk
import tkintertools as tkt
import tkinter.ttk as ttk
import _tkinter as _tk
from tkinter import filedialog, messagebox, scrolledtext
from colorama import Fore, Style, init
from custom.CustomNotebook import CustomNotebook
from custom.liner import Liner
from Runner import Runner
from Edition_logs import Edition_logsForEditor
from VersionSystem import VersionSystem
from versions import GetVersionForEditor


init()

# , 800, 600, 200, 200

AT = '''\
This is the XRthon editor

It is made by '是星星与然然呀' （由 '是星星与然然呀' 制作）
('CustomNoteBook' produced by 'LoveProgramming')（（'CustomNoteBook' 由 'LoveProgramming' 制作））\
''' # about text

AUT = '''\
是星星与然然呀：Contact information （联系方式） (QQ)：3771386319
LoveProgramming：Contact information （联系方式） (BiliBili)：https://space.bilibili.com/3493125991434836?spm_id_from=333.999.0.0

Sponsorship link （赞助链接） :
https://ifdian.net/order/create?plan_id=b2d954aa5c7711ef8af952540025c377&product_type=0&remark=\
''' # about us text

version = GetVersionForEditor()

if VersionSystem.CheckVersion(version if '/NVSFT: ' not in version else version.split('/NVSFT: ')[1]):
    print(f'{Fore.GREEN}Check: Your XRthon Version format is Normal.{Style.RESET_ALL}')
    # messagebox.showinfo("Check", "Your XRthon Version format is Normal.")
else:
    print(f'{Fore.RED}Check: Your XRthon Version format is Invalid.{Style.RESET_ALL}')
    # messagebox.showinfo("Check", "Your XRthon Version format is Invalid.")
    raise SystemExit()

root = tkt.Tk("XRthon Editor")

class Editor():
    def __init__(self, root = tkt.Tk):
        self.frames: list[tuple[tk.Frame, Liner]] = []
        self.frame_id = -1
        self.i = 0
        self.Now_frame_id = 0
        self.root: tkt.Tk = root
        self.parent = tk.Frame(self.root)
        self.Up = tk.Menu(self.parent)
        self.Bottom = tk.Frame(self.parent)

        self.Run_Button = tk.Button(self.Bottom, text="Run", command=self.RunCode)
        self.Run_Button.pack(side=tk.RIGHT)

        self.add_editor_page_Button = tk.Button(self.Bottom, text="Add Editor Page", command=self.add_editor_page)
        self.add_editor_page_Button.pack(side=tk.RIGHT)

        self.File_menu = tk.Menu(self.Up)
        self.File_menu.add_command(label="Open File", command=self.open_file)
        self.File_menu.add_command(label="Save File", command=self.save_file)
        self.File_menu.add_command(label="Choose File and Run", command=self.choose_file_and_run)
        # self.File_menu.pack(side=tk.LEFT)

        self.About_menu = tk.Menu(self.Up)
        self.About_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", AT))
        self.About_menu.add_command(label="About Us", command=self.AboutUsI)
        # lambda: messagebox.showinfo("About Us", AUT)

        self.Up.add_cascade(label="File", menu=self.File_menu)
        self.Up.add_cascade(label="About", menu=self.About_menu)
        self.Up.add_command(label="Exit", command=self.root.destroy)
        self.Up.add_command(label="Edition Logs", command=self.EditionLogsI)
        self.Up.add_command(label="Version", command=lambda: messagebox.showinfo("Version", version))


        self.root.config(menu=self.Up)

        self.notebook = CustomNotebook(self.parent)

        self.Bottom.pack(side=tk.BOTTOM, fill=tk.X)
        self.notebook.pack(fill=tk.BOTH, expand=True)
    
    def AboutUsI(self):
        _ = tkt.Tk('About Us')
        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, AUT)
        t.config(state='disabled')

        t.pack()
        _.mainloop()

    def EditionLogsI(self):
        _ = tkt.Tk('Edition Logs')
        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, Edition_logsForEditor)
        t.config(state='disabled')

        t.pack()
        _.mainloop()

    def open_file(self):
        _ = filedialog.askopenfiles(filetypes=[("XRthon Files", "*.XRthon")], initialdir=os.getcwd())

        for i in _:
            self.add_editor_page()
            self.frames[self.frame_id][1].load_content(i.read())

    def save_file(self):
        _ = filedialog.asksaveasfile(defaultextension='.XRthon', filetypes=[("XRthon Files", "*.XRthon")], initialdir=os.getcwd())
        if _:
            _.write(self.frames[self.frame_id][1].get_text())

    def choose_file_and_run(self):
        self.open_file()
        self.RunCode()

    def RunCode(self):
        _ = self.frames[self.Now_frame_id][1].get_text()
        runner = Runner(f'temp_{self.Now_frame_id + 1}')
        print(f'Start Run temp_{self.Now_frame_id + 1}')
        print( '-----------------------')

        try:
            runner.run_fortexts(_)
        except SystemExit:
            pass
        
        print( '---------------------')
        print(f'End Run temp_{self.Now_frame_id + 1}\n')

        del runner

    def add_updater(self, frame, line):
        self.Now_frame_id = self.frames.index((frame, line))
    
    def add_editor_page(self):
        frame = tk.Frame(self.root)
        line = Liner(frame)
        line.pack(fill="both", expand=True)
        self.frames.append((frame, line))
        frame.bind('<Visibility>', lambda event: self.add_updater(frame, line))
        if self.i == 0:
            self.notebook.add(frame, text="XRthon File")
            self.notebook.protect_tab(len(self.frames) - 1)
        else:
            self.notebook.add(frame, text=f"XRthon File {self.i + 1}")
        
        self.frame_id = len(self.frames) - 1
        self.i += 1
        
    def update(self):
        try:
            if self.root.wm_state() == "iconic":
                pass
            if self.frame_id == -1:
                return
            if isinstance(self.frames[self.frame_id][1], Liner) and not isinstance(self.frames[self.frame_id][1], tk.Label): 
                self.frames[self.frame_id][1].redraw()
        except _tk.TclError:
            quit()

    def pack(self):
        self.parent.pack(fill=tk.NONE, expand=True)

editor = Editor(root)

editor.pack()
editor.add_editor_page()

try:
    while True:
        editor.update()
        root.update()
except KeyboardInterrupt:
    quit()

# root.mainloop()
