import pymysql
from pymysql.cursors import DictCursor

# 连接数据库
# 第一种方法
conn = pymysql.connect(host='10.0.0.179', user='root', password='123456', database='test')
# 第二种方法
# 创建一个conn.json文件，里面包含下列内容
# {
#   "host": "10.0.0.179",
#   "user": "root",
#   "password": "123456",
#   "database": "test",
#   "port": 3306
# }

# with open('conn.json','r',encoding='utf-8') as f:
#     conf = simplejson.load(f)
# conn = pymysql.connect(**conf)


# 游标Cursor：执行 SQL 命令并对结果集进行迭代
# 1 新增数据
cursor = conn.cursor()  # 获取一个游标
for i in range(5):
    sql = "insert into students (name, age) values('tom-{}', {})".format(i, 20 + i)
    rows = cursor.execute(sql)  # 执行SQL命令
conn.commit()  # 事务提交
# conn.rollback()  # 事务回滚
# cursor.close()
# conn.close()

# 2 查询
sql = "select * from employees"
rows = cursor.execute(sql)
print(cursor.fetchone())  # 获取结果集的下一行，如果结果集中没有更多的行，则返回 None
print(cursor.fetchone())
print(cursor.rownumber, cursor.rowcount)  # 返回当前行号和总行数
print('1 -----------')
print(cursor.fetchmany(2))  # 返回2行，None则返回空元组
print(cursor.rownumber, cursor.rowcount)
print('2 ~~~~~~~~~~~')
print(cursor.fetchmany(2))
print(cursor.rownumber, cursor.rowcount)
print('3-----------')
print(cursor.fetchall())  # 返回剩余所有行，如果走到末尾，就返回空元组，否则返回一个元组，其元素是每一行的记录封装的一个元组
print(cursor.rownumber, cursor.rowcount)
print('4~~~~~~~~~~~')
cursor.rownumber = 0  # 可以修改行号，正负都支持，重复读
print(cursor.fetchone())

# 带列名查询。返回一行，是一个字典；返回多行，放在列表中，元素是字典，代表一行。
cursor = conn.cursor(DictCursor)

# 参数化查询，可以有效防止SQL注入攻击
sql = "select * from students where id=%s"
userid = '2 or 1=1'
rows = cursor.execute(sql, userid)  # (userid,)

sql = "select * from student where name like %(name)s and age > %(age)s"  # 仅测试用，通常不要用like
cursor.execute(sql, {'name': 'tom%', 'age': 25})

# 上下文支持
conn = None

try:  # 处理连接过程中可能出现的异常
    conn = pymysql.connect(**conf)
    with conn:
        try:  # 处理 SQL 查询过程中可能出现的异常
            with conn.cursor() as cursor:  # 获取一个游标,在退出 with 语句块时自动调用 cursor.close()。
                sql = "select * from student where id=%s"
                userid = 2
                rows = cursor.execute(sql, userid)
                print(cursor.fetchall())

            with conn.cursor() as cursor:
                sql = "select * from student where id=6"
                cursor.execute(sql)
                print(cursor.fetchall())

            conn.commit()
            
        except:
            conn.rollback()

except Exception as e:
    print(e)  # 记录错误到日志中
