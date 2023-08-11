import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__) # Starting point of flask to run
regmodel=pickle.load(open('regmodel.pkl','rb'))  #Load the model
scalar=pickle.load(open('scaling.pkl','rb'))  #Load the model

@app.route('/')
def home():
    return render_template('price.html') 

@app.route('/predict_api',methods=['POST']) # we are using api called predict. Post requires here will capture the input to the model and our model will give the output
def predict_api():
    data=request.json['data'] # Data is a key, input is in the form of json format
    print(data)

    '''
    basically data in json file in key-value pair.
    If we print data.values we will get dictionary values.
    But this will not be sufficient, we have to first convert this into list
    So I will be getting a single list
    then after this we have reshape the list using np.array with (1,-1) because this is a single data point record
    now we have to take this and do the transformation other wise this transformation whate ever standardization we are using
    is always expecting a single record with so many no.of features based on the data set.
    Now we need to pass this to scaling.pkl
    '''
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform((np.array(list(data.values())).reshape(1,-1)))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

# Creating Web application:

@app.route('/predict',methods=['POST']) # to create web application. We will create a html form with all features
def predict():
    data=[float(x) for x in request.form.values()] # request object to get the values from the form
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("price.html",prediction_text="The house price prediction is {}".format(output))


if __name__=="__main__":
    app.run(debug=True)

    '''
    Here the code is ready, next we need to download and install postman to run the code
    '''