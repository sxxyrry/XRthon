from custom.liner import Liner
import tkinter as tk, tkintertools as tkt, pathlib, json, yaml # type: ignore
from tkinter import filedialog, messagebox, scrolledtext # type: ignore
from Runner import Runner # type: ignore
from typing import Any, Literal, NoReturn # type: ignore
import tkinter.ttk as ttk # type: ignore
import _tkinter as _tk # type: ignore
from Edition_logs import (
    English_Edition_logsForEditor, # type: ignore
    English_Edition_logsForXRthon, # type: ignore
    Chinese_Edition_logsForEditor, # type: ignore
    Chinese_Edition_logsForXRthon, # type: ignore
)
from VersionSystem import (
    VersionSystem,
    VersionSystemRulesMDFileContent, # type: ignore
)
from versions import (
    GetVersionForXRthon, # type: ignore
    GetVersionForEditor, # type: ignore
    GetVersion,
)
from logs import (
    Check_log, # type: ignore
    Plugins_log,
    Runner_log, # type: ignore
    Warning_log, # type: ignore
)
from Notice import Notice
from config import Config
from PIL import Image, ImageTk # type: ignore
from tkintertools import toolbox  # type: ignore
import os
import sys # type: ignore
from colorama import Fore, Style, init # type: ignore
from custom.CustomNotebook import CustomNotebook


LoadedPluginsList: list[str] = []
FolderPath = pathlib.Path(os.path.join(pathlib.Path(__file__).parent.resolve(), './plugins/')).resolve()
root = tkt.Tk(title="XRthon Editor")

icon = toolbox.enhanced.PhotoImage(Image.open(os.path.join(pathlib.Path(__file__).parent.resolve(), './Images/Icon_XRthon.ico')))

root.icon(icon)

frames: list[tuple[tk.Frame, Liner]] = []
framesInfo: list[tk.Frame] = []
parent = tk.Frame(root)
Up = tk.Menu(parent)
Bottom = tk.Frame(parent)
config = Config()

MainNotebook = CustomNotebook(parent)
MainNotebook.pack(fill=tk.BOTH, expand=True)

EditorNBFrame = tk.Frame(parent)
EditorNB = CustomNotebook(EditorNBFrame)
EditorNB.pack(fill=tk.BOTH, expand=True)

InfoNBFrame = tk.Frame(parent)
InfoNB = CustomNotebook(InfoNBFrame)
InfoNB.pack(fill=tk.BOTH, expand=True)

NoticeFrame = tk.Frame(root)
notice = Notice(root, NoticeFrame) # type: ignore
NoticeFrame.pack(side="right", fill="both")
# notice.pack()

def AddInfoPage(title: str="Information", text: str="Information"):
    '''
    增加信息页面

    :param: title 标题
    :param: text 文本

    :return: None
    '''
    frame = tk.Frame(root)

    info_label = tk.Label(frame, text=text, wraplength=400, justify=tk.LEFT)
    info_label.pack(fill="both", expand=True)

    framesInfo.append(frame)

    InfoNB.add(frame, text=title)
    MainNotebook.select(1) # type: ignore
    InfoNB.select(len(framesInfo) - 1) # type: ignore
    if len(framesInfo) - 1 == 0:
        InfoNB.protect_tab(0)

def FindPlugin(plugin_name: str) -> bool:
    '''
    寻找插件

    :param: plugin_name 插件名

    :return: bool 插件是否存在
    '''
    if plugin_name in os.listdir(FolderPath):
        if os.path.isdir(os.path.join(FolderPath, plugin_name)):
            return True
        else:
            return False
    else:
        return False

def GetEditionLogs_Plugin(plugin_name: str) -> str | NoReturn:
    '''
    获得插件的版本日志

    :param: plugin_name 插件名

    :return: str 版本日志 NoReturn 插件不存在或格式不正确
    '''
    if FindPlugin(plugin_name):
        if os.path.isdir(os.path.join(FolderPath, plugin_name)):
            with open(os.path.join(FolderPath, plugin_name, './config.json'), 'r') as f:
                config: dict[str, str] = yaml.safe_load(f)

            EditionLogsFilePath = config['EditionLogsFilePath']
            if EditionLogsFilePath == '':
                raise ValueError(f'EditionLogsFilePath is empty. ({plugin_name})')
            else:
                with open(os.path.join(FolderPath, plugin_name, EditionLogsFilePath), 'r') as f:
                    EditionLogs: str = f.read()
                return EditionLogs
        else:
            raise ValueError(f'Plugin is not a directory. ({plugin_name})')
    else:
        raise ValueError(f'Plugin is not found. ({plugin_name})')

def GetVersionForEditionLogs_Plugin(plugin_name: str) -> str | NoReturn:
    '''
    从插件版本日志中获取版本

    :param: plugin_name 插件名

    :return: str 版本
    :return: NoReturn 插件不存在或格式不正确
    '''
    EL = GetEditionLogs_Plugin(plugin_name)
    return GetVersion(EL)

def JudgeVersion_Greater_Plugin(plugin_name: str, Version: str) -> bool:
    '''
    判断版本是否大于指定版本

    :param: plugin_name 插件名
    :param: Version 指定的版本

    :return: bool 版本是否大于指定版本
    '''
    return VersionSystem.JudgeVersion_Greater(GetVersionForEditionLogs_Plugin(plugin_name), Version)

def JudgeVersion_Less_Plugin(plugin_name: str, Version: str) -> bool:
    '''
    判断版本是否小于指定版本

    :param: plugin_name 插件名
    :param: Version 指定的版本

    :return: bool 版本是否小于指定版本
    '''
    return VersionSystem.JudgeVersion_Less(GetVersionForEditionLogs_Plugin(plugin_name), Version)

def JudgeVersion_Equal_Plugin(plugin_name: str, Version: str) -> bool:
    '''
    判断版本是否等于指定版本

    :param: plugin_name 插件名
    :param: Version 指定的版本

    :return: bool 版本是否等于指定版本
    '''
    return VersionSystem.JudgeVersion_Equal(GetVersionForEditionLogs_Plugin(plugin_name), Version)

def ImportPlugin(plugin_name: str, Now_plugin_name: str) -> dict[str, Any] | NoReturn:
    '''
    导入插件

    :param: plugin_name 本插件的名称
    :param: Now_plugin_name 要导入的插件的名称

    :return: dict[str, Any] 插件内容
    :return: NoReturn 插件不存在或格式不正确
    '''
    def Load(path: str):
        path = str(pathlib.Path(path).resolve())
        filePath = os.path.join(path, './__init__.py')
        
        Plugins_log.info(f"Loading plugin {plugin_name} ({path})")
        try:
            with open(filePath, 'r', encoding='UTF-8') as f:
                c = f.read()
                c = c.replace('../../', '')
                c = c.replace('...', '')
                glo = globals().copy()
                exec(c, glo)
            
                LoadedPluginsList.append(plugin_name)
                Plugins_log.info(f"Plugin {plugin_name} loaded ({path})")
        except Exception as e:
            Plugins_log.warning(f"Error loading plugin {plugin_name}: {e} ({path})")
            glo = globals().copy()
        
        return glo
    if FindPlugin(plugin_name):
        path = os.path.join(FolderPath, plugin_name)
        if os.path.isdir(path):
            if os.path.exists(os.path.join(path, './config.json')):
                with open(os.path.join(path, './config.json'), 'r', encoding='UTF-8') as f:
                    config: dict[str, str] = yaml.safe_load(f)

                if config['state'] == 'Enable':
                    return Load(path)
                else:
                    ask_ = messagebox.askyesno('Plugin is disabled', # type: ignore
                                               f'Do you want to enable {plugin_name} (It\'s only temporary)?\n\
Because this Plugin ({Now_plugin_name}) needs to use it.\n\
')
                    
                    if ask_:
                        # config['state'] = 'Enable'
                        # with open(os.path.join(path, './config.json'), 'w') as f:
                        #     json.dump(config, f)
                        return Load(path)
                    else:
                        raise ValueError('Plugin is disabled.')
            
            else:
                Plugins_log.error(f"Plugin {plugin_name} is not a valid plugin (No config.json) ({path})")
                raise Exception(f"Plugin {plugin_name} is not a valid plugin (No config.json) ({path})")
        
        else:
            Plugins_log.error(f"Plugin {plugin_name} is not a valid plugin (Isn\'t a D) ({path})")
            raise Exception(f"Plugin {plugin_name} is not a valid plugin (Isn\'t a D) ({path})")
    else:
        raise ValueError(f'Plugin {plugin_name} is not found.')
