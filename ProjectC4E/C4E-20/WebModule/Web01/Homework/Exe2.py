from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = {
        'Son':
        {
            'name': 'Son',
            'gender': 'Male',
            'age': 20,
            'hobby': 'Japan'
        },
        'Quang':
        {
            'name': 'Quang',
            'gender': 'Male',
            'age': 20,
            'hobby': 'Japan'
        }
    }
    if username in users:
        return render_template('user.html', username = users[username])
    else:
        return 'User not found'

if __name__ == '__main__':
  app.run(debug=True)