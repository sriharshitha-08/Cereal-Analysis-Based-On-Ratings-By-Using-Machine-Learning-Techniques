from flask import Flask, render_template, request
import requests

import json
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "hoXem41yNssuvlK5vYX6kbgaf0e1ukPpJZQeXxh9zAIA"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
app = Flask (name) 
import pickle
model = pickle.load(open('cerealanalysis.pkl','rb'))

@app.route('/')
def helloworld():
    return render_template('base.html')

@app.route('/assesment')
def prediction ():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def admin():
     a=request.form["mfr"]
     if (a == 'a'):
        a1, a2, a3, a4, a5, a6, a7=1,0,0,0,0,0,0
     if (a == 'g'):
        a1, a2, a3, a4, a5,a6,a7 = 0,1,0,0,0,0,0
     if (a == 'k'):
        a1, a2, a3, a4, a5, a6, a7=0,0,1,0,0,0,0
     if (a == 'n'):
        a1, a2, a3, a4, a5, a6, a7=0,0,0,1,0,0,0
     if (a == 'p'):
        a1, a2, a3, a4, a5, a6, a7=0,0,0,0,1,0,0
     if (a == 'q'):
        a1, a2, a3, a4, a5, a6, a7=0,0,0,0,0,1,0
     if (a == 'r'):
        a1, a2, a3, a4, a5, a6, a7=0,0,0,0,0,0,1
     b= request.form["type"]
     if (b=='c'):
          b=0
     if (b== 'h'):
          b=1
     c= request.form["Calories"]
     d= request.form["Protien"]
     e= request.form[ "Fat"]
     f= request.form["Sodium"]
     g= request.form[ "Fiber"]
     h= request.form["Carbo"]
     i= request.form["Sugars"]
     j= request.form["Potass"]
     k= request.form[ "Vitamins"]
     l= request.form[ "Shelf"]
     m= request.form["weight"]
     n= request.form["Cups"]

     t=[[int (a1), int(a2), int(a3), int(a4), int(a5), int(a6), int (a7), int (b), int(c), int(d), int(e), int(f) ,int(g), int(h),int(i),int(j),int(k),int(l),int(m),int(n)]]
     y = model.predict(t)
     return render_template("prediction.html", z = y[0][0])
      
 # NOTE: manually define and pass the array(s) of values to be scored in the next line
     payload_scoring = {"input_data": [{"field": [["mfr","type","G1","G2","G3","G4","G5","G6","calories","protein","fat","sodium","fiber","carbo","sugars","potass","vitamins","shelf","weight","cups"]], "values": t}]}

     response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d18d52cb-55ec-40df-9e62-b8de982c3585/predictions?version=2021-10-28', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
     print("Scoring response")
     predictions=response_scoring.json()
     print("Final Prediction:")
     #print(predictions['predictions'][0]['values'][0][0])
     print(predictions)
  
 
    
 
if name == "main":
    app.run(debug=False)
