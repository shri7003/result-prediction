from flask import Flask,request,render_template
import numpy as np
import pickle

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data',methods = ['POST'])
def data():
    data = request.form
    print(data)
    total_marks = int(data['total_marks'])
    percentage = float(data['percentage'])
    cgpa = float(data['cgpa'])
    array = np.array([[total_marks,percentage,cgpa]])
    print(array)
    with open('model.pkl','rb') as file:
        model = pickle.load(file)
    result = model.predict(array)
    print(result)
    if result[0]==0:
        result ="Fail"
        print("Fail")

    if result[0]>=0 and result[0]<=1:
        result ="Pass"
        print('Pass')

    if result[0]>=1 and result[0]<=2:
        result = "First Class"
        print('First Class')

    if result[0]>=2 and result[0]<=3:
        result ="Pass with Distinction"
        print('Pass with Distinction')

    return render_template('index.html',result = result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port =8080)