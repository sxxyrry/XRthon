import os
import sys
import tkinter as tk
import webbrowser
import time
from typing import Literal
from PIL import Image, ImageTk
import tkintertools as tkt # type: ignore
import tkinter.ttk as ttk
import _tkinter as _tk
from tkinter import filedialog, messagebox, scrolledtext
from colorama import Fore, Style, init
import yaml
from custom.liner import Liner
from Runner import Runner
from Edition_logs import English_Edition_logsForEditor, Chinese_Edition_logsForEditor
from VersionSystem import VersionSystem
from folder import folder
from versions import GetVersionForEditor
from _del_ import del___pycache__
from GithubAboutFile import GetFileText
from BaseGConfig import token
from PluginAPI import (
    # GetEditionLogs_Plugin,
    root,
    frames,
    parent,
    Up,
    Bottom,
    config,
    # GetVersionForEditionLogs_Plugin,
    GetVersion,
    JudgeVersion_Less_Plugin,
    framesInfo,
    MainNotebook,
    EditorNB,
    EditorNBFrame,
    InfoNB,
    InfoNBFrame,
    AddInfoPage,
    notice,
)
from Plugin import (
    LoadPlugins,
    # GetLoadedPlugins,
    GetInstalledPluginsList,
    GetAllPlugins,
    FindPlugin,
    InstallPlugin,
    UninstallPlugin,
    # PluginsIconDict,
)
from logs import Check_log, Runner_log
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
LoveProgramming：Contact information （联系方式） (163 Email （邮箱）)：sxxyrry_23XR@163.com

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
        self.framesInfo: list[tk.Frame] = framesInfo
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

        def _EN(self=self):
            self.texts = [
                "Run",
                "Add Editor Page",
                "Open File",
                "Save File",
                "Choose File and Run",
                "About",
                "About Us",
                "Installed Plugins",
                "English Edition Logs",
                "Chinese Edition Logs",
                "File",
                "About",
                "Plugins",
                "Edition Logs",
                "Version",
                "Exit",
                "Tips",
                "Effective after restart.",
                "Close Tab",
                "Do you want to close this tab?",
                "Select a file to save",
                "Select a file to open",
                "Switch Language",
                "Introduction website",
                " FIle",
                "Name",
                "Enabled",
                "Disabled",
                "All Plugins",
                "Install Plugin",
                "Are you sure you want to install the {} plugin?",
                "Install Plugin complete.",
                " (exist)",
                "",
                "Uninstall Plugin",
                "Are you sure you want to uninstall the {} plugin?",
                "Uninstall Plugin complete.",
                "Updata Plugin",
                "Are you sure you want to update the {} plugin?",
                "Updata Plugin complete.",
                "Help",
                "Please take a look at the HowToUse file.",
                "Test Program",
                "Notice",
                "Normal connection",
                "Connect to the database normally",
                "Unable to connect",
                "Unable to connect to the database, please check your network connection",
                "Editor",
                "Info",
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
                "安装的插件",
                "英文版日志",
                "中文版日志",
                "文件",
                "关于",
                "插件",
                "版本日志",
                "版本",
                "退出",
                "提示",
                "重启后生效。",
                "关闭标签页",
                "您是否要关闭此标签页？",
                "选择文件保存",
                "选择文件打开",
                "切换语言",
                "介绍网站",
                "文件",
                "名称",
                "启用",
                "禁用",
                "所有插件",
                "安装插件",
                "确定安装{}插件吗？",
                "安装插件完成。",
                "（存在）",
                "",
                "卸载插件",
                "确定卸载{}插件吗？",
                "卸载插件完成。",
                "更新插件",
                "确定更新{}插件吗？",
                "更新插件完成。",
                "帮助",
                "请去看 HowToUse 文件。",
                "测试程序",
                "通知",
                "正常连接",
                "正常连接到数据库。",
                "无法连接",
                "无法连接到数据库，请检查网络连接。",
                "编辑器",
                "信息",
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
        self.Plugin_menu.add_command(label=self.texts[28], command=self.AllPluginsInterface)
        self.Plugin_menu.add_command(label=self.texts[7], command=self.InstalledPluginsInterface)

        self.EditionLogs_menu = tk.Menu(self.Up)
        self.EditionLogs_menu.add_command(label=self.texts[8], command=self.EditionLogsInterface_English)
        self.EditionLogs_menu.add_command(label=self.texts[9], command=self.EditionLogsInterface_Chinese)

        self.Up.add_cascade(label=self.texts[10], menu=self.File_menu)
        self.Up.add_cascade(label=self.texts[11], menu=self.About_menu)
        self.Up.add_cascade(label=self.texts[12], menu=self.Plugin_menu)
        # self.Up.add_command(label="Edition Logs", command=self.EditionLogsInterface)
        self.Up.add_cascade(label=self.texts[13], menu=self.EditionLogs_menu)
        self.Up.add_command(label=self.texts[40], command=lambda :messagebox.showinfo(self.texts[40], self.texts[41])) # type: ignore
        if self.config.Mod == 'DEV':
            self.Up.add_command(label="Restart", command=self.Restart)
            # self.Up.add_command(label="Toggle Theme", command=self.toggle_theme)
        self.Up.add_command(label=self.texts[22], command=self.switch_language)
        self.Up.add_command(label=self.texts[23], command=self.Introduction_Website)
        self.Up.add_command(label=self.texts[14], command=self.VersionInterface)
        # self.Up.add_command(label=self.texts[42], command=self.TestProgramInterface)
        self.Up.add_command(label=self.texts[15], command=lambda: os._exit(0))
        
        self.root.config(menu=self.Up)

        self.MainNotebook = MainNotebook

        self.EditorNB = EditorNB
        self.EditorNBFrame = EditorNBFrame

        self.InfoNB = InfoNB
        self.InfoNBFrame = InfoNBFrame

        self.Bottom.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.Notice = notice
        self.Notice.title.config(text=self.texts[43])

        self.MainNotebook.add(self.EditorNBFrame, text=self.texts[48])
        self.MainNotebook.add(self.InfoNBFrame, text=self.texts[49])
        self.MainNotebook.protect_tab(0)
        self.MainNotebook.protect_tab(1)

        self.TestCanConnectTheDatabase()

    def TestCanConnectTheDatabase_(self):
        # 发送网络请求到 Github 私人仓库，如果请求速度超过2秒，视为网络连接失败
        import requests
        def check_repo(url: str):
            try: response = requests.get(url, timeout=2, verify=False); return response.status_code == 200 #
            except requests.exceptions.RequestException: return False
        repos = [
            'https://api.github.com/repos/sxxyrry/XRthonPluginsDatabase',
            'https://api.github.com/repos/sxxyrry/XRthon',
            'https://api.github.com/repos/sxxyrry/XRthonDatabase'
        ]
        for repo in repos:
            if check_repo(repo): del requests; return True
        del requests; return False

    def TestCanConnectTheDatabase(self):
        if self.TestCanConnectTheDatabase_():
            self.Notice.EmitNotice(self.texts[44], self.texts[45])
        else: 
            self.Notice.EmitErrorNotice(self.texts[46], self.texts[47])

    def Introduction_Website(self):
        webbrowser.open('https://sxxyrry.github.io/XRthon_Project/')

    def Restart(self):
        os.startfile(os.path.join(folder, "./Editor.py"), show_cmd=1)
        os._exit(0)

    def switch_language(self):
        if self.config.language == 'en':
            a = 'English'
            b = '中文'
            if messagebox.askyesno(self.texts[22], f'{a} -> {b}'): # type: ignore
                self.config.SwitchLanguage('zh-cn')
            else:
                return
        elif self.config.language == 'zh-cn':
            a = '中文'
            b = 'English'
            if messagebox.askyesno(self.texts[22], f'{a} -> {b}'): # type: ignore
                self.config.SwitchLanguage('en')
            else:
                return

        messagebox.showinfo(self.texts[16], self.texts[17]) # type: ignore

    def bind_shortcuts(self):
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-n>", lambda event: self.add_editor_page())
        self.root.bind("<Control-q>", lambda event: self.root.destroy())
        self.root.bind("<Control-S>", lambda event: self.save_all_files())

    def save_all_files(self):
        for _, (_, line) in enumerate(self.frames):
            file_path = filedialog.asksaveasfilename(title=self.texts[20],defaultextension='.XRthon', filetypes=[("XRthon Files", "*.XRthon")], initialdir=os.getcwd())
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(line.get_text())

    def toggle_theme(self):
        if self.theme == "light":
            self.theme = "dark"
            self.style.configure("CustomNotebook", background="black", fieldbackground="black", foreground="black") # type: ignore
            self.style.map("CustomNotebook.Tab", background=[("selected", "black")], foreground=[("selected", "black")]) # type: ignore
            for _, line in self.frames:
                line.config(bg="black", fg="white")
        else:
            self.theme = "light"
            self.style.configure("CustomNotebook", background="white", fieldbackground="white", foreground="black") # type: ignore
            self.style.map("CustomNotebook.Tab", background=[("selected", "white")], foreground=[("selected", "white")]) # type: ignore
            for _, line in self.frames:
                line.config(bg="white", fg="black")

    def InstalledPluginsInterface(self):
        _ = tkt.Tk(title=self.texts[7])

        PluginsList: list[tuple[str, Literal['Enabled', 'Disabled'], Image.Image, str, str]] = GetInstalledPluginsList()

        for i in range(len(PluginsList)):
            img_ = PluginsList[i][2]

            img = ImageTk.PhotoImage(img_, master=_)

            # print(img, img.height(), img.width(), img.tk, img._PhotoImage__photo, img._PhotoImage__mode, img._PhotoImage__size)
            f = tk.Frame(_)

            # btn = tk.Button()
            # btn.pack()

            state: str = PluginsList[i][1]
            state: str = self.texts[26] if state == 'Enabled' else self.texts[27]

            PluName = PluginsList[i][0]

            iLbl = tk.Label(f, text=f"{i + 1}")
            iLbl.grid(row=0, column=0)

            imgLbl = tk.Label(f, image=img)
            imgLbl.image = img # type: ignore
            imgLbl.grid(row=0, column=1)

            t = tk.Label(f, text=f"{self.texts[25]}: {PluName} ({state})")
            t.grid(row=0, column=2)

            UninstallBtn = tk.Button(f, text=self.texts[34], command=lambda PluName=PluName: self.UninstallPlugin(PluName))
            UninstallBtn.grid(row=0, column=3)

            UpdateBtn = tk.Button(f, text=self.texts[37], command=lambda PluName=PluName: self.UpdatePlugin(PluName))
            UpdateBtn.config(state='disabled')

            if JudgeVersion_Less_Plugin(
                PluName,
                GetVersion(
                    GetFileText(
                        token,
                        'sxxyrry',
                        'XRthonPluginsDatabase',
                        f'Plugins/{PluName}/{yaml.safe_load(
                            GetFileText(
                                token,
                                'sxxyrry',
                                'XRthonPluginsDatabase',
                                f'Plugins/{PluName}/config.json'
                            )
                        )['EditionLogsFilePath'][2::]}'
                    )
                )
            ):
                UpdateBtn.config(state='normal')

            OverviewTextLbl = tk.Label(f, text=f"{PluginsList[i][3]}")
            OverviewTextLbl.grid(row=1, column=2)

            # print(f'{GetVersion(
            #         GetFileText(
            #             token,
            #             'sxxyrry',
            #             'XRthonPluginsDatabase',
            #             f'Plugins/{PluName}/{yaml.safe_load(
            #                 GetFileText(
            #                     token,
            #                     'sxxyrry',
            #                     'XRthonPluginsDatabase',
            #                     f'Plugins/{PluName}/config.json'
            #                 )
            #             )['EditionLogsFilePath'][2::]}'
            #         )
            #     )=}')

            UpdateBtn.grid(row=0, column=4)

            f.pack()
        
        _.mainloop()

    def UninstallPlugin(self, PluName: str):
        if messagebox.askyesno(self.texts[34], self.texts[35].format(PluName)): # type: ignore

            UninstallPlugin(PluName)

            messagebox.showinfo(self.texts[34], self.texts[36]) # type: ignore

            messagebox.showinfo(self.texts[16], self.texts[17]) # type: ignore
        else:
            return

    def AllPluginsInterface(self):
        _ = tkt.Tk(title=self.texts[29])

        PluginsList: list[str] = GetAllPlugins()

        for i in range(len(PluginsList)):
            f = tk.Frame(_)

            PluName = PluginsList[i]

            t = tk.Label(f, text=f"{i + 1} {self.texts[25]}: {PluName}")
            t.grid(row=0, column=0)

            btn = tk.Button(f, text=self.texts[29], command=lambda PluName=PluName: self.InstallPlugin(PluName))

            s = tk.Label(f, text=self.texts[32])

            if FindPlugin(PluName):
                btn.config(state='disabled')
            else:
                s.config(text=self.texts[33])
            
            s.grid(row=0, column=1)
            btn.grid(row=0, column=2)

            f.pack()
        
        _.mainloop()

    def InstallPlugin(self, PluName: str):
        if messagebox.askyesno(self.texts[29], self.texts[30].format(PluName)): # type: ignore # type: ignore
            
            InstallPlugin(PluName)

            messagebox.showinfo(self.texts[29], self.texts[31]) # type: ignore

            messagebox.showinfo(self.texts[16], self.texts[17]) # type: ignore
        else:
            return

    def UpdatePlugin(self, PluName: str):
        if messagebox.askyesno(self.texts[37], self.texts[38].format(PluName)): # type: ignore
            
            UninstallPlugin(PluName)
            InstallPlugin(PluName)

            messagebox.showinfo(self.texts[37], self.texts[39]) # type: ignore

            messagebox.showinfo(self.texts[16], self.texts[17]) # type: ignore
        else:
            return

    def VersionInterface(self):
        _ = tkt.Tk(title=self.texts[14])

        lable = tk.Label(_, text=f'{self.texts[14]}: {version}')
        lable.pack()

        _.mainloop()
    
    def AboutInterface(self):
        _ = tkt.Tk(title=self.texts[5])

        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, AT)
        t.config(state='disabled')
        t.pack()

        _.mainloop()

    def AboutUsInterface(self):
        _ = tkt.Tk(title=self.texts[6])

        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, AUT)
        t.config(state='disabled')
        t.pack()

        _.mainloop()

    def EditionLogsInterface_English(self):
        _ = tkt.Tk(title=self.texts[13])

        t = scrolledtext.ScrolledText(_, width=100, height=20)
        t.insert(tk.END, English_Edition_logsForEditor)
        t.config(state='disabled')
        t.pack()

        _.mainloop()

    def EditionLogsInterface_Chinese(self):
        _ = tkt.Tk(title='版本记录')

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

        runner.End()

    def OnCloseEditorPage(self, e: tk.Event): # type: ignore
        widget: tk.Frame = e.widget # type: ignore

        frames_ = [i[0] for i in self.frames]

        self.frames.remove(self.frames[frames_.index(widget)]) # type: ignore
        self.i -= 1
        self.frame_id -= 1

    def OnCloseInfoPage(self, e: tk.Event): # type: ignore
        widget: tk.Frame = e.widget # type: ignore

        self.framesInfo.remove(self.framesInfo[self.framesInfo.index(widget)]) # type: ignore

    def add_updater(self, frame: tk.Frame, line: Liner):
        try:
            self.Now_frame_id = self.frames.index((frame, line))
        except ValueError:
            self.Now_frame_id = self.frame_id

    def add_editor_page(self):
        frame = tk.Frame(self.root)
        line = Liner(frame)
        line.pack(fill="both", expand=True)
        self.frames.append((frame, line))
        frame.bind('<Visibility>', lambda event: self.add_updater(frame, line))
        frame.bind('<<NotebookTabClosed>>', self.OnCloseEditorPage) # type: ignore
        if self.i == 0:
            self.EditorNB.add(frame, text=f"XRthon{self.texts[24]}")
            self.EditorNB.protect_tab(len(self.frames) - 1)
        else:
            self.EditorNB.add(frame, text=f"XRthon{self.texts[24]} {self.i + 1}")
        
        self.MainNotebook.select(0) # type: ignore
        self.EditorNB.select(len(self.frames) - 1) # type: ignore
        
        self.frame_id = len(self.frames) - 1
        self.i += 1
    
    def update(self):
        try:
            if self.root.wm_state() == "iconic":
                pass
            if self.frame_id == -1:
                return
            if isinstance(self.frames[self.frame_id][1], Liner) and not isinstance(self.frames[self.frame_id][1], tk.Label):  # type: ignore
                self.frames[self.frame_id][1].redraw()
        except _tk.TclError:
            del___pycache__()
            quit()

    def pack(self):
        self.parent.pack(fill=tk.NONE, expand=True)

def start():
    global root  # 确保使用全局的 root 变量
    # root = tkt.Tk("XRthon Editor")  # 创建新的主窗口

    texts = []

    def _EN():
        texts = [
            'Start Screen',
            'We greatly appreciate your use of our program',
        ]
        return texts
    
    if config.language == 'en':
        texts = _EN()
    elif config.language == 'zh-cn':
        texts = [
            '启动界面',
            '我们非常欢迎您使用我们的程序',
        ]
    else:
        texts = _EN()

    IconPNG = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), './Images/Icon_XRthon.png')).resize((370, 70))) # type: ignore

    SignPNG = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), './Images/Sign.png')).resize((330, 180))) # type: ignore

    IconLbl = tk.Label(root, image=IconPNG)
    IconLbl.image = IconPNG # type: ignore
    IconLbl.pack()

    SignLbl = tk.Label(root, image=SignPNG)
    SignLbl.image = SignPNG # type: ignore
    SignLbl.pack()

    root.update()

    time.sleep(1)

    IconLbl.destroy()
    SignLbl.destroy()

    notice.pack()

    editor = Editor()
    editor.pack()

    editor.add_editor_page()

    AddInfoPage(texts[0], texts[1])

    if len(sys.argv) == 2:
        editor.frames[editor.frame_id][1].load_content(open(sys.argv[1], 'r', encoding='UTF-8').read())

    LoadPlugins()

    root.update()
    editor.update()
    
    # messagebox.showinfo(texts[0], texts[1])

    try:
        while True:
            root.update()
            editor.update()
    except KeyboardInterrupt:
        del___pycache__()

    del___pycache__()

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        start()
    else:
        raise Exception('Invalid arguments')
