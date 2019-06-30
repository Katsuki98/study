from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def introduce():
    info = {
        'Name': 'Nguyen Minh Son',
        'Age': 20,
        'Work': 'Student',
        'University': 'HUST',
        'GF': 'What is that?',
        'Hobby': 'Japan'
    }
    return render_template('index.html', info=info)

@app.route('/school')
def school():
    return redirect('http://techkids.vn', code=302)

if __name__ == '__main__':
    app.run(debug=True)
    
