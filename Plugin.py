import os, shutil
from typing import Literal
from folder import folder
from PluginAPI import *
from logs import Plugins_log


PluginsPath = os.path.join(folder, './plugins')
VirtualEnvironmentPath = os.path.join(folder, './VirtualEnvironment')

def LoadPlugins():
    for dir in os.listdir(PluginsPath):
        path = os.path.join(PluginsPath, dir)
        if os.path.isdir(path):
            folder_ = pathlib.Path(path).resolve()
            if json.load(open(os.path.join(folder_, './config.json'), 'r'))['state'] == 'Disabled':
                continue
            else:
                Plugins_log.info(f"Loading plugin {dir} ({path})")
                filePath = os.path.join(folder_, './__init__.py')
                try:
                    with open(filePath, 'r') as f:
                        c = f.read()
                        c = c.replace('../../', '')
                        c = c.replace('...', '')
                        exec(c, globals())
                    
                    LoadedPluginsList.append(dir)
                    Plugins_log.info(f"Plugin {dir} loaded ({path})")
                except Exception as e:
                    Plugins_log.warning(f"Error loading plugin {dir}: {e} ({path})")
        # elif os.path.isfile(path):
        #     if file.endswith('.py'):
        #         module_name = file[:-3]
        #         module_path = os.path.join(PluginsPath, file)

        #         Plugins_log.info(f"Loading plugin {module_name} ({module_path})")

        #         try:
        #             with open(module_path, 'r') as f:
        #                 c = f.read()
        #                 c = c.replace('../', '')
        #                 c = c.replace('..', '')
        #                 exec(c, globals())
                    
        #             LoadedPluginsList.append(module_name)
        #             Plugins_log.info(f"Plugin {module_name} loaded ({module_path})")
        #         except Exception as e:
        #             Plugins_log.warning(f"Error loading plugin {module_name}: {e} ({module_path})")

def GetLoadedPlugins() -> list[str]:
    return LoadedPluginsList

def GetInstalledPluginsList() -> list[tuple[str, Literal['Enable', 'Disable']]]:
    InstalledPluginsList: list[tuple[str, Literal['Enable', 'Disable']]] = []
    for dir in os.listdir(PluginsPath):
        if os.path.isdir(os.path.join(PluginsPath, dir)):
            if json.load(open(os.path.join(PluginsPath, dir, './config.json'), 'r'))['state'] == 'Disabled':
                InstalledPluginsList.append((dir, 'Disable'))
            else:
                InstalledPluginsList.append((dir, 'Enable'))
    return InstalledPluginsList
