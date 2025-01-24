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
            return False
        
        # 提取匹配的各部分
        tag, major_version, version_number, indev, year, month, revision = match.groups()
        
        # 验证标记
        if tag not in ['O', 'B']:
            return False
        
        # 验证主版本
        major_version = int(major_version)
        if tag == 'B' and major_version != 0:
            return False
        if tag == 'O' and major_version < 1:
            return False
        
        # 验证版本号
        try:
            version_parts = list(map(int, version_number.split('.')))
            if len(version_parts) != 2 or any(part < 0 for part in version_parts):
                return False
        except ValueError:
            return False
        
        # 验证年份、月份和修订次数
        try:
            year = int(year)
            month = int(month)
            revision = int(revision)
            if year < 1000 or year > 9999:
                return False
            if month < 1 or month > 12:
                return False
            if revision < 1:
                return False
        except ValueError:
            return False
        
        return True

    @staticmethod
    def GetNumberVersion(version: str) -> str:
        if VersionSystem.CheckVersion(version):
            # 定义正则表达式模式
            pattern = r'^(O|B)--(\d+)--(\d+\.\d+)(--_indev)?--(\d{4})\*(\d{2})\*(\d+)$'
        
            # 匹配版本字符串
            match = re.match(pattern, version)
            
            if match is None:
                raise ValueError('Invalid version format')

            # 提取匹配的各部分
            tag, major_version, version_number, indev, year, month, revision = match.groups()

            return f'{major_version}.{version_number}{' _indev' if indev else ''} {year}*{month}*{revision}'
        else:
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
