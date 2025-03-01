import ghapi.all as ghapi # type: ignore


def FileExists(access_token: str, owner: str, repo: str, file_path: str):
    """
    查询 GitHub 仓库中是否存在指定文件。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param file_path: 文件路径
    :return: 文件是否存在 (True/False)
    """
    # 初始化 API 客户端
    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)
    
    try:
        # 尝试获取文件内容
        api.repos.get_content(path=file_path) # type: ignore
        return True
    except Exception as e:
        if e.status == 404: # type: ignore
            return False
        else:
            raise e
