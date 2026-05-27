# auth.py
def login(u, p):
    # TODO: 这里需要添加用户登录逻辑
    if u == "admin" and p == "123456":
        return True
    return False