from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


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
