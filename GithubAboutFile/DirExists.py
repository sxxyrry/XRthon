import ghapi.all as ghapi


def DirExists(access_token, owner, repo, file_path):
    """
    查询 GitHub 仓库中是否存在指定文件夹。
    
    :param access_token: GitHub 个人访问令牌
    :param owner: 仓库所有者
    :param repo: 仓库名称
    :param file_path: 文件路径
    :return: 文件是否存在 (True/False)
    """
    # 初始化 API 客户端
    api = ghapi.GhApi(owner=owner, repo=repo, token=access_token)
    
    try:
        # 获取文件内容
        response = api.repos.get_content(path=file_path) # type: ignore
        
        # 如果返回结果是目录，则返回 True
        return isinstance(response, list)
    except Exception as e:
        if e.status == 404: # type: ignore
            return False
        else:
            raise e
