import pymysql


class DBUtil:
    config = {
        # localhost
        'host': '10.0.0.179',
        'port': 3306,
        'user': 'root',
        'passwd': '123456',
        'db': 'test',
        'charset': 'utf8'
    }

    def __init__(self) -> None:
        '''
        获取链接
        获取游标
        '''
        self.con = pymysql.connect(**DBUtil.config)
        self.cursor = self.con.cursor()

    def close(self) -> None:
        '''
        关闭链接与游标
        '''
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()

    def execute_dml(self, sql, *args):
        '''
        可以执行dml语句，用于数据的增加、删除、修改
        '''
        try:
            # 执行SQL
            self.cursor.execute(sql, args)
            # 提交事务
            self.con.commit()
        except Exception as e:
            print(e)
            if self.con:
                self.con.rollback()
        finally:
            self.close()

    def execute_dml_back_id(self, sql, *args):
        '''
        可以执行dml语句，用于数据的增加
        '''
        try:
            # 执行SQL
            self.cursor.execute(sql, args)
            # 获取添加的id
            id = self.con.insert_id()
            # 提交事务
            self.con.commit()
            # 返回id
            return id
        except Exception as e:
            print(e)
            if self.con:
                self.con.rollback()
        finally:
            self.close()

    def query_one(self, sql, *args):
        '''
        获取一条数据
        '''
        try:
            # 执行SQL
            self.cursor.execute(sql, args)
            # 获取结果
            rs = self.cursor.fetchone()
            # 返回数据
            return rs
        except Exception as e:
            print(e)
        finally:
            self.close()

    def query_all(self, sql, *args):
        '''
        获取所有数据
        '''
        try:
            # 执行SQL
            self.cursor.execute(sql, args)
            # 获取结果,并返回数据
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close()
