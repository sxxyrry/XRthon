import sys, os, pathlib

folder = pathlib.Path(__file__).parent.resolve()

# print(f'setx PATH "%PATH%;{folder}"')
# print()

# 在Windows系统的环境变量中的PATH增加本文件的文件夹路径（即本文件夹的folder变量）
if sys.platform == 'win32':
    print('请先右键在桌面的此电脑，在弹出的窗口中寻找并点击“高级系统设置”，找到“环境变量”，选择用户变量的“Path”点击“编辑”')
    print(f'在弹出的窗口中点击“新建”，输入以下内容“{folder}”，点击“确定”，此操作重启系统后生效')

# print(os.environ['PATH'])

input()
