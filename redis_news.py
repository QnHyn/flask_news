import math
import redis

NEWS_FIELDS = (
    "title",
    "img_url",
    "content",
    "is_valid",
    "news_type",
    "created_at",
    "updated_at"
)


class RedisNews(object):
    def __init__(self):
        # 如果返回是二进制类似 b'3\xe6\x9c\x885\xe6\x97\xa5\xe...'需要加decode_responses=True
        try:
            self.r = redis.StrictRedis(host='localhost',
                                       port=6379, encoding='utf-8',
                                       decode_responses=True,
                                       db=1)
        except Exception as e:
            print('redis connect faild')

    def _news_id(self, int_id):
        ''' 新闻id '''
        return 'news:%d' % int(int_id)

    def _news_type(self, news_type):
        ''' 新闻类型 '''
        return 'news_type:%s' % news_type

    def _news_list_name(self):
        ''' 新闻列表名称 '''
        return 'news'

    def add_new_from_page(self, news_obj):
        ''' 从页面新增新闻数据 '''

        # 记录news_id的数字自增1
        int_id = self.r.incr('news_id', amount=1)
        # 获取新闻id
        news_id = self._news_id(int_id)

        # 新闻列表中添加
        self.r.lpush(self._news_list_name(), int_id)

        # 新闻类型中添加信息
        news_type = news_obj['news_type']
        self.r.sadd(news_type, int_id)

        # 新闻内容中添加信息
        self.r.hmset(news_id, news_obj)

    def add_news(self, news_obj):
        ''' 新增新闻数据 '''
        # 获取到新闻的id
        int_id = int(self.r.incr('news_id'))
        # 　拼接新闻数据Hash key(news:2)
        news_id = self._news_id(int_id)

        # 存储新闻数据(hash)
        rest = self.r.hmset(news_id, news_obj)

        # 存储新闻的id list
        self.r.lpush(self._news_list_name(), int(int_id))

        # 存储新闻的类别-新闻id(set)
        news_type = self._news_type(news_obj['news_type'])
        self.r.sadd(news_type, int_id)
        return rest

    def add_news_with_transaction(self, news_obj):
        ''' 使用事务来新增新闻数据 '''
        pipe = self.r.pipeline(transaction=True)
        int_id = self.r.incr('news_id')
        news_id = self._news_id(int_id)

        # 使用列表list获取新闻的id
        pipe.lpush(self._news_list_name(), int_id)

        # 使用hash来保存新闻具体内容
        pipe.hmset(news_id, news_obj)

        # 使用hash来保存新闻分类信息
        news_type = self._news_type(news_obj['news_type'])
        pipe.sadd(news_type, int_id)

        rest = pipe.execute()
        return rest

    def get_all_news(self):
        ''' 获取所有新闻信息 '''

        # 获取id列表
        id_list = self.r.lrange(self._news_list_name(), 0, -1)
        data_list = []

        for int_id in id_list:
            # 获取具体新闻内容
            news_id = self._news_id(int_id)
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            # print(data)
            data_list.append(data)

        return data_list

    def get_news_from_id(self, news_id):
        ''' 根据新闻id获取新闻内容 '''
        news_id = self._news_id(news_id)

        # 根据新闻id获取新闻内容
        news_obj = self.r.hgetall(news_id)
        return news_obj

    def get_news_from_cat(self, cat_name):
        ''' 根据新闻类型获取新闻内容 '''
        news_list = []

        # 获取新闻类型
        news_type = self._news_type(cat_name)
        # print(news_type)
        # 获取新闻类型集合中新闻id的列表
        id_list = self.r.smembers(news_type)
        print(id_list)
        for int_id in id_list:
            # 获取新闻id
            news_id = self._news_id(int_id)
            # 根据新闻id获取新闻内容
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            news_list.append(data)
        return news_list

    def update_news(self, pk, news_obj):
        ''' 新闻的修改 '''
        news_id = self._news_id(pk)

        # 修改新闻
        rest = self.r.hmset(news_id, news_obj)
        return rest

    def delete_news(self, pk, news_obj):
        '''
            新闻的删除，物理删除

            关于常用的方法可以通过查询redis的命令类型判断是list,string还是hash或者set
            1.命令列表定位到具体命令：http://www.redis.cn/commands.html#hash
            2.找到命令后，查询api的用法http://redis-py.readthedocs.io/en/latest/

        '''

        # 获取新闻id
        news_id = self._news_id(pk)
        # 从新闻列表中删除新闻id
        self.r.lrem(self._news_list_name(), 0, pk)
        # 从新闻的类型set集合中清理新闻id
        news_type = self._news_type(news_obj['news_type'])
        self.r.srem(news_type, pk)
        # 从新闻的内容hash列表中清理具体的新闻内容NEWS_FIELDS(具体的列信息)
        self.r.hdel(news_id, *NEWS_FIELDS)

    def paginate(self, page=1, per_page=5):
        ''' 新闻后台分页 '''
        if page is None:
            page = 1

        data_list = []
        # 开始页，结束页面
        start = (page - 1) * per_page
        end = page * per_page - 1

        # 获取所有新闻列表(计算页码使用)
        list_ids = self.r.lrange(self._news_list_name(), 0, -1)

        # 获取新闻列表
        id_list = self.r.lrange(self._news_list_name(), start, end)
        # print('id_list%s' % id_list)

        for int_id in id_list:
            news_id = self._news_id(int_id)
            # 根据新闻id获取新闻内容
            data = self.r.hgetall(news_id)
            data['id'] = int_id
            data_list.append(data)
        # print('data_list%s' % data_list)
        return Pagenation(data_list, page, per_page, list_ids)

    def init_news(self, data_list):
        ''' 批量导入新闻数据 '''
        for news_obj in data_list:
            rest = self.add_news_with_transaction(news_obj)
            print(rest)


class Pagenation(object):
    ''' 分页类 '''

    def __init__(self, data_list, now_page, per_page, list_ids):
        self.now_page = now_page
        self.data_list = data_list
        self.per_page = per_page
        self.list_ids = list_ids

    @property
    def page(self):
        ''' 当前页 '''
        return self.now_page

    @property
    def items(self):
        ''' 返回页面数据 '''
        return self.data_list

    @property
    def prev_num(self):
        ''' 上一页 '''
        return self.now_page - 1

    @property
    def next_num(self):
        ''' 下一页页码 '''
        return self.now_page + 1

    @property
    def has_prev(self):
        ''' 是否有上一页 '''
        return self.now_page > 1

    @property
    def has_next(self):
        ''' 是否有下一页 '''
        return self.per_page == len(self.data_list)

    def iter_pages(self):
        ''' 页码 '''
        # 获取所有的id长度(即新闻条数)除以每页显示的页面，得到取进一位的整数
        total_page = math.ceil(len(self.list_ids) / self.per_page) + 1
        # print('total_page=%d' % total_page)
        return range(1, total_page)

