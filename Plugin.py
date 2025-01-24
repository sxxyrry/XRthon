import os, subprocess, shutil
from typing import Literal
from folder import folder
from PluginAPI import *
from logs import Plugins_log


PluginsPath = os.path.join(folder, './plugins')
VirtualEnvironmentPath = os.path.join(folder, './VirtualEnvironment')
LoadedPluginsList: list[str] = []

def LoadPlugins():
    for file in os.listdir(PluginsPath):
        if file.endswith('.py'):
            module_name = file[:-3]
            module_path = os.path.join(PluginsPath, file)

            Plugins_log.info(f"Loading plugin {module_name} ({module_path})")

            try:
                with open(module_path, 'r') as f:
                    c = f.read()
                    c = c.replace('../', '')
                    c = c.replace('..', '')
                    exec(c, globals())

                LoadedPluginsList.append(module_name)

                Plugins_log.info(f"Plugin {module_name} loaded ({module_path})")

            except Exception as e:
                Plugins_log.warning(f"Error loading plugin {module_name}: {e} ({module_path})")

def GetLoadedPlugins() -> list[str]:
    return LoadedPluginsList

def GetInstalledPluginsList() -> list[tuple[str, Literal['Enable', 'Disable']]]:
    InstalledPluginsList: list[tuple[str, Literal['Enable', 'Disable']]] = []
    for file in os.listdir(PluginsPath):
        if file.endswith('.py'):
            module_name = file[:-3]
            InstalledPluginsList.append((module_name, 'Enable'))
        elif file.endswith('.py.disabled'):
            module_name = file[:-12]
            InstalledPluginsList.append((module_name, 'Disable'))
    return InstalledPluginsList
