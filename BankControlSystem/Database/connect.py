import pymysql


# 创建数据表
def connect(host, user, password, database, sql, data):
    """
    :param host: 主机名
    :param user: 用户  root
    :param password: 密码
    :param database: 数据库的名字
    :param sql: sql语句
    """
    db = pymysql.connect(host, user, password, database, charset="utf8")
    # 链接数据库
    cursor = db.cursor()
    # 游标
    cursor.execute(sql, data)
    # 执行sql语句
    # 关闭
    cursor.close()
    db.close()


# 插入更新 删除
def IUD(host, user, password, database, sql):
    """
        :param host: 主机名
        :param user: 用户  root
        :param password: 密码
        :param database: 数据库的名字
        :param sql: sql语句
        """
    db = pymysql.connect(host, user, password, database, charset="utf8")
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("成功")
    except Exception as err:
        # Rollback in case there is any error
        db.rollback()
        print(err)
    # 关闭数据库连接
    db.close()


# 查询
def Select(host, user, password, database, sql):
    """
        :param host: 主机名
        :param user: 用户  root
        :param password: 密码
        :param database: 数据库的名字
        :param sql: 查询sql语句
        """
    # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    # fetchall(): 接收全部的返回结果行.
    # rowcount: 这是一个只读属性，并返回执行execute()
    # 方法后影响的行数。
    db = pymysql.connect(host, user, password, database, charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        return results
    except:
        print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()
