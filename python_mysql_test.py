import pymysql
# 写一个 数据库操作的类


#中文输出. 只是为了在控制台上显示，字符的类型是正确的。
def chinese_output(str_tuple):
    for i in range(len(str_tuple)):
        print(str_tuple[i])
    pass


#将获取链接封装成calss
class MysqlSearch(object):  # 让MysqlSearch类继承object对象

    def __init__(self): # 在初始化的时候调用
        self.get_conn()


    def get_conn(self): # 数据库链接
        try:
            self.conn = pymysql.connect(
                host = "127.0.0.1",
                user = "root",
                passwd = "123456",
                db = "school",
                port = 3306,
                charset = 'utf8'
                )
        except pymysql.Error as e:
            print("Error : %s" % e)

    def close_conn(self):   #关闭数据库
        try:
            if self.conn:
                # 关闭链接
                self.conn.close()
        except pymysql.Error as e:
            print("Error: %s" % e)

    def get_one(self): #查询一条数据
        """ 流程："""
        # 1.准备SQL
        sql = "SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;"
        # 2.找到cursor
        cursor = self.conn.cursor()
        # 3.执行SQL
        cursor.execute(sql, ("本地", ))
         # 这边传的参数是一个元组
        # print cursor.rowcount # 一共多少行
        # print cursor.description
        # 4.拿到结果
        # rest = cursor.fetchone() # 就查询一体哦啊结果
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 5.处理数据
        #print rest
        #print rest['title']
        # 6.关闭cursor链接  两个关闭
        cursor.close()
        self.close_conn()

        return rest

    def get_more(self):
        sql = "SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;"
        cursor = self.conn.cursor()
        cursor.execute(sql, ("本地", ))
        # 多条数据获取的应该是一个list
        # 列表推倒式子
        rest = [dict(zip([k[0] for k in cursor.description], row))
            for row in cursor.fetchall() ]
        cursor.close()
        self.close_conn()
        return rest


    # 多条数据换页
    def get_more_page(self, page, page_size):
        # 页面换算
        offset = (page - 1) * page_size # 启始页面

        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC LIMIT %s, %s;'
        cursor = self.conn.cursor()
        # 将数字转换为字符.  不用转换。 瞎忙活。
        # offset_str = str(offset)
        # page_size_str = str(page_size)

        cursor.execute(sql, ('本地', offset, page_size, ))
        # 多条数据获取的应该是一个list
        # 列表推倒式子
        rest = [dict(zip([k[0] for k in cursor.description], row))
            for row in cursor.fetchall() ]
        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        """事务处理"""
        try:
            # 准备SQL
            sql =(
                "INSERT INTO `news` (`title`, `image`, `content`, `types`, `is_valid`) VALUE "
                "( %s, %s, %s, %s, %s );"
            )
             # 出现换行的时候用一个元组扩起来。 应用双引号扩起来
            # 获取链接和cursor
            cursor = self.conn.cursor()
            # 执行SQL
            cursor.execute(sql, ('标题7','0122.png', '新闻内容22', '推荐', 1))
            cursor.execute(sql, ('标题8','0122.png', '新闻内容22', '推荐', '2'))
            # 错误
            # 提交数据到数据库
            """ 如果不提交的事务的话。就是 已经提交多数据库 但是没有被保存  """
            # 提交事务
            self.conn.commit()
            # 关闭cursor
            cursor.close()
        except :
            print("Error")
            # self.conn.commit() # 部分提交
            self.conn.rollback() # 回滚
        # 关闭链接
        self.close_conn()

# 多选 + / 多行注释

def main():
    obj = MysqlSearch()

    #单个结果输出
    # rest = obj.get_one()
    # print rest['title']

    #多个结果删除。list
    # rest_more = obj.get_more()
    # for item in rest_more:
    #     print item
    #     print '-----------------------------------------------------------------------'

    #分页输出
    # rest_more_page = obj.get_more_page(1,1)
    # for item in rest_more_page:
    #     print item
    #     print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    obj.add_one()

if __name__ == '__main__':
    main()