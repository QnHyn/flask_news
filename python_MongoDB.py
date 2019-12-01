# python 直接对MongDB数据库操作
from pymongo import MongoClient
from datetime import datetime


class TestMongo:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['blog']

    def add_one(self):
    # 新增一条数据
        post = {
            'title': '标题',
            'content': ' 内容',
            'created at': datetime .now(),
        }
        rest = self.db.blog.posts.insert_one(post)
        return rest

    def get_one(self):
        '''查询一条数据'''
        return self.db.blog.posts.find_one()

    def get_more(self):
        '''查询多条数据'''
        return self.db.blog.posts.find()

    def get_from_old(self, oid):
        '''根据记录的ID来获取数据'''
        from bson.objectid import ObjectId
        return self.db.blog.posts.find_one({'_id': ObjectId(oid)})

    def update(self):
        '''修改数据'''
        # 修改一条数据 x 增加三，如果没有x设置为三
        rest = self.db.blog.posts.update_one({'title': '标题'}, {'$inc': {'x': 3}})
        print(rest.matched_count)
        print(rest.modified_count)

        # 修改多条数据
        rest = self.db.blog.posts.update_many({}, {'$inc': {'x': 1}})
        print(rest.matched_count)
        print(rest.modified_count)


    def delete(self):
        # 删除一条数据
        rest = self.db.blog.posts.delete_one({'title': '标题'})
        print(rest.deleted_count)

        # 删除多条数据
        rest = self.db.blog.posts.delete_many({'title': '标题'})
        print(rest.deleted_count)


def main():
    obj = TestMongo()
    #rest = obj.add_one()
    # rest = obj.get_more()
    # for item in rest:
    #     print(item['_id'])
    obj.delete()


if __name__=='__main__':
    main()