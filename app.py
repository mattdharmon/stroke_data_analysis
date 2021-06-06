from flask import Flask, render_template, redirect, request
import pandas as pd
import tensorflow as tf
import numpy as np

app = Flask(__name__)

@app.before_first_request
def load_model():
   app.model = tf.keras.models.load_model('resources/model/stroke_data_analysis.h5')

@app.route("/", methods=['GET', 'POST'])
def index():
   if request.method == 'GET':
      form = {
         'age': None,
         'current_smoker': 1,
         'hypertension': 1,
         'bmi': None,
         'avg_glucose_level': None,
         'gender': 1
      }
      return render_template("./index.html", form=form, prediction=None)
   if request.method == 'POST':
      form = request.form.to_dict()

      # Prepare data for pridiction
      stroke_df = pd.DataFrame([form.values()], columns=form.keys())
      stroke_df['age'] =  pd.to_numeric(stroke_df['age'], downcast='float')
      stroke_df['bmi'] =  pd.to_numeric(stroke_df['bmi'], downcast='float')
      stroke_df['avg_glucose_level'] = pd.to_numeric(stroke_df['avg_glucose_level'], downcast='integer')
      stroke_df['current_smoker'] = pd.to_numeric(stroke_df['current_smoker'], downcast='integer')
      stroke_df['hypertension'] = pd.to_numeric(stroke_df['hypertension'], downcast='integer')
      
      # Set up encoded columns
      stroke_df['gender_Male'] = np.where(stroke_df['gender'] == 'Male', 1, 0)
      stroke_df['gender_Female'] = np.where(stroke_df['gender'] == 'Female', 1, 0)
      stroke_df['gender_Other'] = np.where(stroke_df['gender'] == 'Other', 1, 0)
      stroke_df.drop(columns=['gender'], inplace=True)

      # Make prediction
      prediction = app.model.predict(stroke_df)[0][0]
      print(prediction)
      # prediction = round(prediction * 100, 4)
      return render_template("./index.html", form=form, prediction=prediction)

# Start the app
if __name__ == "__main__":
   app.run()