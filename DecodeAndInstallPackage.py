from Encrypt_Decrypt import decrypt
import os, base64, py7zr, yaml, shutil
from folder import folder
from ConfigType import Config

class ManyError(BaseException):
    def __init__(self, *args: object):
        super().__init__(*args)

class ManyFilesError(ManyError):
    def __init__(self, *args: object):
        super().__init__(*args)

class ManyDirsError(ManyError):
    def __init__(self, *args: object):
        super().__init__(*args)

class UncompletedError(BaseException):
    def __init__(self, *args: object):
        super().__init__(*args)

packages_path = os.path.join(folder, "./packages")

def DecodeAndInstallPackage(PackagePath: str):
    temppatha = os.path.join(folder, f'./temp/{os.path.split(PackagePath)[1][:-8]}')
    temppathb = os.path.join(folder, f'./temp/{os.path.split(PackagePath)[1][:-8]}.package_7z')
    temppathc = os.path.join(folder, f'./temp/{os.path.split(PackagePath)[1][:-8]}-Code')

    with open(PackagePath, 'r', encoding='UTF-8') as f:
        text = f.read()

        list_ = text.split('\n')

        key = list_[0]
        text = list_[1]

        de_text = decrypt(text, key)

        de_bytes = base64.b64decode(de_text)

        with open(temppathb, 'wb') as f:
            f.write(de_bytes)

    with py7zr.SevenZipFile(temppathb, 'r') as f:
        f.extractall(temppatha)
   
    with open(os.path.join(temppatha, './config.yaml')) as f:
        config: Config = yaml.safe_load(f.read())

        for k, v in config.items():
            config[k] = str(v)
        
        print(config)

    with py7zr.SevenZipFile(os.path.join(temppatha, './Code.7z'), 'r') as f:
        f.extractall(temppathc)

    name = config['name']

    _ = 0

    for i in os.listdir(temppathc):
        if os.path.isfile(os.path.join(temppathc, i)):
            _ += 0
        if os.path.isdir(os.path.join(temppathc, i)):
            _ = 1

    if _:
        # Dir Logic
        if len(os.listdir(temppathc)) > 1:
            raise ManyDirsError(f'Many dirs ({', '.join(os.listdir(temppathc))}).')
        if len(os.listdir(temppathc)) == 1:
            raise UncompletedError('Dir logic is uncompleted.')
            pass
    else:
        # File Logic
        if len(os.listdir(temppathc)) > 1:
            raise ManyFilesError(f'Many files ({', '.join(os.listdir(temppathc))}).')
        if len(os.listdir(temppathc)) == 1:
            shutil.copy2(os.path.join(temppathc, os.listdir(temppathc)[0]), os.path.join(packages_path, os.listdir(temppathc)[0]))


    shutil.rmtree(temppatha)
    os.remove(temppathb)
    shutil.rmtree(temppathc)

DecodeAndInstallPackage(os.path.join(folder, './test1.package'))
