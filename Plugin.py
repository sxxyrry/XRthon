import os, shutil
from typing import Literal
from folder import folder
from PluginAPI import *
from GithubAboutFile import GetFileAndDirsNameList, DownloadDir
from BaseGConfig import token
from logs import Plugins_log


PluginsPath = os.path.join(folder, './plugins')
VirtualEnvironmentPath = os.path.join(folder, './VirtualEnvironment')

def GetAllPlugins() -> list[str]:
    return GetFileAndDirsNameList(token, 'sxxyrry', 'XRthonPluginsDatabase', 'Plugins')

def UninstallPlugin(PluName: str):
    if os.path.exists(os.path.join(PluginsPath, f'./{PluName}')):
        shutil.rmtree(os.path.join(PluginsPath, f'./{PluName}'))

def InstallPlugin(PluName: str):
    DownloadDir(token, 'sxxyrry', 'XRthonPluginsDatabase', f'Plugins/{PluName}', os.path.join(PluginsPath, f'./{PluName}'))

def LoadPlugins():
    for dir in os.listdir(PluginsPath):
        path = os.path.join(PluginsPath, dir)
        if os.path.isdir(path):
            path = pathlib.Path(path).resolve()
            
            if os.path.exists(os.path.join(path, './config.json')):
                with open(os.path.join(path, './config.json'), 'r', encoding='UTF-8') as f:
                    config: dict[str, str] = yaml.safe_load(f)
                
                if config['state'] == 'Disabled':
                    continue
                else:
                    Plugins_log.info(f"Loading plugin {dir} ({path})")
                    filePath = os.path.join(path, './__init__.py')
                    try:
                        with open(filePath, 'r', encoding='UTF-8') as f:
                            c = f.read()
                            c = c.replace('../../', '')
                            c = c.replace('...', '')
                            exec(c, globals())
                        
                        LoadedPluginsList.append(dir)
                        Plugins_log.info(f"Plugin {dir} loaded ({path})")
                    except Exception as e:
                        Plugins_log.warning(f"Error loading plugin {dir}: {e} ({path})")
            else:
                Plugins_log.error(f"Plugin {dir} is not a valid plugin (No config.json) ({path})")
                raise Exception(f"Plugin {dir} is not a valid plugin (No config.json) ({path})")
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

def GetInstalledPluginsList() -> list[tuple[str, Literal['Enabled', 'Disabled']]]:
    InstalledPluginsList: list[tuple[str, Literal['Enabled', 'Disabled']]] = []
    for dir in os.listdir(PluginsPath):
        if os.path.isdir(os.path.join(PluginsPath, dir)):
            if json.load(open(os.path.join(PluginsPath, dir, './config.json'), 'r'))['state'] == 'Disabled':
                InstalledPluginsList.append((dir, 'Disabled'))
            else:
                InstalledPluginsList.append((dir, 'Enabled'))
    return InstalledPluginsList
