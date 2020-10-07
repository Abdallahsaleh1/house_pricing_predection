from flask import Flask,render_template,request
import argparse
import csv
import pickle
import numpy as np
import sklearn


app = Flask(__name__)



def file_open():
    """
    function that will use the pickle to read model.sav
    """
    with open(path,'rb') as f:
        loaded_model=pickle.load(f)
    return loaded_model    


@app.route('/predict',methods=['GET','POST']) 
def prediction():
    """ 
    predict the house price that take the features and return the preicted price 
    """

    #if the method is post
    if(request.method=='POST'):
        #request the data from jsonfile       
        req_data = request.get_json()
        
        # accept the data coming from the jason file and store it in variables
        feature1 = float(req_data['feature1'])
        feature2 = float(req_data['feature2']) 
        feature3 = float(req_data['feature3'])
        feature4 = float(req_data['feature4'])
        feature5 = float(req_data['feature5'])
        feature6 = float(req_data['feature6'])

        ## store the features into array
        x = np.array([feature1,feature2,feature3,feature4,feature5,feature6]).reshape(1,6)
        # use the model to predict the price
        result = str(loaded_model.predict(x))
   
        # return the price
        return result
    
    #if method is GET
    else:
        #take the features from the url and store it
        feature1 = float(request.args.get('x1'))
        feature2 = float(request.args.get('x2')) 
        feature3 = float(request.args.get('x3'))
        feature4 = float(request.args.get('x4'))
        feature5 = float(request.args.get('x5'))
        feature6 = float(request.args.get('x6'))

        # store the features into array
        features = np.array([feature1,feature2,feature3,feature4,feature5,feature6],dtype=float).reshape(1,6)
        # use the model to predict the price
        result = str(loaded_model.predict(features))
        # return the price
        return result


if __name__ == '__main__':
    
    """
    take the model file path from the command line
    """
    #to use the argparse throughout ap
    ap = argparse.ArgumentParser()

    #use the ap variable to add the argument that will enter the path using it 
    ap.add_argument("-n",type=str)

    #take the argument that are inside ap and parse them inside the args
    args =ap.parse_args()

    #store the path through the arugment
    path = args.n
    loaded_model=file_open()
    app.run(debug=True)