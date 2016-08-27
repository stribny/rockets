import os, sqlite3
from time import gmtime, strftime
from validate_email import validate_email
from flask import Flask, request
from flask import flash, g, render_template, redirect, url_for
app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(dict(
    DATABASE = os.path.join(app.instance_path, 'database.db'),
    SECRET_KEY='948-73q5fjiaifjdijlkejf'
))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_email', methods=['POST'])
def submit_email():
    if not validate_email(request.form['e_m_a_i_l']):
        flash('Please enter a valid e-mail address to sign up!')
        return redirect(url_for('index'))
    datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    db = get_db()
    db.execute('insert into submissions (date, note, email_address)'
        + ' values (?, ?, ?)',
        [datetime, request.form['note'], request.form['e_m_a_i_l']])
    db.commit()
    flash('Thank you for signing up!')
    return redirect(url_for('index'))

def connect_db():
    """Opens a new database connection."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Command to initialize the database."""
    init_db()
    print('Initialized the database.')

@app.teardown_appcontext
def close_db(error):
    """Closes the database at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
