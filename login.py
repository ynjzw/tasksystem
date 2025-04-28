import sqlite3
from getpass import getpass

# 创建数据库连接
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# 创建用户表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

def register():
    print("=== 注册 ===")
    username = input("请输入用户名: ")
    password = getpass("请输入密码: ")
    confirm_password = getpass("请确认密码: ")

    if password != confirm_password:
        print("两次输入的密码不一致！")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("注册成功！")
    except sqlite3.IntegrityError:
        print("用户名已存在！")

def login():
    print("=== 登录 ===")
    username = input("请输入用户名: ")
    password = getpass("请输入密码: ")

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        print("登录成功！欢迎,", username)
    else:
        print("用户名或密码错误！")

def main():
    while True:
        print("\n1. 注册")
        print("2. 登录")
        print("3. 退出")
        choice = input("请选择操作: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("退出系统。")
            break
        else:
            print("无效的选择，请重试。")

if __name__ == "__main__":
    main()

# 关闭数据库连接
conn.close()
