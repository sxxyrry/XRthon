from custom.CustomNotebook import CustomNotebook
from custom.liner import Liner
import tkinter as tk, tkintertools as tkt, pathlib, json, yaml
from tkinter import filedialog, messagebox, scrolledtext
from Runner import Runner
from typing import Any, Literal, NoReturn
import tkinter.ttk as ttk
import _tkinter as _tk
from Edition_logs import (
    English_Edition_logsForEditor,
    English_Edition_logsForXRthon,
)
from VersionSystem import (
    VersionSystem,
    VersionSystemRulesMDFileContent,
)
from versions import (
    GetVersionForXRthon,
    GetVersionForEditor,
    GetVersion,
)
from logs import (
    Check_log,
    Plugins_log,
    Runner_log,
    Warning_log,
)
from config import Config
import os
import sys
from colorama import Fore, Style, init


LoadedPluginsList: list[str] = []
FolderPath = pathlib.Path(os.path.join(pathlib.Path(__file__).parent.resolve(), './plugins/')).resolve()
root = tkt.Tk("XRthon Editor")
frames: list[tuple[tk.Frame, Liner]] = []
parent = tk.Frame(root)
Up = tk.Menu(parent)
Bottom = tk.Frame(parent)
notebook = CustomNotebook(parent)
config = Config()

def FindPlugin(plugin_name: str) -> bool:
    if plugin_name in os.listdir(FolderPath):
        if os.path.isdir(os.path.join(FolderPath, plugin_name)):
            return True
        else:
            return False
    else:
        return False

def GetEditionLogs_Plugin(plugin_name: str) -> str | NoReturn:
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
    EL = GetEditionLogs_Plugin(plugin_name)
    return GetVersion(EL)

def JudgeVersion_Greater_Plugin(plugin_name: str, Version: str) -> bool:
    return VersionSystem.JudgeVersion_Greater(GetVersionForEditionLogs_Plugin(plugin_name), Version)

def JudgeVersion_Less_Plugin(plugin_name: str, Version: str) -> bool:
    return VersionSystem.JudgeVersion_Less(GetVersionForEditionLogs_Plugin(plugin_name), Version)

def JudgeVersion_Equal_Plugin(plugin_name: str, Version: str) -> bool:
    return VersionSystem.JudgeVersion_Equal(GetVersionForEditionLogs_Plugin(plugin_name), Version)

def ImportPlugin(plugin_name: str, Now_plugin_name) -> dict[str, Any] | NoReturn:
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
                    ask_ = messagebox.askyesno('Plugin is disabled',
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
