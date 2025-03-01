import os, base64, py7zr, yaml, shutil
from Encrypt_Decrypt import encrypt
from folder import folder
from ConfigType import Config


def CreatePackage7zFile(Code7zFile: str, outputPath: str):
    # , outputPath: str = ''
    if py7zr.is_7zfile(Code7zFile):
        with py7zr.SevenZipFile(outputPath, 'w') as _7zFile:
            config: Config = {
                            'name'            : '',
                            'version'         : '',
                            'number_version'  : '',
                            'author'          : ''
                            }

            config['author'] = input('Package Author :')

            config['number_version'] = input('Package Number Version :')

            config['version'] = input('Package Version :')

            config['name'] = input('Package Name :')

            temppatha = os.path.join(folder, './temp/config.yaml')

            temppathb = os.path.join(folder, './temp/Code.7z')

            with open(temppatha, 'w', encoding='UTF-8') as f:
                yaml.safe_dump(config, f, encoding='UTF-8')

            print()

            shutil.copy(Code7zFile, temppathb)

            _7zFile.write(temppatha, './config.yaml')

            _7zFile.write(temppathb, './Code.7z')
        
            os.remove(temppatha)
            os.remove(temppathb)

def CreatePackageTextFile(_7zFilePath: str, outputPath: str):
    # , outputPath: str = ''
    _7zFilePath = os.path.join(_7zFilePath)
    if os.path.exists(_7zFilePath):
        if os.path.isfile(_7zFilePath):
            if py7zr.is_7zfile(_7zFilePath):
                with open(_7zFilePath, 'rb') as fp:
                    FileContent = fp.read()
                    Base64FileContent = str(base64.b64encode(FileContent))[1:][:-1]
                
                temppath = os.path.join(folder, f'./temp/{_7zFilePath.split('/')[-1]}')

                with py7zr.SevenZipFile(_7zFilePath, 'r') as archive:
                    archive.extractall(temppath)
                
                with open(os.path.join(temppath, './config.yaml'), 'r', encoding='UTF-8') as f:
                    config: Config = yaml.safe_load(f.read())

                for k, v in config.items():
                    config[k] = str(v)

                key = '-'.join(list(config.values())) # type: ignore

                text_ = encrypt(Base64FileContent, key) # type: ignore

                shutil.rmtree(temppath)

                with open(outputPath, 'w', encoding='UTF-8') as f:
                    f.write(f'{key}\n{text_}')

                # print(text_)

# CreatePackage7zFile(os.path.join(folder, './packages/Code.7z'), os.path.join(folder, './test1.package_7z'))
CreatePackageTextFile(os.path.join(folder, './test1.package_7z'), os.path.join(folder, './test1.package'))
