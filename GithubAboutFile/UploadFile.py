import base64
import ghapi.all as ghapi
from .GetFileText import GetFileText


def UploadFile(access_token, owner, repo, file_path, commit_message, path):
    """
    上传文件到 GitHub 仓库。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param file_path: 文件路径
    :param commit_message: 提交消息
    :param path: 文件保存路径
    """
    # 初始化 API 客户端
    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)
    
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # 将文件内容转换为 base64 编码
    encoded_content = base64.b64encode(file_content).decode('utf-8') # type: ignore
    
    # 上传文件到 GitHub
    response = api.repos.create_or_update_file_contents( # type: ignore
        path=path,
        message=commit_message,
        content=encoded_content,
        encoding='UTF-8'
    )

    # print(f"File {file_path} has been uploaded.")
