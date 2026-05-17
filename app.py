import streamlit as st
import pickle
import numpy as np


@st.cache_resource
def load_model():
    with open("model/predictor.pickle", "rb") as file:
        model = pickle.load(file)
    return model


model = load_model()


def add_one_hot(feature_list, option_list, selected_value):
    for item in option_list:
        if item == selected_value:
            feature_list.append(1)
        else:
            feature_list.append(0)


st.title("Flight Price Predictor")
st.write("Enter flight details below to predict the ticket price.")


stops = st.selectbox("Number of Stops", [0, 1, 2])
flight_class = st.selectbox("Class", ["Economy", "Business"])

duration = st.number_input("Duration in hours", min_value=0.0, value=2.0, step=0.1)
days_left = st.number_input("Days Left Before Travel", min_value=1, value=10, step=1)

airline = st.selectbox(
    "Airline",
    ["AirAsia", "Air_India", "G0_FIRST", "SpiceJet", "Indigo", "Vistara"]
)

source = st.selectbox(
    "Source City",
    ["Delhi", "Kolkata", "Mumbai", "Chennai", "Bangalore", "Hydabad"]
)

destination = st.selectbox(
    "Destination City",
    ["Delhi", "Kolkata", "Mumbai", "Chennai", "Bangalore", "Hydabad"]
)

departure = st.selectbox(
    "Departure Time",
    ["Morning", "Afternoon", "Evening", "Night", "Early_morning", "Late_night"]
)

arrival = st.selectbox(
    "Arrival Time",
    ["Morning", "Afternoon", "Evening", "Night", "Early_morning", "Late_night"]
)


if st.button("Predict Price"):
    feature_list = []

    feature_list.append(int(stops))
    feature_list.append(float(duration))
    feature_list.append(int(days_left))

    if flight_class == "Economy":
        feature_list.append(0)
    else:
        feature_list.append(1)

    airline_list = ["AirAsia", "Air_India", "G0_FIRST", "SpiceJet", "Indigo", "Vistara"]
    destination_list = ["Delhi", "Kolkata", "Mumbai", "Chennai", "Bangalore", "Hydabad"]
    source_list = ["Delhi", "Kolkata", "Mumbai", "Chennai", "Bangalore", "Hydabad"]
    departure_list = ["Morning", "Afternoon", "Evening", "Night", "Early_morning", "Late_night"]
    arrival_list = ["Morning", "Afternoon", "Evening", "Night", "Early_morning", "Late_night"]

    add_one_hot(feature_list, airline_list, airline)
    add_one_hot(feature_list, destination_list, destination)
    add_one_hot(feature_list, source_list, source)
    add_one_hot(feature_list, departure_list, departure)
    add_one_hot(feature_list, arrival_list, arrival)

    prediction = model.predict([feature_list])
    predicted_price = np.round(prediction[0])

    st.success(f"Predicted Flight Price: ₹ {predicted_price:,.0f}")
