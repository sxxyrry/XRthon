import ghapi.all as ghapi # type: ignore


def ListDir(access_token: str, owner: str, repo: str, dirpath: str) -> list[str]:
    """
    从 GitHub 仓库获取指定文件夹中的文件及文件夹的名称列表。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    """
    # 初始化 API 客户端
    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)
    
    # 获取文件内容
    response = api.repos.get_content(path=dirpath) # type: ignore
    
    return [item['name'] for item in response] # type: ignore