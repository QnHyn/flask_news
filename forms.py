from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class NewsForm_mysql(FlaskForm):
    """ 新闻表单 """
    title = StringField(label='新闻标题', validators=[DataRequired("请输入标题")],
        description="请输入标题",
        render_kw={"required": "required", "class": "form-control"})
    content = TextAreaField(label='新闻内容', validators=[DataRequired("请输入内容")],
        description="请输入内容",
        render_kw={"required": "required", "class": "form-control"})
    types = SelectField('新闻类型',
        choices=[('推荐', '推荐'), ('百家', '百家'), ('本地', '本地'), ('图片', '图片')],
        render_kw={'class': 'form-control'})
    image = StringField(label='新闻图片',
        description='请输入图片地址',
        render_kw={'class': 'form-control'})
    submit = SubmitField('提交')


class NewsForm_mongo(FlaskForm):
    """ 新闻表单 """
    title = StringField(label='新闻标题', validators=[DataRequired("请输入标题")],
        description="请输入标题",
        render_kw={"required": "required", "class": "form-control"})
    content = TextAreaField(label='新闻内容', validators=[DataRequired("请输入内容")],
        description="请输入内容",
        render_kw={"required": "required", "class": "form-control"})
    news_type = SelectField('新闻类型',
        choices=[('推荐', '推荐'), ('百家', '百家'), ('本地', '本地'), ('图片', '图片')],
        render_kw={'class': 'form-control'})
    img_url = StringField(label='新闻图片',
        description='请输入图片地址',
        render_kw={'class': 'form-control'})
    submit = SubmitField('提交')


class NewsForm_redis(FlaskForm):
    """新闻表单数据验证"""
    title = StringField(label = '新闻标题', validators = [DataRequired('请输入标题')],
        description = '请输入标题',
        render_kw={'required':'required', 'class':'form-control'})
    content = TextAreaField(label = '新闻内容', validators = [DataRequired('请输入新闻内容')],
        description = '请输入新闻内容',
        render_kw={'required':'required', 'class':'form-control'})
    news_type = SelectField('新闻类型', choices = [('推荐','推荐'), ('百家', '百家'),('本地','本地'), ('图片','图片')])
    img_url = StringField(label='新闻图片', description='请输入图片地址',
        render_kw={'class':'form-control'})
    # photo = FileField('图片上传', validators=[FileAllowed(['png', 'JPEG', 'jpg'], '只能上传图片！'),
    #     FileRequired('文件未选择！')])
    submit = SubmitField('提交')