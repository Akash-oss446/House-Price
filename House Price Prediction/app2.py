# from flask import Flask, render_template, request
import json
from flask import Flask ,request,render_template
import pickle
import numpy as np
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
@app.route('/',methods=['POST'])
def Home():
    return render_template('index.html')
with open("columns.json", "r") as f:
   __data_columns = json.load(f)['data_columns']

app=Flask(__name__)
model=pickle.load(open('model (1).pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")
@app.route("/predict", methods=['POST',['GET']])
def predict():
    if request.method == 'POST':
        area = int(request.form['area'])
        bathrooms = int(request.form['bathrooms'])
        bedrooms = int(request.form['bedrooms'])
        stories = int(request.form['stories'])
        parking = int(request.form['parking'])
        main_road = request.form['mainroad']
        basement = request.form['basement']
        guestroom = request.form['guest_room']
        hotwaterheating = request.form['hotwaterheating']
        airconditioning = request.form['airconditioning']
        prefarea = request.form['prefarea']
        furnishingstatus = request.form['furnishingstatus']
        
        if main_road == 'Yes':
            mainroad_no=0
            mainroad_yes=1
        else:
            mainroad_no=1
            mainroad_yes=0
            
        if guestroom == 'No':
            guestroom_no=1
            guestroom_yes=0
        else:
            guestroom_no=0
            guestroom_yes=1

        fr = furnishingstatus
        dp = np.zeros(3)
        if fr == 'furnished':
            dp[1] = 1
        elif fr == 'semifurnished':
            dp[2] = 1
        elif fr == 'unfurnished':
            dp[3] = 1
        else:
            dp[0] = 1
        if basement == 'No':
            basement_no=1
            basement_yes=0
        else:
            basement_no=0
            basement_yes=1
        if hotwaterheating == 'No':
            hotwaterheating_no=1
            hotwaterheating_yes=0
        else:
            hotwaterheating_no=0
            hotwaterheating_yes=1
        if airconditioning=='No':
            airconditioning_no=1
            airconditioning_yes=0
        else:
            airconditioning_no=0
            airconditioning_yes=1
        if prefarea=='No':
           prefarea_no=1
           prefarea_yes=0
        else:
           prefarea_yes=1
           prefarea_no=0
        x = np.zeros(len(__data_columns))

        x[0] = area
        x[1] = bedrooms
        x[2] = bathrooms
        x[3] = stories
        x[4] = parking
        x[5] = mainroad_no
        x[6] = mainroad_yes
        x[7] = guestroom_no
        x[8] = guestroom_yes
        x[9] = basement_no
        x[10] = basement_yes
        x[11] = hotwaterheating_no
        x[12] = hotwaterheating_yes
        x[13] = airconditioning_no
        x[14] = airconditioning_yes
        x[15] = prefarea_no
        x[16] = prefarea_yes
        x[17] = dp[0]
        x[18] = dp[1]
        x[19] = dp[2]
        x[20] = dp[3]
        prediction=model.predict([x])
        output=round(prediction[0],2)
    return render_template('index.html',prediction_text="Your House Price is Rs.{}".format(output))
if __name__=="__main__":
    app.run(debug=True)                   
