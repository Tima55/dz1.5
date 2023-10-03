from flask import Flask, redirect, request, render_template, flash, session, url_for

app = Flask(__name__)
app.secret_key= '12345fffff'

@app.route('/')
def index(): 
    if 'name' in session: 
        return f'Привет, {session["name"], session["email"]}' 
    else: 
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['name']: 
            flash('Введите имя!','danger') 
            return redirect(url_for('form'))
        session['name'] = request.form.get('name') or 'NoName'
        session['email'] = request.form.get('email') or 'No email'
        flash ('Вы вошли!','success')
        return redirect(url_for('main'))
    return render_template('form.html')

@app.route('/main/', methods=['GET', 'POST'])
def main(): 
    if 'name' in session:
        context = {
            'name': session['name'],
            'email': session['email'],
        }
        return render_template('main.html', **context)
    else: 
        return redirect(url_for('login'))

@app.route('/logout/', methods=['POST'])
def logout(): 
    session.pop('name', None) 
    return redirect(url_for('index'))
