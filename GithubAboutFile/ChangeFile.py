import base64
import ghapi.all as ghapi
# from .FileExists import FileExists


def ChangeFile(access_token, owner, repo, file_path, commit_message, content):
    """
    在 GitHub 仓库中修改文件。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param file_path: 文件路径
    :param commit_message: 提交消息
    :param content: 文件内容
    """
    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)

    try:
        current_file = api.repos.get_content(path=file_path) # type: ignore
        sha = current_file.sha
    except Exception as e:
        if hasattr(e, 'status') and e.status == 404: # type: ignore
            sha = None
        else:
            raise e
    
    # if FileExists(access_token, owner, repo, file_path):

    # 将内容转换为字节，再进行Base64编码，并解码为字符串
    encoded_content = base64.b64encode(content.encode()).decode('utf-8')

    # 使用编码后的字符串内容更新或创建文件
    response = api.repos.create_or_update_file_contents( # type: ignore
        path=file_path,
        message=commit_message,
        content=encoded_content,
        sha=sha
    )
