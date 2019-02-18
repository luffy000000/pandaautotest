import pymysql

class DataBase():
    
    def __init__(self):
        self.conn = pymysql.connect(
            host = '47.98.34.57',
            port = 3306,
            user = 'root',
            password = '!qaz7410',
            db = 'panda',
            charset = 'utf8',
        )
    
    def execute_mysql(self, src):
        cur = self.conn.cursor()
        cur.execute(src)
        result = cur.fetchall()
        return result
        cur.close()
        self.conn.close()


    