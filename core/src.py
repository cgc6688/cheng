import os
import pickle
dic_msg = """
    1-管理员注册
    2-管理员登陆
"""
admin = {'username':None}
def admin_register():
    username = input('请输入用户名:')
    password = input('请输入密码:')
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'admin')
    file = os.path.join(filepath,f'{username}.pkl')
    if os.path.exists(file):
        print('用户名已存在!')
    else:
        user = {'username':username,'password':password}
        with open(file,'wb') as fw:
            pickle.dump(user,fw)
        print('注册成功!')

def admin_login():
    username = input('请输入用户名:')
    password = input('请输入密码:')
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'admin')
    file = os.path.join(filepath, f'{username}.pkl')
    if not os.path.exists(file):
        print('用户名不存在!')
    else:
        with open(file,'rb') as fr:
            user = pickle.load(fr)
        if user['password'] == password:
            admin['username'] = username
            print('登录成功!')
        else:
            print('密码错误!')

dic_func = {
    '1':admin_register,
    '2':admin_login
}

def run():
    while True:
        print(dic_msg)
        choice = input('请输入你要选择的功能编号:(q退出)')
        if choice == 'q':
            break
        if choice not in dic_func:
            print('你的输入有误1')
            continue
        dic_func[choice]()

if __name__ == '__main__':
    run()