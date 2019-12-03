import redis


class Base(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)


class StringTest(object):
    def __init__(self):
        # redis.Redis()兼容老版本，redis.StrictRedis()不考虑兼容性
        # self.r = redis.Redis(host='localhost', port=6379, db=0)
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    def test_set(self):
        ''' set -- 设置值 '''
        rest = self.r.set('user2', 'amy')
        print(rest)
        return rest

    def test_get(self):
        '''get -- 获取值'''
        rest = self.r.get('user2')
        print(rest)
        return rest

    def test_mset(self):
        ''' mset -- 设置多个键值对 '''
        d = {
            'user3': 'Bob',
            'user4': 'Bobx'
        }
        rest = self.r.mset(d)
        print(rest)
        return rest

    def test_mget(self):
        ''' mset -- 设置多个键值对 '''
        d = ['user3','user4']
        rest = self.r.mget(d)
        print(rest)
        return rest

    def test_del(self):
        ''' del删除键值 '''
        rest = self.r.delete('user3')
        print(rest)

    def test_push(self):
        ''' lpush/rpush -- 从左/右插入数据 '''
        t = ['Amy', 'Jhon']
        # 如果不加*则会把两个元素当做整体存入
        rest = self.r.lpush('l_eat3', *t)
        print(rest)
        rest = self.r.lrange('l_eat3', 0, -1)
        print(rest)

    def test_pop(self):
        ''' lpop/rpop 移除最左/右边的元素并返回值'''
        rest = self.r.lpop('l_eat3')
        print(rest)
        rest = self.r.lrange('l_eat3', 0, -1)
        print(rest)

class SetTest(Base):
    def test_sadd(self):
        ''' sadd --添加元素 '''
        l = ['cat', 'dog', 'monkey']
        # rest = self.r.sadd('zoo2', l)
        rest = self.r.sadd('zoo2', *l)
        print(rest)
        rest = self.r.smembers('zoo2')
        print(rest)

    def test_srem(self):
        ''' srem -- 删除元素 '''
        rest = self.r.srem('zoo2', 'monkey')
        print(rest)
        rest = self.r.smembers('zoo2')
        print(rest)

    def test_sinter(self):
        ''' sinter --返回元素的交集 '''
        rest = self.r.sinter('zoo2', 'zoo1')
        print(rest)

class HashTest(Base):
    def hset_test(self):
        ''' hset设置新闻内容
        self.r.hset(1,'title','朝鲜特种部队视频公布展示士兵身体素质与意志')
        self.r.hset(1,'content','content01')
        self.r.hset(1,'img_url','/static/img/news/01.png')
        self.r.hset(1,'is_valid','true')
        self.r.hset(1,'news_type','推荐')

        self.r.hset(2,'title','男子长得像\"祁同伟\"挨打 打人者:为何加害检察官')
        self.r.hset(2,'content','因与热门电视剧中人物长相相近,男子竟然招来一顿拳打脚踢。4月19日,打人男子周某被抓获。半个月前,酒后的周某看到KTV里有一名男子很像电视剧中的反派。二话不说,周某冲上去就问你为什么要加害检察官?男子莫名其妙,回了一句神经病。周某一听气不打一处来,对着男子就是一顿拳打脚踢,嘴里面还念叨着,“叫你加害检察官,我打死你!”随后,周某趁机逃走。受伤男子立即报警,周某被上海警方上网通缉')
        self.r.hset(2,'img_url','/static/img/news/02.png')
        self.r.hset(2,'is_valid','true')
        self.r.hset(2,'news_type','百家')

        '''

        ''' mset/mget -- 设置/获取散列值'''
        rest = self.r.hset('stu:002','name','tom')
        print(rest)
        rest = self.r.hexists('stu:002','name')
        print(rest)
        rest = self.r.hget('stu:002', 'name')
        print(rest)

    def mset_test(self):
        ''' 获取新闻的数据 '''
        # rest = self.r.hget(1,'title')
        # print(rest.decode('utf-8'))
        # rest = self.r.hget(1, 'news_type')
        # print(rest.decode('utf-8'))

        # rest = self.r.hget(3,'title')
        # print(rest.decode('utf-8'))
        # rest = self.r.hget(3, 'news_type')
        # print(rest.decode('utf-8'))

        # mset和hkeys
        m = {
            'name':'lily',
            'age':18,
            'grade':90
        }
        rest = self.r.hmset('stu:003', m)
        print(rest)
        rest = self.r.hkeys('stu:003')
        print(rest)
        rest = self.r.hvals('stu:003')
        print(rest)

    def test_hgetall(self):
        data = self.r.hgetall('news:3')
        print(data['title'].decode('utf-8'))
        print(data['content'].decode('utf-8'))


def main():
    # st = StringTest()
    # st.test_set()
    # st.test_get()
    # st.test_mset()
    # st.test_mget()
    # st.test_del()
    # st.test_push()
    # st.test_pop()

    # set_test = SetTest()
    # set_test.test_sadd()
    # set_test.test_srem()
    # set_test.test_sinter()

    ht = HashTest()
    # ht.mset_test()
    # ht.hset_test()
    # ht.hget_test()
    ht.test_hgetall()

if __name__ == "__main__":
    main()