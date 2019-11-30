# -- coding: utf-8 --
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import NewsForm
from datetime import datetime
"""
https://pypi.python.org/pypi/Flask-SQLAlchemy
http://flask-sqlalchemy.pocoo.org/2.1/
http://www.pythondoc.com/flask-sqlalchemy/config.html
http://docs.sqlalchemy.org/en/latest/core/type_basics.html#generic-types
"""


app = Flask(__name__)  # 构造出一个app对象

app.config['SQLALCHEMY_DATABASE_URI']  = 'mysql+pymysql://root:123456@127.0.0.1/flask_news?charset=utf8'
app.config['SECRET_KEY'] = 'this is a random key string'
db = SQLAlchemy(app)


class News(db.Model):
    """ 新闻模型 """
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    types = db.Column(db.Enum('推荐', '百家', '本地', '图片'))
    image = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(20))
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean, default=True)

    # print class对象的时候返回的是数据（新闻标题）、而不是地址。
    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    '''新闻首页'''
    news_list = News.query.filter_by(is_valid=1)
    return render_template('index.html', news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    '''新闻的类别'''
    news_list = News.query.filter(News.types == name)
    return render_template('index.html',name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ 新闻详情页 """
    new_obj = News.query.get(pk)
    return render_template('detail.html', new_obj=new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 新闻管理首页 """
    if page is None:
        page = 1
    page_data = News.query.paginate(page=page, per_page=3)
    return render_template('admin/index.html', page_data=page_data)


@app.route('/admin/add/', methods=('GET', 'POST'))
def add():
    form = NewsForm()
    if form.validate_on_submit():
        # 获取数据
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            image=form.image.data,
            types=form.types.data,
            created_at=datetime.now(),
        )
        # 保存数据
        db.session.add(new_obj)
        db.session.commit()
        flash("新增成功")
        return redirect(url_for('admin'))
    return render_template("admin/add.html", form=form)


@app.route('/update/<int:pk>/')
def update():
    """ 新闻管理首页 """
    new_list = News.query.all()
    return render_template('admin/index.html', new_list=new_list)


@app.route('/delete/<int:pk>/')
def delete():
    """ 新闻管理首页 """
    new_list = News.query.all()
    return render_template('admin/index.html', new_list=new_list)


if __name__ == '__main__':
    app.run(debug=True)
    #  创建表 直接导入db对象
    #  from yourappliation import db
    #  db.create_all()