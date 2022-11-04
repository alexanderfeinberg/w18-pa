from flask import Flask, render_template, redirect, request
from .config import Configuration
from .models import db, SimplePerson
from .forms import SimpleForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

def enter_into_db(entry, redirect_path=None):
    db.session.add(entry)
    db.session.commit()
    return redirect(redirect_path) if redirect_path else None




@app.route('/', methods=['GET','POST'])
def index():
    return '<h1>Practice Assessment</h1>'

@app.route('/simple-form', methods=['GET'])
def simple_form():
    form = SimpleForm()
    return render_template('simple_form.html', form=form)

@app.route('/simple-form', methods=['POST'])
def simple_form_post():
    form = SimpleForm()
    if form.validate_on_submit():
        new_entry = form.data
        print("FORM DATA ",form.data)
        entry = SimplePerson(**{'name':form.data['name'], 'age':form.data['age'], 'bio':form.data['bio']})

        return enter_into_db(entry, '/')
    return 'Bad Data'


@app.route('/simple-form-data')
def simple_form_data():
    person_query = db.session.query(SimplePerson).filter(SimplePerson.name.ilike('M%'))
    records = person_query.all()

    return render_template('simple_form_data.html', records=records)
