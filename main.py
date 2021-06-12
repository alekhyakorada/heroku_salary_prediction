from flask import Flask,render_template,request 
import joblib
app=Flask(__name__)

model=joblib.load('hiring_model.pkl')

@app.route("/" )

def welcome():
    return render_template('form.html')
@app.route('/predict' , methods = ['POST'])
def predict():

    exp = request.form.get('experience')
    score = request.form.get('test_score')
    interview_score = request.form.get('interview_score')

    prediction = model.predict([[int(exp) , int(score) , int(interview_score)]])

    output = round(prediction[0] , 2)

    return render_template('form.html' , prediction_text = f"Employee Salary will be $ {output}")

@ app.route('/contacts')
def contacts():
    return 'Welcome to Contacts page'
@ app.route('/feedback')
def feedback():
    return 'Welcome to feedback page'

if __name__=="__main__":
    app.run(debug=True)