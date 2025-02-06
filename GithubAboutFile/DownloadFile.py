from .FileExists import FileExists
import ghapi.all as ghapi, base64


def DownloadFile(access_token, owner, repo, file_path, local_path):
    """
    从 GitHub 仓库下载文件。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param file_path: GitHub 上的文件路径
    :param local_path: 本地保存路径
    """
    # 初始化 API 客户端
    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)
    
    # if FileExists(access_token, owner, repo, file_path):
    # 获取文件内容
    response = api.repos.get_content(path=file_path) # type: ignore
        
    # 解码文件内容
    decoded_content = base64.b64decode(response.content)
        
    # 将文件内容写入本地文件
    with open(local_path, 'wb') as f:
        f.write(decoded_content)
    