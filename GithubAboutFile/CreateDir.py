from .CreateFile import CreateFile


def CreateDir(access_token: str, owner: str, repo: str, dir_path: str, commit_message: str) -> None:
    """
    在 GitHub 仓库中创建目录。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param dir_path: 目录路径
    :param commit_message: 提交消息
    :prompt 副作用：创建一个名为 “a” 空文件作为目录的支持文件。
    """
    # 创建一个空文件作为目录的支持文件
    CreateFile(access_token, owner, repo, f'{dir_path}/a', commit_message, "")