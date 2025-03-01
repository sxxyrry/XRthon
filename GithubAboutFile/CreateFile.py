import base64
import ghapi.all as ghapi # type: ignore


def CreateFile(access_token: str, owner: str, repo: str, file_path: str, commit_message: str, content: str) -> None:
    """
    在 GitHub 仓库中创建文件。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param file_path: 文件路径
    :param commit_message: 提交消息
    :param content: 文件内容
    """
    # 初始化 API 客户端
    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)
    
    # 将文件内容转换为 base64 编码
    encoded_content = base64.b64encode(content.encode())

    # 获取当前仓库的提交记录
    commits = api.get_commits() # type: ignore

    # 获取最新提交的 SHA 值
    latest_commit_sha = commits[0]['sha'] # type: ignore

    try:
        current_file = api.get_file(file_path, latest_commit_sha) # type: ignore
        sha = current_file.sha # type: ignore
    except Exception:
        sha = None
    
    response = api.update_file( # type: ignore
        path=file_path,
        message=commit_message,
        content=encoded_content,
        sha=sha
    )
