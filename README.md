# Flight Price Predictor ✈️

A machine learning-powered web application that predicts flight prices based on various flight parameters. Built with Flask and scikit-learn, this project uses a trained regression model to estimate flight prices accurately.

## 🌐 Live Demo

Try the application here: [Flight Price Predictor App](https://flight-price-predictor-32w9.onrender.com)

## 📋 Features

- **Real-time Flight Price Prediction**: Get instant price estimates based on flight details
- **Comprehensive Input Parameters**:
  - Number of stops (0-5)
  - Flight duration (in minutes)
  - Days left before departure
  - Travel class (Economy, Business)
  - Airline selection (AirAsia, Air India, GO_FIRST, SpiceJet, Indigo, Vistara)
  - Source city (Delhi, Kolkata, Mumbai, Chennai, Bangalore, Hyderabad)
  - Destination city (Delhi, Kolkata, Mumbai, Chennai, Bangalore, Hyderabad)
  - Departure time (Morning, Afternoon, Evening, Night, Early Morning, Late Night)
  - Arrival time (Morning, Afternoon, Evening, Night, Early Morning, Late Night)

## 🛠️ Technologies Used

- **Python** - Programming language
- **Flask** - Web framework for Python
- **scikit-learn** - Machine learning library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Pickle** - Model serialization
- **Gunicorn** - WSGI HTTP Server
- **gdown** - Google Drive file downloader

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Dhanushka0626/Flight-price-predictor.git
cd Flight-price-predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Run Locally

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Fill in the flight details and click "Predict Price" to get the estimated fare

### Deployment

The application is configured for deployment on Render using the provided `render.yaml` configuration file. The deployment automatically:
- Installs all dependencies
- Runs the app with Gunicorn
- Sets production environment variables

## 📁 Project Structure

```
Flight-price-predictor/
├── app.py                 # Main Flask application
├── Main.ipynb            # Jupyter notebook with model development
├── requirements.txt      # Python dependencies
├── render.yaml          # Render deployment configuration
├── Clean_Dataset.csv    # Training dataset
├── predictor.pickle     # Pre-trained ML model (downloaded from Google Drive)
├── templates/
│   └── index.html       # Web interface template
├── static/              # Static files (CSS, JS, images)
├── README.md           # Project documentation
├── LICENSE             # MIT License
└── .gitignore         # Git ignore rules
```

## 💡 How It Works

1. **Input Collection**: User provides flight details through the web interface
2. **Feature Engineering**: The app processes and encodes categorical features (airline, routes, times) into one-hot encoded vectors
3. **Feature Preparation**: All input features are formatted as a list
4. **Model Prediction**: The trained scikit-learn model predicts the flight price
5. **Result Display**: The predicted price is rounded and displayed to the user

## 📊 Input Features

The model considers the following features:
- **Stops** (integer): Number of flight stops
- **Duration** (float): Total flight duration in minutes
- **Days Left** (integer): Number of days before departure
- **Class** (integer): Flight class (encoded)
- **Airline** (categorical): One-hot encoded airline selection (6 options)
- **Destination** (categorical): One-hot encoded destination city (6 options)
- **Source** (categorical): One-hot encoded source city (6 options)
- **Departure Time** (categorical): One-hot encoded departure time (6 options)
- **Arrival Time** (categorical): One-hot encoded arrival time (6 options)

**Total Features**: 38 input features after one-hot encoding

## 📝 Model Details

- **Algorithm**: Regression model trained using scikit-learn
- **Training Data**: Clean_Dataset.csv with historical flight prices
- **Output**: Flight price prediction in the local currency
- **Format**: Serialized using pickle and stored on Google Drive
- **Model Loading**: Automatically downloaded from Google Drive when app starts

## ⚙️ Requirements

See `requirements.txt` for the complete list:
```
Flask
numpy
pandas
scikit-learn
gdown
gunicorn
```

## 📊 Dataset

The model was trained on `Clean_Dataset.csv` which contains:
- Flight details and attributes
- Historical pricing information
- Over 10,000+ flight records
- Cleaned and preprocessed data

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dhanushka0626**
- GitHub: [@Dhanushka0626](https://github.com/Dhanushka0626)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For issues or questions about the project, please open an issue on the [GitHub Issues](https://github.com/Dhanushka0626/Flight-price-predictor/issues) page.

## 🔍 Model Development

The complete model development process, including:
- Data exploration and analysis
- Feature engineering
- Model training and evaluation
- Hyperparameter tuning

Can be found in the `Main.ipynb` Jupyter notebook.

---

**Note**: This project uses machine learning to predict flight prices based on historical data. Predictions are estimates and may vary based on actual market conditions, seasonal variations, and airline pricing strategies.
