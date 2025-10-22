from flask import Flask, render_template, request, session, flash, redirect,url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

USERNAME = 'admin'
PASSWORD = '1234'

@app.route('/')
def home():
    # Quando for criado um login, cria-se um valor, gerando uma chave-valor
    # sessões ficam no cookies
    if "username" in session:
        return render_template('home.html', username=session['username'])

    return redirect(url_for('login'))

#
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('home'))
        else:
            flash("Credenciais inválidas!", 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout realizado com sucesso!', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)