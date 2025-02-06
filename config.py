import os, yaml
from typing import Literal, NoReturn
from folder import folder


class Config():
    def __init__(self):
        with open(os.path.join(folder, './config/language.yaml'), 'r') as f:
            self.language: Literal['en', 'zh-cn'] = yaml.safe_load(f)['language']
        
        with open(os.path.join(folder, './config/VS.yaml'), 'r') as f:
            self.VS: Literal['DEV', 'NAL'] = yaml.safe_load(f)['VS']

        if self.language not in ['en', 'zh-cn']: raise Exception('Language not found.')
        if self.VS not in ['DEV', 'NAL']:
            raise Exception('Error!')

        self.languageList = ['en', 'zh-cn']
    
    def SwitchLanguage(self, language: Literal['en', 'zh-cn']) -> str | NoReturn:
        if language not in self.languageList: raise Exception('Language not found.')
        with open(os.path.join(folder, './config/language.json'), 'w') as f:
            yaml.dump({'language' : language}, f)             
        
        self.language = language

        return language
    
