# auth.py

def authenticate_user(username, password):
    """
    验证用户登录凭证是否正确
    
    :param username: 用户名 (str)
    :param password: 密码 (str)
    :return: 验证通过返回 True，否则返回 False (bool)
    """
    # 实际开发中此处应查询数据库，实验中简化为硬编码判断
    if username == "admin" and password == "123456":
        return True
    return False