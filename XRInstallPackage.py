from GithubAboutFile import *
from BaseGConfig import *
# from DecodeAndInstallPackage import DecodeAndInstallPackage
from colorama import init, Fore, Style
from folder import folder
import os, shutil


init()

# class NotProvidedDataError(Exception):
#     def __init__(self, message: str):
#         super().__init__(message)

# class ProvidedDataTooMuchError(Exception):
#     def __init__(self, message: str):
#         super().__init__(message)

# 配置GitHub仓库信息
repo_name = "XRthonDatabase"

packages_path = os.path.join(folder, "./packages")


class Installer():
    def __init__(self):
        pass

    def install(self, name: str):
        filelist = ListDir(token, username, repo_name, '/packages')
        if name in filelist:
            if name in os.listdir(packages_path):
                print(f'{Fore.YELLOW}Warning: Package "{name}" already exists.{Style.RESET_ALL}')
            else:
                try:
                    DownloadDir(token, username, repo_name, f"/packages/{name}", os.path.join(packages_path, f"{name}"))
                except FileNotFoundError:
                    print(f'{Fore.RED}Error: Package "{name}" not found.{Style.RESET_ALL}')

                print(f'Installed "{name}"')
            
        elif f'{name}.XRthon' in filelist:
            if f'{name}.XRthon' in os.listdir(packages_path):
                print(f'{Fore.YELLOW}Warning: Package "{name}" already exists.{Style.RESET_ALL}')
            else:
                DownloadFile(token, username, repo_name, f"/packages/{name}.XRthon", os.path.join(packages_path, f"{name}.XRthon"))

                print(f'Installed "{name}"')
        else:
            print(f'{Fore.RED}Error: Package "{name}" not found.{Style.RESET_ALL}')

    def uninstall(self, name: str):
        filelist = ListDir(token, username, repo_name, '/packages')
        if name in filelist:
            if name in os.listdir(packages_path):
                shutil.rmtree(os.path.join(packages_path, name))

                print(f'Package "{name}" was removed.')

            elif f'{name}.XRthon' in os.listdir(packages_path):
                os.remove(os.path.join(packages_path, name))

                print(f'Package "{name}" was removed.')

            else:
                print(f'Package "{name}" not installed.')
        else:
            print(f'{Fore.RED}Error: Package "{name}" not found.{Style.RESET_ALL}')

def main():
    import sys
    if len(sys.argv) <= 2:
        print(f'{Fore.RED}Error: Insufficient data provided.{Style.RESET_ALL}')
        input()

        return
    if len(sys.argv) >= 4:
        print(f'{Fore.RED}Error: Too much data provided.{Style.RESET_ALL}')
        input()

        return
    arg = sys.argv.copy()
    installer = Installer()
    # print(f'{sys.argv=}')
    if arg[1] == 'install':
        installer.install(arg[2])
    elif arg[1] == 'uninstall':
        installer.uninstall(arg[2])
    else:
        print(f'{Fore.RED}Error: Invalid command.{Style.RESET_ALL}')
    
    input()

    return

if __name__ == '__main__':
    main()
