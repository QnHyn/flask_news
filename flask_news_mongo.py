# coding:utf-8
from flask import Flask, render_template, redirect, flash, url_for
from datetime import datetime
from flask_mongoengine import MongoEngine
from mongoengine import *
from forms import NewsForm_mongo

app = Flask(__name__, template_folder='templates_mongo')
app.config['MONGODB_SETTINGS'] = {
    'db': 'mongo_news',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)

app.config['SECRET_KEY'] = 'this is a mongodb key'

# 新闻类型
NEWS_TYPES = (
    ('推荐', '推荐'),
    ('百家', '百家'),
    ('本地', '本地'),
    ('图片', '图片')
)


class News(db.Document):
    ''' 新闻 '''
    title = db.StringField(required=True, max_lenght=64)
    content = db.StringField(required=True)
    news_type = db.StringField(required=True, choices=NEWS_TYPES)
    img_url = db.StringField()
    is_valid = db.BooleanField(default=True)
    created_at = db.DateTimeField(default=datetime.now())
    updated_at = db.DateTimeField(default=datetime.now())

    # def clean(self):
    #     if '黄' in self.title:
    #         raise db.ValidationError("不能有黄字")

    meta = {
        'collection': 'news',
        'ordering': ['-created_at']
    }


@app.route('/', methods=['get'])
def index():
    ''' 首页 '''
    # return 'ok'
    news_list = News.objects.filter(is_valid=True).all()
    print(news_list)
    return render_template('index.html', news_list=news_list)


@app.route('/cat/<name>/', methods=['GET', 'POST'])
def cat(name):
    ''' 栏目 '''
    news_list = News.objects.filter(is_valid=True, news_type=name).all()
    return render_template('cat.html', news_list=news_list)


@app.route('/detail/<pk>/', methods=['GET', 'POST'])
def detail(pk):
    ''' 新闻详情页 '''
    # 如果新闻不存在则报404错误
    obj = News.objects.filter(pk=pk).first_or_404()
    return render_template('detail.html', obj=obj)


@app.route('/admin/', methods=['GET', 'POST'])
@app.route('/admin/<page>/', methods=['GET', 'POST'])
def admin(page=None):
    ''' 后台首页 '''
    # 如果page参数没有传就默认显示首页
    if page == None:
        page = 1
    page_data = News.objects.paginate(page=int(page), per_page=5)
    return render_template('admin/index.html', page_data=page_data, page=int(page))


@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    ''' 添加新闻 '''
    form = NewsForm_mongo()
    if form.validate_on_submit:
        # 获取数据
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            news_type=form.news_type.data,
            img_url=form.img_url.data
        )
        new_obj.save()
        flash('新闻添加成功')
        return redirect(url_for('admin'))
    return render_template('admin/add.html', form=form)


@app.route('/admin/delete/<pk>/', methods=['GET', 'POST'])
def delete(pk):
    ''' 删除新闻 '''
    new_obj = News.objects.filter(pk=pk).first()
    print(new_obj.title)
    if not new_obj:
        return 'no'
    # 逻辑删除
    new_obj.is_valid = False
    new_obj.save()
    return 'yes'

    # 物理删除
    # new_obj.delete()
    # return 'yes'


@app.route('/admin/update/<pk>/', methods=['POST', 'GET'])
def update(pk):
    ''' 修改新闻 '''
    new_obj = News.objects.get_or_404(pk=pk)
    print(new_obj.title)
    form = NewsForm_mongo(obj=new_obj)
    if form.validate_on_submit():
        new_obj.title = form.title.data
        new_obj.content = form.content.data
        new_obj.news_type = form.news_type.data
        new_obj.img_url = form.img_url.data

        new_obj.save()
        flash('新闻修改成功')
        return redirect(url_for('admin'))
    return render_template('admin/update.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)