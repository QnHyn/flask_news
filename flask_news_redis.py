import sys
from datetime import datetime
from werkzeug import secure_filename
from flask import Flask, request, render_template, redirect, flash, url_for, abort
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

from forms import NewsForm_redis
from redis_news import RedisNews

app = Flask(__name__, template_folder='templates_redis')
app.config['SECRET_KEY'] = 'this is a redis key'
app.config['UPLOADED_PHOTOS_DEST'] = "/data/three_db_python/redis_version01/static/img/news"
query = RedisNews()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

patch_request_class(app)  # set maximum file size, default is 16MB


@app.route("/", methods=['GET'])
def index():
    ''' 获取新闻列表 '''
    news_list = query.get_all_news()
    return render_template("index.html", news_list=news_list)


@app.route("/cat/<name>/", methods=['GET'])
def cat(name):
    ''' 获取新闻列表 '''
    news_list = query.get_news_from_cat(name)
    return render_template("cat.html", news_list=news_list)


@app.route("/detail/<int:pk>/", methods=['GET'])
def detail(pk):
    ''' 获取新闻列表 '''
    news_obj = query.get_news_from_id(pk)
    return render_template("detail.html", obj=news_obj)


@app.route("/admin/", methods=['GET'])
@app.route("/admin/<int:page>/", methods=['GET'])
def admin(page=None):
    ''' 获取后台新闻列表 '''
    if page is None:
        page = 1
    page_data = query.paginate(page, 3)
    return render_template("admin/index.html", page_data=page_data)


@app.route("/admin/add/", methods=['GET', 'POST'])
def add():
    ''' 从后台页面添加新闻 '''
    form = NewsForm_redis()
    news_obj = {}
    # 提交增加
    if form.validate_on_submit():
        # 图片文件名
        #filename = photos.save(form.photo.data)

        news_obj['title'] = form.title.data
        news_obj['news_type'] = form.news_type.data
        news_obj['img_url'] = form.img_url.data
        news_obj['content'] = form.content.data
        news_obj['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        news_obj['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query.add_new_from_page(news_obj)
        flash('添加成功')
        return redirect(url_for('admin'))

    return render_template("admin/add.html", form=form)


@app.route("/admin/update/<int:pk>/", methods=['GET', 'POST'])
def update(pk):
    ''' 获取后台新闻列表 '''
    # 获取新闻
    news_obj = query.get_news_from_id(pk)
    if news_obj is None:
        abort('no this news')
    form = NewsForm_redis(data=news_obj)

    # 提交修改
    if form.validate_on_submit():
        news_obj['title'] = form.title.data
        news_obj['news_type'] = form.news_type.data
        #news_obj['img_url'] = form.img_url.data
        news_obj['content'] = form.content.data
        news_obj['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query.update_news(pk, news_obj)

        flash('新闻修改成功')
        return redirect(url_for('admin'))
    return render_template("admin/update.html", form=form)


@app.route("/admin/delete/<int:pk>/", methods=['GET', 'POST'])
def delete(pk):
    ''' 删除新闻 '''
    news_obj = query.get_news_from_id(pk)
    if news_obj:
        query.delete_news(pk, news_obj)
        return 'yes'

    return 'no'


if __name__ == "__main__":
    app.run(debug=True)