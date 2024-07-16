from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField, SubmitField
from wtforms.fields.numeric import IntegerField


class JobsForm(FlaskForm):
    job = StringField("Содержание")
    work_size = IntegerField("Объем работы в часах")
    collaborations = StringField("Коллабораторы")
    is_finished = BooleanField("Завершено")
    submit = SubmitField('Применить')
