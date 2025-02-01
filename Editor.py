from calendar import c
import os
import sys
import tkinter as tk
from typing import Literal
import tkintertools as tkt
import tkinter.ttk as ttk
import _tkinter as _tk
from tkinter import filedialog, messagebox, scrolledtext
from colorama import Fore, Style, init
from custom.CustomNotebook import CustomNotebook
from custom.liner import Liner
from Runner import Runner
from Edition_logs import English_Edition_logsForEditor, Chinese_Edition_logsForEditor
from VersionSystem import VersionSystem
from versions import GetVersionForEditor
from _del_ import del___pycache__
from PluginAPI import (
    root,
    frames,
    parent,
    Up,
    Bottom,
    notebook,
    config
)
from Plugin import LoadPlugins, GetLoadedPlugins, GetInstalledPluginsList
from logs import Check_log, Runner_log


init()

# , 800, 600, 200, 200

AT = '''\
This is the XRthon editor

It is made by '是星星与然然呀' （由 '是星星与然然呀' 制作）
(The files in the 'custom' folder were all created by 'LoveProgramming' , but I made some modifications to fit my programming language)
（（ ‘custom’ 文件夹下的文件均由  ‘LoveProgramming’  制作，但由于为了贴合我的编程语言，所以我修改了一部分））\
''' # about text

AUT = '''\
是星星与然然呀：Contact information （联系方式） (QQ)：3771386319
LoveProgramming：Contact information （联系方式） (BiliBili)：https://space.bilibili.com/3493125991434836?spm_id_from=333.999.0.0

Sponsorship link （赞助链接） :
https://ifdian.net/order/create?plan_id=b2d954aa5c7711ef8af952540025c377&product_type=0&remark=\
''' # about us text

version = GetVersionForEditor()
if VersionSystem.CheckVersion(version if '/NVSFT: ' not in version else version.split('/NVSFT: ')[1]):
    Check_log.info(f'{Fore.GREEN}Check: Your XRthon Editor Version format is Normal.{Style.RESET_ALL}')
    # messagebox.showinfo("Check", "Your XRthon Version format is Normal.")
else:
    Check_log.warning(f'{Fore.RED}Check: Your XRthon Editor Version format is Invalid.{Style.RESET_ALL}')
    # messagebox.showinfo("Check", "Your XRthon Version format is Invalid.")
    raise SystemExit()

class Editor():
    def __init__(self):
        self.frames: list[tuple[tk.Frame, Liner]] = frames
        self.frame_id = -1
        self.i = 0
        self.Now_frame_id = 0
        self.root: tkt.Tk = root
        self.parent: tk.Frame = parent
        self.Up: tk.Menu = Up
        self.Bottom: tk.Frame = Bottom
        self.style = ttk.Style()
        self.bind_shortcuts()
        self.config = config

        def _EN():
            self.texts = [
                "Run",
                "Add Editor Page",
                "Open File",
                "Save File",
                "Choose File and Run",
                "About",
                "About Us",
                "Install Plugins",
                "English Edition Logs",
                "Chinese Edition Logs",
                "File",
                "About",
                "Plugins",
                "Edition Logs",
                "Version",
                "Exit",
                "Tips",
                "Effective after restart",
                "Close Tab",
                "Do you want to close this tab?",
                "Select a file to save",
                "Select a file to open",
                "Switch Language",
            ]

        if self.config.language == 'en':
            _EN()
        elif self.config.language == 'zh-cn':
            self.texts = [
                "运行",
                "添加编辑页面",
                "打开文件",
                "保存文件",
                "选择文件并运行",
                "关于",
                "关于我们",
                "安装插件",
                "英文版日志",
                "中文版日志",
                "文件",
                "关于",
                "插件",
                "版本日志",
                "版本",
                "退出",
                "提示",
                "重启后生效",
                "关闭标签页",
                "您是否要关闭此标签页？",
                "选择文件保存",
                "选择文件打开",
                "切换语言",
            ]
        else:
            _EN()

        self.Run_Button = tk.Button(self.Bottom, text=self.texts[0], command=self.RunCode)
        self.Run_Button.pack(side=tk.RIGHT)

        self.add_editor_page_Button = tk.Button(self.Bottom, text=self.texts[1], command=self.add_editor_page)
        self.add_editor_page_Button.pack(side=tk.RIGHT)

        self.File_menu = tk.Menu(self.Up)
        self.File_menu.add_command(label=self.texts[2], command=self.open_file)
        self.File_menu.add_command(label=self.texts[3], command=self.save_file)
        self.File_menu.add_command(label=self.texts[4], command=self.choose_file_and_run)
        # self.File_menu.pack(side=tk.LEFT)

        self.About_menu = tk.Menu(self.Up)
        self.About_menu.add_command(label=self.texts[5], command=self.AboutInterface)
        self.About_menu.add_command(label=self.texts[6], command=self.AboutUsInterface)
        # lambda: messagebox.showinfo("About Us", AUT)

        self.Plugin_menu = tk.Menu(self.Up)
        self.Plugin_menu.add_command(label=self.texts[7], command=self.InstalledPluginsInterface)

        self.EditionLogs_menu = tk.Menu(self.Up)
        self.EditionLogs_menu.add_command(label=self.texts[8], command=self.EditionLogsInterface_English)
        self.EditionLogs_menu.add_command(label=self.texts[9], command=self.EditionLogsInterface_Chinese)

        self.Up.add_cascade(label=self.texts[10], menu=self.File_menu)
        self.Up.add_cascade(label=self.texts[11], menu=self.About_menu)
        self.Up.add_cascade(label=self.texts[12], menu=self.Plugin_menu)
        # self.Up.add_command(label="Edition Logs", command=self.EditionLogsInterface)
        self.Up.add_cascade(label=self.texts[13], menu=self.EditionLogs_menu)
        self.Up.add_command(label=self.texts[22], command=self.switch_language)
        self.Up.add_command(label=self.texts[14], command=self.VersionInterface)
        # self.Up.add_command(label="Toggle Theme", command=self.toggle_theme)
        self.Up.add_command(label=self.texts[15], command=self.root.destroy)
        
        self.root.config(menu=self.Up)

        self.notebook = notebook

        self.Bottom.pack(side=tk.BOTTOM, fill=tk.X)
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def switch_language(self):
        if self.config.language == 'en':
            a = 'English'
            b = '中文'
            if messagebox.askyesno(self.texts[22], f'{a} -> {b}'):
                self.config.SwitchLanguage('zh-cn')
            else:
                return
        elif self.config.language == 'zh-cn':
            a = '中文'
            b = 'English'
            if messagebox.askyesno(self.texts[22], f'{a} -> {b}'):
                self.config.SwitchLanguage('en')
            else:
                return

        messagebox.showinfo(self.texts[16], self.texts[17])

    def bind_shortcuts(self):
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-n>", lambda event: self.add_editor_page())
        self.root.bind("<Control-q>", lambda event: self.root.destroy())
        self.root.bind("<Control-w>", lambda event: self.close_tab(self.notebook.index("current")))
        self.root.bind("<Control-S>", lambda event: self.save_all_files())

    def close_tab(self, index):
        if messagebox.askokcancel(self.texts[18], self.texts[19]):
            self.notebook.forget(index)
            del self.frames[index]

    def save_all_files(self):
        for i, (frame, line) in enumerate(self.frames):
            file_path = filedialog.asksaveasfilename(title=self.texts[20],defaultextension='.XRthon', filetypes=[("XRthon Files", "*.XRthon")], initialdir=os.getcwd())
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(line.get_text())

    # def toggle_theme(self):
    #     if self.theme == "light":
    #         self.theme = "dark"
    #         self.style.configure("CustomNotebook", background="black", fieldbackground="black", foreground="black")
    #         self.style.map("CustomNotebook.Tab", background=[("selected", "black")], foreground=[("selected", "black")])
    #         for frame, line in self.frames:
    #             line.config(bg="black", fg="white")
    #     else:
    #         self.theme = "light"
    #         self.style.configure("CustomNotebook", background="white", fieldbackground="white", foreground="black")
    #         self.style.map("CustomNotebook.Tab", background=[("selected", "white")], foreground=[("selected", "white")])
    #         for frame, line in self.frames:
    #             line.config(bg="white", fg="black")

    def InstalledPluginsInterface(self):
        _ = tkt.Tk('Installed Plugins')

        PluginsList: list[tuple[str, Literal['Enable', 'Disable']]] = GetInstalledPluginsList()

        for i in range(len(PluginsList)):
            f = tk.Frame(_)

            # btn = tk.Button()
            # btn.pack()

            t = tk.Label(f, text=f"{i + 1} Name: {PluginsList[i][0]} ({PluginsList[i][1]})")
            t.pack()

            f.pack()
        
        _.mainloop()

    def VersionInterface(self):
        _ = tkt.Tk('Version')

        lable = tk.Label(_, text=f'Version: {version}')
        lable.pack()

        _.mainloop()

    def AboutInterface(self):
        _ = tkt.Tk('About')

        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, AT)
        t.config(state='disabled')
        t.pack()

        _.mainloop()

    def AboutUsInterface(self):
        _ = tkt.Tk('About Us')

        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, AUT)
        t.config(state='disabled')
        t.pack()

        _.mainloop()

    def EditionLogsInterface_English(self):
        _ = tkt.Tk('Edition Logs')

        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, English_Edition_logsForEditor)
        t.config(state='disabled')
        t.pack()

        _.mainloop()

    def EditionLogsInterface_Chinese(self):
        _ = tkt.Tk('版本记录')

        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, Chinese_Edition_logsForEditor)
        t.config(state='disabled')
        t.pack()

        _.mainloop()

    def open_file(self):
        _ = filedialog.askopenfiles(title=self.texts[21], filetypes=[('XRthon Files', '*.XRthon')], initialdir=os.getcwd())

        for i in _:
            self.add_editor_page()
            self.frames[self.frame_id][1].load_content(i.read())

    def save_file(self):
        _ = filedialog.asksaveasfile(title=self.texts[20], defaultextension='.XRthon', filetypes=[('XRthon Files', '*.XRthon')], initialdir=os.getcwd())
        if _:
            _.write(self.frames[self.Now_frame_id][1].get_text())

    def choose_file_and_run(self):
        self.open_file()
        self.RunCode()

    def RunCode(self):
        _ = self.frames[self.Now_frame_id][1].get_text()
        runner = Runner(f'temp_{self.Now_frame_id + 1}')
        Runner_log.info(f'\nStart Run temp_{self.Now_frame_id + 1}\n-----------------------')

        try:
            runner.run_fortexts(_)
        except SystemExit:
            pass
        
        Runner_log.info(f'\n---------------------\nEnd Run temp_{self.Now_frame_id + 1}\n')

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
            self.notebook.select(len(self.frames) - 1)
        
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
            del___pycache__()
            quit()

    def pack(self):
        self.parent.pack(fill=tk.NONE, expand=True)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        editor = Editor()

        editor.pack()
        editor.add_editor_page()

        LoadPlugins()

        try:
            while True:
                editor.update()
                root.update()
        except KeyboardInterrupt:
            del___pycache__()
            quit()

        # root.mainloop()

        del___pycache__()
    elif len(sys.argv) == 2:
        editor = Editor()

        editor.pack()
        editor.add_editor_page()
        editor.frames[editor.frame_id][1].load_content(open(sys.argv[1], 'r', encoding='UTF-8').read())

        LoadPlugins()

        try:
            while True:
                editor.update()
                root.update()
        except KeyboardInterrupt:
            del___pycache__()
            quit()

        # root.mainloop()

        del___pycache__()
    else:
        raise Exception('Invalid arguments')
