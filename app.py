from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)


def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value


@app.route('/', methods=['POST','GET'])
def index():
    pred = 0
    if request.method == 'POST':
        Stops = request.form['stops']
        Class = request.form['class']
        Duration = request.form['duration']
        Days_left = request.form['days_left']
        Airline = request.form['airline']
        Source = request.form['source']
        Destination = request.form['destination']
        Departure = request.form['departure']
        Arrival = request.form['arrival']
        
        feature_list = []
        feature_list.append(int(Stops))
        feature_list.append(float(Duration))
        feature_list.append(int(Days_left))
        feature_list.append(int(Class))
        
        Airline_list = ['AirAsia', 'Air_India', 'G0_FIRST', 'SpiceJet', 'Indigo', 'Vistara']
        Destination_list = ['Delhi', 'Kolkata', 'Mumbai', 'Chennai', 'Bangalore', 'Hydabad']
        Source_list = ['Delhi', 'Kolkata', 'Mumbai', 'Chennai', 'Bangalore', 'Hydabad']
        Departure_list = ['Morning', 'Afternoon', 'Evening', 'Night', 'Early_morning', 'Late_night']
        Arrival_list = ['Morning', 'Afternoon', 'Evening', 'Night', 'Early_morning', 'Late_night']
        
        def traverse(lst,value):
            for i in lst:
                if i == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        traverse(Airline_list,Airline)
        traverse(Destination_list,Destination)
        traverse(Source_list,Source)
        traverse(Departure_list,Departure)
        traverse(Arrival_list,Arrival)
        
        pred = prediction(feature_list)
        pred = np.round(pred[0])
        
    return render_template('index.html', pred=pred)

if __name__ == '__main__':
    app.run(debug=True)