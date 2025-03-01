'''
# 版本系统规则

## 标记--主版本--版本号（--_indev标记）--年\\*月\\*第几次修改

```text
标记： O 或 B
    （ O 是正式版， B 是测试版）

主版本：
    若标记是 B 时：主版本强制为0
    若标记是 O 时：主版本大于等于1

版本号：
    x.y
    x： 版本1
    y： 版本2

_indev标记：表达是否是正在开发版，可以不加

年\\*月\\*第几次修改：表达修改时间、次数
```


'''

import re
from typing import NoReturn

from _del_ import del___pycache__


class VersionSystem():
    def __init__(self):
        pass

    @staticmethod
    def GetRules() -> str:
        return '''\
标记--主版本--版本号（--_indev标记）--年*月*第几次修改

标记： O 或 B
    （ O 是正式版， B 是测试版）

主版本：
    若标记是 B 时：主版本强制为0
    若标记是 O 时：主版本大于等于1

版本号：
    x.y
    x： 版本1
    y： 版本2

_indev标记：表达是否是正在开发版，可以不加

年*月*第几次修改：表达修改时间、次数\
'''

    @staticmethod
    def CheckVersion(version: str) -> bool:
        # 定义正则表达式模式
        pattern = r'^(O|B)--(\d+)--(\d+\.\d+)(--_indev)?--(\d{4})\*(\d{1,2})\*(\d+)$' # (\d{2})怎么加上是一个数字的情况
        
        # 匹配版本字符串
        match: re.Match[str] | None = re.fullmatch(pattern, version)
        if match is None:
            del___pycache__()
            return False
        
        # 提取匹配的各部分
        tag, major_version, version_number, indev, year, month, revision = match.groups() # type: ignore
        
        # 验证标记
        if tag not in ['O', 'B']:
            del___pycache__()
            return False
        
        # 验证主版本
        major_version = int(major_version)
        if tag == 'B' and major_version != 0:
            del___pycache__()
            return False
        if tag == 'O' and major_version < 1:
            del___pycache__()
            return False
        
        # 验证版本号
        try:
            version_parts = list(map(int, version_number.split('.')))
            if len(version_parts) != 2 or any(part < 0 for part in version_parts):
                del___pycache__()
                return False
        except ValueError:
            del___pycache__()
            return False
        
        # 验证年份、月份和修订次数
        try:
            year = int(year)
            month = int(month)
            revision = int(revision)
            if year < 1000 or year > 9999:
                del___pycache__()
                return False
            if month < 1 or month > 12:
                del___pycache__()
                return False
            if revision < 1:
                del___pycache__()
                return False
        except ValueError:
            del___pycache__()
            return False
        
        del___pycache__()
        return True

    @staticmethod
    def CompareVersions(version1: list, version2: list) -> int: # type: ignore
        # 比较标记
        if version1[0] != version2[0]:
            del___pycache__()
            return 1 if version1[0] == 'O' else -1
        
        # 比较主版本
        if version1[1] != version2[1]:
            del___pycache__()
            return 1 if version1[1] > version2[1] else -1
        
        # 比较次版本
        if version1[2] != version2[2]:
            del___pycache__()
            return 1 if version1[2] > version2[2] else -1
        
        # 比较小版本
        if version1[3] != version2[3]:
            del___pycache__()
            return 1 if version1[3] > version2[3] else -1
        
        # 比较是否为开发版
        if version1[4] != version2[4]:
            del___pycache__()
            return 1 if version1[4] else -1
        
        # 比较年份
        if version1[5] != version2[5]:
            del___pycache__()
            return 1 if version1[5] > version2[5] else -1
        
        # 比较月份
        if version1[6] != version2[6]:
            del___pycache__()
            return 1 if version1[6] > version2[6] else -1
        
        # 比较修订次数
        if version1[7] != version2[7]:
            del___pycache__()
            return 1 if version1[7] > version2[7] else -1
        
        del___pycache__()
        return 0

    @staticmethod
    def JudgeVersion_Greater(Version1: str, Version2: str) -> bool:
        try:
            NV1 = VersionSystem.GetNumberVersion(Version1).split('.')
            NV2 = VersionSystem.GetNumberVersion(Version2).split('.')
        except:
            del___pycache__()
            return False
        
        del___pycache__()
        return VersionSystem.CompareVersions(NV1, NV2) > 0 # type: ignore
        
    @staticmethod
    def JudgeVersion_Less(Version1: str, Version2: str) -> bool | NoReturn:
        try:
            NV1 = VersionSystem.GetNumberVersion(Version1).split('.')
            NV2 = VersionSystem.GetNumberVersion(Version2).split('.')
        except:
            del___pycache__()
            return False
        
        del___pycache__()
        return VersionSystem.CompareVersions(NV1, NV2) < 0 # type: ignore
    
    @staticmethod
    def JudgeVersion_Equal(Version1: str, Version2: str) -> bool | NoReturn:
        try:
            NV1 = VersionSystem.GetNumberVersion(Version1).split('.')
            NV2 = VersionSystem.GetNumberVersion(Version2).split('.')
        except:
            del___pycache__()
            return False
        
        del___pycache__()
        return VersionSystem.CompareVersions(NV1, NV2) == 0 # type: ignore

    @staticmethod
    def GetNumberVersion(version: str) -> str | NoReturn:
        if VersionSystem.CheckVersion(version):
            # 定义正则表达式模式
            pattern = r'^(O|B)--(\d+)--(\d+\.\d+)(--_indev)?--(\d{4})\*(\d{1,2})\*(\d+)$'
        
            # 匹配版本字符串
            match = re.match(pattern, version)
            
            if match is None:
                del___pycache__()
                raise ValueError('Invalid version format')

            # 提取匹配的各部分
            tag, major_version, version_number, indev, year, month, revision = match.groups()

            del___pycache__()
            return f'{'1.' if tag == 'O' else '0.'}{'0.' if indev else '.'}{major_version}.{version_number}.{year}.{month}.{revision}'
        else:
            del___pycache__()
            raise ValueError('Invalid version format')

del___pycache__()

if __name__ == '__main__':
    print(VersionSystem.GetRules())
    print(VersionSystem.CheckVersion('B--0--1.0--_indev--2023*10*1'))  # 应该返回 True
    print(VersionSystem.CheckVersion('O--1--1.0--2023*10*1'))          # 应该返回 True
    print(VersionSystem.CheckVersion('B--1--1.0--_indev--2023*10*1'))  # 应该返回 False
    print(VersionSystem.CheckVersion('O--0--1.0--2023*10*1'))          # 应该返回 False
    print(VersionSystem.CheckVersion('B--0--1.0--2023*13*1'))          # 应该返回 False
    print(VersionSystem.CheckVersion('B--0--1.0--2023*10*0'))          # 应该返回 False
