import os, json
from typing import NoReturn
from folder import folder


class Config():
    def __init__(self):
        with open(os.path.join(folder, './config/language.json'), 'r') as f:
            self.language = json.load(f)['language']
        
        self.languageList = ['en', 'zh-cn']
    
    def SwitchLanguage(self, language: str) -> str | NoReturn:
        if language not in self.languageList: raise Exception('Language not found.')
        with open(os.path.join(folder, './config/language.json'), 'w') as f:
            json.dump({'language': language}, f)             
        
        self.language = language

        return language
    
