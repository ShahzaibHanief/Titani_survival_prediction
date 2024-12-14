from flask import Flask, render_template, request
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Load options dynamically from the CSV file
def load_options(csv_file):
    data = pd.read_csv(csv_file)
    # Extract unique values for each dropdown field
    options = {
        'Pclass': sorted(data['Pclass'].unique().tolist()),
        'Sex': sorted(data['Sex'].unique().tolist()),
        'Family_type': sorted(data['Family_type'].unique().tolist()),
        'AgeGroup': sorted(data['AgeGroup'].unique().tolist()),
        'Title': sorted(data['Title'].unique().tolist())
    }
    return options

# Route to render the home page
@app.route('/')
def home():
    # Load dropdown options from the CSV file
    options = load_options('select_titanic_field.csv')
    return render_template('index.html', options=options)

# Route to handle the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    Pclass = request.form['Pclass']
    Sex = request.form['Sex']
    Family_type = request.form['Family_type']
    AgeGroup = request.form['AgeGroup']
    FarePerPerson = request.form['FarePerPerson']
    Title = request.form['Title']
    MeanFareByEmbarked = request.form['MeanFareByEmbarked']

    # Prepare the input data for prediction
    input_data = pd.DataFrame([{
        'Pclass': Pclass,
        'Sex': Sex,
        'Family_type': Family_type,
        'AgeGroup': AgeGroup,
        'FarePerPerson': FarePerPerson,
        'Title': Title,
        'MeanFareByEmbarked': MeanFareByEmbarked
    }])

    # Dummy prediction logic (replace with actual model logic)
    result = "Survived 😊" if int(Pclass) == 1 else "Did not survive 😢"

    # Reload options for the dropdown fields
    options = load_options('select_titanic_field.csv')

    # Render the template with the result and options
    return render_template('index.html', options=options, prediction_text=f'The passenger {result}.')

if __name__ == "__main__":
    app.run(debug=True)
