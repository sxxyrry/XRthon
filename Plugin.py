import os, shutil
from PIL import Image, ImageTk
# from PIL.ImageFile import ImageFile
from typing import Literal, TypedDict
from folder import folder
from PluginAPI import *
from GithubAboutFile import ListDir, DownloadDir
from BaseGConfig import token
from logs import Plugins_log


PluginsPath = os.path.join(folder, './plugins')
PluginsIconDict: dict[str, ImageTk.PhotoImage] = {}

def GetAllPlugins() -> list[str]:
    return ListDir(token, 'sxxyrry', 'XRthonPluginsDatabase', 'Plugins')

def UninstallPlugin(PluName: str):
    if os.path.exists(os.path.join(PluginsPath, f'./{PluName}')):
        shutil.rmtree(os.path.join(PluginsPath, f'./{PluName}'))

def InstallPlugin(PluName: str):
    DownloadDir(token, 'sxxyrry', 'XRthonPluginsDatabase', f'Plugins/{PluName}', os.path.join(PluginsPath, f'./{PluName}'))

def LoadPlugins():
    for dir_ in os.listdir(PluginsPath):
        if dir_ == 'a' and os.path.isfile(os.path.join(PluginsPath, dir_)):
            continue
        path = os.path.join(PluginsPath, dir_)
        if IsPlugin(path):
            path = pathlib.Path(path).resolve()
            
            with open(os.path.join(path, './config.json'), 'r', encoding='UTF-8') as f:
                config: dict[str, str] = yaml.safe_load(f)
            
            if config['state'] == 'Disabled':
                continue
            else:
                Plugins_log.info(f"Loading plugin {dir_} ({path})")
                filePath = os.path.join(path, './__init__.py')

                try:
                    with open(filePath, 'r', encoding='UTF-8') as f:
                        c = f.read()
                        c = c.replace('../../', '')
                        c = c.replace('...', '')
                        exec(c, globals())
                    
                    LoadedPluginsList.append(dir_)
                    Plugins_log.info(f"Plugin {dir_} loaded ({path})")
                except Exception as e:
                    Plugins_log.warning(f"Error loading plugin {dir_}: {e} ({path})")
        else:
            Plugins_log.warning(f"Plugin {dir_} isn't a plugin ({path})")
            raise Exception(f"Plugin {dir_} isn't a plugin ({path})")
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

def IsPlugin(Path: str) -> bool:
    if os.path.isdir(Path):
        if os.path.exists(os.path.join(Path, '__init__.py')):
            if os.path.exists(os.path.join(Path, 'config.json')):
                try:
                    with open(os.path.join(Path, 'config.json'), 'r') as f: config: dict[str, str] = json.load(f)
                except Exception: return False
                
                if "EditionLogsFilePath" in config and "state" in config and "IconFilePath" in config and "OverviewText" in config and "MarkdownFilePathForDescribingInformation" in config:
                    if config["state"] == "Enabled" or config["state"] == "Disabled":
                        if os.path.exists(os.path.join(Path, config["EditionLogsFilePath"])) and os.path.exists(os.path.join(Path, config["IconFilePath"])) and os.path.exists(os.path.join(Path, config["MarkdownFilePathForDescribingInformation"])):
                            if config["EditionLogsFilePath"].endswith('txt'):
                                try: 
                                    with open(os.path.join(Path, config["EditionLogsFilePath"]), 'r', encoding='UTF-8') as f: f.read();f.close()
                                except Exception: return False
                            if config["IconFilePath"].endswith('png') or config["IconFilePath"].endswith('jpg') or config["IconFilePath"].endswith('jpeg') or config["IconFilePath"].endswith('gif'):
                                try: Image.open(os.path.join(Path, config["IconFilePath"]))
                                except Exception: return False
                            if config["MarkdownFilePathForDescribingInformation"].endswith('md'):
                                try: 
                                    with open(os.path.join(Path, config["MarkdownFilePathForDescribingInformation"]), 'r', encoding='UTF-8') as f: f.read();f.close()
                                except Exception: return False
                            return True
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False
    else: return False

def GetLoadedPlugins() -> list[str]:
    return LoadedPluginsList

class PluginType_(TypedDict):
    EditionLogsFilePath: str
    state: Literal["Enabled", "Disabled"]
    IconFilePath: str
    OverviewText: str
    MarkdownFilePathForDescribingInformation: str

def GetInstalledPluginsList() -> list[tuple[str, Literal['Enabled', 'Disabled'], Image.Image, str, str]]:
    InstalledPluginsList: list[tuple[str, Literal['Enabled', 'Disabled'], Image.Image, str, str]] = []
    for dir_ in os.listdir(PluginsPath):
        if IsPlugin(os.path.join(PluginsPath, dir_)):
            with open(os.path.join(PluginsPath, dir_, './config.json'), 'r', encoding='UTF-8') as jsonf:
                config: PluginType_ = yaml.safe_load(jsonf)
            IFP = os.path.join(PluginsPath, dir_, config["IconFilePath"])
            img = Image.open(IFP)
            img = img.resize((64, 64)) # type: ignore

            OverviewText = config["OverviewText"]
            MDFPFDI = config["MarkdownFilePathForDescribingInformation"]
            with open(os.path.join(PluginsPath, dir_, MDFPFDI), 'r', encoding='UTF-8') as f:
                InfoMDContent = f.read()

            # image = ImageTk.PhotoImage(img)
            InstalledPluginsList.append((dir_, config['state'], img, OverviewText, InfoMDContent))
    return InstalledPluginsList
