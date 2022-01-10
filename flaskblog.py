from flask import Flask, render_template, url_for
from forms import LoginForm, RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c8783a81399a0f7a938e47b79126d3d8'

posts = [
    {
        'author': 'Huong',
        'title': 'Post 1',
        'content': 'First content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Oanh',
        'title': 'Post 2',
        'content': 'Second content',
        'date_posted': 'April 21, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
if __name__ == '__main__':
    app.run(debug=True)

