import base64
import ghapi.all as ghapi
# from .FileExists import FileExists


def AddLineToFile(access_token, owner, repo, file_path, commit_message, content):
    """
    在 GitHub 仓库中修改文件，以加入一行新内容。
    
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

    # 获取当前文件的内容作为字符串
    old_content = base64.b64encode(current_file.content.encode()).decode('utf-8') if sha else ''

    # 将新的内容编码为Base64
    new_content_encoded = base64.b64encode(content.encode()).decode('utf-8')

    # 合并旧内容和新内容
    combined_content = base64.b64encode(f"{old_content}\n{new_content_encoded}".encode()).decode('utf-8')

    # 使用编码后的字符串内容更新或创建文件
    try:
        response = api.repos.create_or_update_file_contents( # type: ignore
            path=file_path,
            message=commit_message,
            content=combined_content,
            sha=sha,
            encoding='UTF-8',
        )
    except Exception as e:
        # if "Unprocessable Entity" in str(e):
        #     raise e
        #     pass
        # else:
            raise e
