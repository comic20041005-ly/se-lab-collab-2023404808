# auth.py
def login(u, p):
    if u == "admin" and p == "123456":
        return True
    return False