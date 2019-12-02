# ORM 链接数据库
from sqlalchemy import create_engine
# pymysql需要加上
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/news?charset=utf8')
# 模型声明（声明的class 都是继承他）
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# class需要使用到的数据类型
from sqlalchemy import Column, Integer, String, DateTime, Boolean


class News(Base):
    ''' 新闻类型 '''
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    #id = Column('news_id',Integer, primary_key=True) 字段名别名
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300))
    author = Column(String(20))
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)


# 创建表 帮我们把些sql的工作都完成了
News.metadata.create_all(engine)
# 如果报错Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 489") 不用管它 它是Mysql版本自带的警告 不影响建表

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

class OrmTest(object):

    def __init__(self):
        self.session = Session()

    def add_one(self):
        ''' 添加数据 '''
        new_obj = News(
            title='标题1',
            content='内容1',
            types="百家"
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj   # 每一个条记录都是一个class

    def get_one(self):
        return self.session.query(News).get(1)  # 查询id为1的数据

    def get_more(self):
        """  获取多条数据  """
        return self.session.query(News).filter_by(is_valid=True)  # 查询没有删除的 即 is_valid =1

    def update_data(self, pk):
        """ 修改单条数据 """
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            # 逻辑删除
            new_obj.is_valid = 0
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False  # 如果有数据就修改数据返回True，没有数据就直接返回False

    def update_data_more(self):
        """ 修改多条数据 """
        # data_list = self.session.query(News).filter_by(is_valid = False)
        data_list = self.session.query(News).filter(News.id >= 5)
        for item in data_list:
            item.is_valid = 1
            self.session.add(item)
        self.session.commit()
        pass

    def delete_data(self, pk):
        """ 删除单条数据  """
        # 获取删除的数据
        new_obj = self.session.query(News).get(pk)
        self.session.delete(new_obj)
        self.session.commit()

    def delete_data_more(self):
        """ 删除多条数据  """
        data_list = self.session.query(News).filter(News.id >= 5)
        for item in data_list:
            self.session.delete(item)
        self.session.commit()
        pass

def main():
    obj = OrmTest()
    # obj.update_data(1)
    # obj.update_data_more()
    # obj.delete_data(20)
    obj.delete_data_more()

if __name__ == '__main__':
    main()