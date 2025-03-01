# Plugin Development Document - 插件开发文档

## 中文

创建：

```plaintext
VersionSystem\VersionSystemRules.md
B--0--0.1--_indev--2025*1*1 Version:
在 “plugins” 下创建一个文件夹
必须包含：
    1.config.json
    2.__init__.py
    3.自己的版本日志文件
    4.图标文件路径（建议为64X64或32X32的大小）
    5.描述信息的Markdown文件路径

config.json 文件格式：
{
    "EditionLogsFilePath": "版本日志文件路径",
    "state": "状态（启用（Enabled）/禁用（Disabled））",
    "IconFilePath": "图标文件路径",
    "OverviewText": "概述文本",
    "MarkdownFilePathForDescribingInformation": "描述信息的Markdown文件路径",
}
版本日志文件格式：
版本 Version:
    日志
版本 Version:
    日志
版本请参考VersionSystem/VersionSystemRules.md

```

导入：

```python
from ..PluginAPI import (
    # 要导入的东西
)
```

使用的UI库：tkinter、tkintertools
