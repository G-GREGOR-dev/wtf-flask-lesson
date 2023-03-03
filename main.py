from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username_astr = StringField('id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username_cap = StringField('id капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/')
@app.route('/index/<title>')
def index(title='default'):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/list_prof/<list>')
def prof(list):
    list_prof = ['инженер-исследователь', 'пилот', 'строитель',
                 'экзобиолог', 'врач', 'инженер по терраформированию',
                 'климатолог', 'специалист по радиационной защите',
                 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
                 'метеоролог', 'оператор марсохода', 'киберинженер',
                 'штурман', 'пилот дронов']
    return render_template('prof.html', list=list, proff=list_prof)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    jon = {'surname': 'Wanty', 'name': 'Mark', 'education': 'выше среднего',
           'profession': 'штурман марсахода', 'sex': 'male',
           'motivation': 'Всегда мечтал застрять на Марсе!', 'ready': True}
    return render_template('auto_answer.html', surname=jon['surname'], name=jon['name'], education=jon['education'],
                           profession=jon['profession'], sex=jon['sex'], motivation=jon['motivation'], ready=jon['ready'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
