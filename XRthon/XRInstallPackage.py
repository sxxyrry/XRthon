from GithubAboutFile import *
from Encrypt_Decrypt import decrypt
from folder import folder
import os, shutil


class NotProvidedDataError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class ProvidedDataTooMuchError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

# 配置GitHub仓库信息
username = "sxxyrry"
repo_name = "XRthonDatabase"
local_path = os.path.join(folder, "./XRthonDatabase")
token = decrypt("1419404_1420545_1429673_1410276_1397725_1364636_1390879_1393161_1426250_1385174_1379469_\
1377187_1418263_1358931_1431955_1396584_1400007_1404571_1413699_\
1356649_1366918_1389738_1439942_1390879_1423968_1361213_1417122_1377187_1387456_\
1365777_1397725_1376046_1381751_1441083_1358931_1389738_1358931_1403430_1415981_1438801_", "sxxyrry-23XR")  # 用于认证
packages_path = os.path.join(folder, "./packages")


class Installer():
    def __init__(self):
        pass

    def install(self, name: str):
        filelist = GetFileAndDirsNameList(token, username, repo_name, '/packages')
        if name in filelist:
            if name in os.listdir(packages_path):
                print(f"Package {name} already exists.")
            else:
                try:
                    DownloadDir(token, username, repo_name, f"/packages/{name}", os.path.join(packages_path, f"{name}"))
                except FileNotFoundError:
                    print(f'Package {name} not found.')
                    return

                print(f'Installed {name}')
            
        elif f'{name}.XRthon' in filelist:
            if f'{name}.XRthon' in os.listdir(packages_path):
                print(f"Package {name} already exists.")
            else:
                DownloadFile(token, username, repo_name, f"/packages/{name}.XRthon", os.path.join(packages_path, f"{name}.XRthon"))

                print(f'Installed {name}')
        else:
            print(f'Package {name} not found.')

    def uninstall(self, name: str):
        filelist = GetFileAndDirsNameList(token, username, repo_name, '/packages')
        if name in filelist:
            if name in os.listdir(packages_path):
                os.remove(os.path.join(packages_path, name))
            else:
                print(f'Package {name} not installed.')
        else:
            print(f'Package {name} not found.')

def main():
    import sys
    if len(sys.argv) <= 2:
        raise NotProvidedDataError('Insufficient data provided')
    if len(sys.argv) >= 4:
        raise ProvidedDataTooMuchError('Too much data provided')
    arg = sys.argv.copy()
    installer = Installer()
    # print(f'{sys.argv=}')
    if arg[1] == 'install':
        installer.install(arg[2])
    elif arg[1] == 'uninstall':
        installer.uninstall(arg[2])
    else:
        print('Invalid command.')
    
    return

if __name__ == '__main__':
    main()
