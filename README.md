# ml-iris-prediction-app
"A Flask-based API for predicting Iris flower species using a pre-trained machine learning model. Includes endpoints for making predictions and testing the API."
# ml-iris-app

This project implements a basic machine learning model using the Iris dataset with scikit-learn and deploys the model using Flask or FastAPI.

## Project Structure

```
ml-iris-app
├── src
│   ├── app.py          # Entry point of the application
│   ├── model.py        # Machine learning model implementation
│   ├── train.py        # Model training script
│   └── utils.py        # Utility functions
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ml-iris-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Training the Model

To train the model, run the following command:
```
python src/train.py
```
This will load the Iris dataset, train the model, and save it to disk for later use.

## Running the Application

To start the application, run:
```
python src/app.py
```
The application will be available at `http://127.0.0.1:8000` (or the default port for Flask/FastAPI).

## Making Predictions

Once the application is running, you can make predictions by sending a POST request to the `/predict` endpoint with the appropriate data format.

## License

This project is licensed under the MIT License.