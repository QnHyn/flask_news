# -- coding: utf-8 --
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
"""
https://pypi.python.org/pypi/Flask-SQLAlchemy
http://flask-sqlalchemy.pocoo.org/2.1/
http://www.pythondoc.com/flask-sqlalchemy/config.html
http://docs.sqlalchemy.org/en/latest/core/type_basics.html#generic-types
"""


app = Flask(__name__)  # 构造出一个app对象

app.config['SQLALCHEMY_DATABASE_URI']  = 'mysql+pymysql://root:123456@127.0.0.1/flask_news?charset=utf8'
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
    news_list = News.query.all()
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


if __name__ == '__main__':
    app.run(debug=True)
    #  创建表 直接导入db对象
    #  from yourappliation import db
    #  db.create_all()