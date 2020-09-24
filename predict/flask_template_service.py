from flask import Flask,render_template,request
import csv
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('design.html')


@app.route('/predict',methods=['GET','POST']) 
def prediction():
    if(request.method=='POST'):
        with open('file.csv','r') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=','))

        thetas=reader[0]
        theta0=float(reader[1][0])
        float_thetas=[]

        for i in range (6):
            float_thetas.append(float(thetas[i]))
            
        features=[]
        for i in range(1,7):
            count=str(i)
            features.append(float(request.form['features'+count]))
        
   
        solution=str(theta0+(features[0]*float_thetas[0])+(features[1]*float_thetas[1])+(features[2]*float_thetas[2])+(features[3]*float_thetas[3])+(features[4]*float_thetas[4])+(features[5]*float_thetas[5]))
        return solution

if __name__ == '__main__':
    app.run(debug=True)
