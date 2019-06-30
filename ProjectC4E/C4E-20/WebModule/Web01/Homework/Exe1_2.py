from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi1/<int:weight>/<int:height>')
def bmi1(weight,height):
    BMI = weight/((height/100)**2)
    if BMI < 16:
        cond = 'Severely underweight'
    elif BMI < 18.5:
        cond = 'Underweight'
    elif BMI < 25:
        cond = 'Normal'
    elif BMI < 30:
        cond = 'Overweight'
    else: cond = 'Obese'
    return 'BMI: {:.2f}. You are {}.'.format(BMI,cond)

@app.route('/bmi2/<int:weight>/<int:height>')
def bmi2(weight,height):
    BMI = round(weight/((height/100)**2), 2)
    return render_template('bmi.html',BMI=BMI)

if __name__ == '__main__':
    app.run(debug=True)
    
