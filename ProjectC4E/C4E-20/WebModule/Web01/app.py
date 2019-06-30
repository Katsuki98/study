from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            'title': 'Death or Survive',
            'content': 'Sword Art Online',
            'author': 'Kayaba Akihiko',
            'author_sex': 1
        },
        {
            'title': 'Ecchi 18+',
            'content': 'To love RU',
            'author': 'Hasemi Saki to Yabuki Kentaro',
            'author_sex': 2
        }
    ]
    return render_template('index.html', posts=posts)

@app.route('/hello')
def say_hello():
    return 'Starburst Stream'

@app.route('/say_hi/<name>/<age>')
def hi(name,age):
    return "Hi {}, you're {} years old".format(name,age)

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1,num2):
    return str(num1 + num2)

if __name__ == '__main__':
  app.run(debug=True)

 