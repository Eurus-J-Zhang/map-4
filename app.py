from flask import Flask,render_template,url_for,request, redirect, send_from_directory, session
from flask_migrate import Migrate
from forms import EmotionForm1
from forms import FeedbackForm
from forms import DemographicInfo
import os
import pymysql
from models import db, Data

pymysql.install_as_MySQLdb()

# Here is about configuration

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('JAWSDB_URL')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "iloveeurus"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

app = create_app()

def handle_form_submission(form, session_key, next_page):
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session[session_key] = data
        return redirect(next_page)
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DemographicInfo()
    if form.validate_on_submit():
        data = form.data
        data.pop('csrf_token', None)
        session['index_data'] = data
        session['counter'] = 0
        return redirect(url_for('p1'))
    return render_template('index.html',form=form)

@app.route('/p4', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        slot_choice = request.form.get('slotChoice')
        session['final_choice'] = slot_choice
        if slot_choice == 'B':
            return redirect(url_for('r_correct'))  # Redirect to the correct page
        elif slot_choice in ('A', 'C'):
            return redirect(url_for('r_wrong')) # Redirect to the wrong page
        else:
            return render_template('p4.html', error='Please select an option.') 
    return render_template('p4.html')


@app.route('/p_emo1', methods=['GET', 'POST'])
def emo1():
    final_choice = session.get('final_choice', None)
    content = {
    'B': {'image_path': 'static/img/ring.jpg'},
    'A_C': {'image_path': 'static/img/alarm.jpg'}
    }
    chosen_content = content['B'] if final_choice == 'B' else content['A_C']
    form = EmotionForm1()
    result = handle_form_submission(form, 'emo1_data', 'p_emo2')
    if result:
        return result
    return render_template('p_emo1.html',form=form,chosen_content=chosen_content)


@app.route('/p_emo2', methods=['GET', 'POST'])
def emo_end():
    form = FeedbackForm()
    result = handle_form_submission(form, 'emo_add_data', 'page_end')
    if result:
        index_data = session.get('index_data')
        final_choice = session.get('final_choice')
        emo1_data = session.get('emo1_data')
        emo_add_data = session.get('emo_add_data')
        
        combined_data = {**index_data, 'final_choice': final_choice, **emo1_data, **emo_add_data}
        data = Data(**combined_data)
        db.session.add(data)
        db.session.commit()

        return result
    return render_template('p_emo2.html',form=form)


# P1
@app.route('/p1')
def p1():
    return render_template('p1.html')

# P2
@app.route('/p2')
def p2():
    return render_template('p2.html')

# P3
@app.route('/p3')
def p3():
    return render_template('p3.html')

# P4
@app.route('/p4_office')
def p4_office():
    return render_template('p4_office.html')


# livingroomA
@app.route('/livingroomA')
def livingroomA():
    return render_template('livingroomA.html')


# livingroomB
@app.route('/livingroomB')
def livingroomB():
    return render_template('livingroomB.html')

# livingroomC
@app.route('/livingroomC')
def livingroomC():
    return render_template('livingroomC.html')

# livingroomD
@app.route('/livingroomD')
def livingroomD():
    return render_template('livingroomD.html')

# r_correct
@app.route('/r_correct')
def r_correct():
    return render_template('r_correct.html')

# r_wrong
@app.route('/r_wrong')
def r_wrong():
    return render_template('r_wrong.html')


# end page
@app.route('/page_end')
def page_end():
    return render_template('page_end.html')

if __name__ == "__main__":
    app.run(debug=True)