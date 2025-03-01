from .DirExists import DirExists
from .DownloadFile import DownloadFile
import ghapi.all as ghapi # type: ignore
import os


def DownloadDir(access_token: str, owner: str, repo: str, dir_path: str, local_path: str) -> None:
    """
    从 GitHub 仓库下载文件夹。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param dir_path: GitHub 上的文件路径
    :param local_path: 本地保存路径
    """
    # 初始化 API 客户端
    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)

    if DirExists(access_token, owner, repo, dir_path):
        try:
            response = api.repos.get_content(path=dir_path)  # type: ignore

            os.makedirs(local_path, exist_ok=True)

            for item in response: # type: ignore
                if item['type'] == 'file':
                    file_path = os.path.join(local_path, item['name']) # type: ignore
                    DownloadFile(access_token, owner, repo, item['path'], file_path) # type: ignore
                elif item['type'] == 'dir':
                    sub_dir_path = os.path.join(local_path, item['name']) # type: ignore
                    os.makedirs(sub_dir_path, exist_ok=True)
                    DownloadDir(access_token, owner, repo, item['path'], sub_dir_path) # type: ignore
        except Exception as e:
            raise Exception(f"Error downloading directory {dir_path}: {e}")
    else:
        raise FileNotFoundError(f"Directory not found: {dir_path}")