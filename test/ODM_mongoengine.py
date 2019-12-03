from mongoengine import connect, Document, EmbeddedDocument, DynamicDocument, StringField, IntField, \
    FloatField, ListField, EmbeddedDocumentField

connect('students')

SEX_CHICES = (
    ('male', '男'),
    ('female', '女')
)


class Grade(EmbeddedDocument):
    ''' 学生的成绩 '''
    name = StringField(required=True)
    score = FloatField(required=True)

# 如果我们想增加一些students没有的字段，可以用DynamicDocument。
# 使用Document如果字段没有定义, 就不能增删改查。可以用DynamicDocument改进
# class Student(Document):
class Student(DynamicDocument):
    '''学生'''
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHICES, required=True)
    grade = FloatField()
    address = StringField()
    # 很多科目的成绩 嵌套的文档
    grades = ListField(EmbeddedDocumentField(Grade))

    meta = {
        # 指定添加到students集合,不设置的话默认为student集合
        'collection': 'students',
        # 排序功能，按照分数倒序
        'ordering': ['-grade']
    }


class TestMongoEngine(object):
    def add_one(self):
        '''添加一条数据到数据库'''
        yuwen = Grade(
            name='语文',
            score=90)
        shuxue = Grade(
            name='数学',
            score=100)
        stu_obj = Student(
            name='张三丰',
            age=15,
            grades=[yuwen, shuxue],
            sex='male'
        )
        # 直接添加remark字段是无法添加成功的，需要引入动态添加字段的方法DynamicDocument

        stu_obj.remark = 'remark'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        ''' 获取单条数据 '''
        return Student.objects.first()

    def get_more(self):
        ''' 获取多条数据 '''
        # return Student.objects
        return Student.objects.all()

    def get_one_from_oid(self, oid):
        ''' 查询指定id的数据 '''
        return Student.objects.filter(id=oid).first()


    def update(self):
        ''' 修改数据 '''
        # 修改一条数据
        # res = Student.objects.filter(sex='male').update_one(inc__age=1)
        # return res

        # 修改多条数据
        res = Student.objects.filter(sex='male').update(inc__age=10)
        return res


    def delete(self):
        ''' 删除数据 '''
        # 删除一条数据
        # res = Student.objects.filter(sex='male').first().delete()
        # return res

        # 删除多条数据
        res = Student.objects.filter(gender='male').delete()


def main():
    en = TestMongoEngine()
    # en.add_one()

    # res = en.get_one()
    # print(res.name)

    # rows = en.get_more()
    # for row in rows:
    #     print(row.name)

    # res = en.get_one_from_oid('5a9df2e48a86b467d4a2c44f')
    # print(res.name)

    # res = en.update()
    # print(res)

    res = en.delete()
    print(res)


if __name__ == "__main__":
    main()


# db.students.insertMany(
# [
#     {name: "bob", age:16, gender:"male", grade:95},
#     {name: "ana", age:18, gender:"female", grade:45},
#     {name: "xi", age:15, gender:"male", grade:75},
#     {name: "bob1", age:16, gender:"male", grade:95},
#     {name: "ana1", age:18, gender:"female", grade:45},
#     {name: "jack", age:18, gender:"male", grade:85},
#     {name: "tom", age:19, gender:"male", grade:65},
#     {name: "lily", age:16, gender:"female", grade:59},
#     {name: "lucy", age:18, gender:"female", grade:68},
#     {name: "lilei", age:18, gender:"female", grade:68},
#     {name: "hanmeimei", age:16, gender:"female", grade:90},
#     {name: "harry", age:16, gender:"male", grade:81},
#     {name: "json", age:16, gender:"male", grade:75},
#     {name: "jim", age:16, gender:"male", grade:36},
#     {name: "rose", age:16, gender:"female", grade:91},
#     {name: "moli", age:16, gender:"female", grade:93},
#     {name: "linda", age:16, gender:"female", grade:96}
# ]
# )
