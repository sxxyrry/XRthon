from .DirExists import DirExists
from .DownloadFile import DownloadFile
import ghapi.all as ghapi, os


def DownloadDir(access_token, owner, repo, dir_path, local_path):
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
        response = api.repos.get_content(path=dir_path) # type: ignore

        for item in response:
            if item['type'] == 'file':
                file_path = os.path.join(local_path, item['name'])
                DownloadFile(access_token, owner, repo, item['path'], file_path)
            elif item['type'] == 'dir':
                sub_dir_path = os.path.join(local_path, item['name'])
                os.makedirs(sub_dir_path, exist_ok=True)
                DownloadDir(access_token, owner, repo, item['path'], sub_dir_path)
    
    else:
        raise FileNotFoundError(f"Directory not found: {dir_path}")
