import base64
import ghapi.all as ghapi


def DeleteFile(access_token, owner, repo, file_path, commit_message):
    """
    在 GitHub 仓库中删除文件。

    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param file_path: 文件路径
    :param commit_message: 提交消息
    :return: 删除文件后的响应
    """

    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)
    try:
        current_file = api.repos.get_content(path=file_path) # type: ignore
        sha = current_file.sha
    except Exception as e:
        if 'status' in e.__dict__:
            if e.status == 404: # type: ignore
                sha = None
        else:
            raise e
    
    response = api.repos.delete_file( # type: ignore
        path=file_path,
        message=commit_message,
        sha=sha
    )

    return response
