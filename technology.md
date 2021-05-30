# Technologies Used

## Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

## Database Storage
Mongo is the database we intend to use, and we will integrate Flask to display the data.

## Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. Our training and testing setup is a supervised learning model with overfitted data. In this way, we produce more false positives than false negatives. It is safer for us to diagnose someone who does not end up having a stroke than to not diagnose someone who actually has a stroke and then put their life at risk.  

## Dashboard
In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard. It will be hosted on a HTML page. We will send the data to this html page from python code contained in a file called ‘application.py’. We are also looking to make Tableau storyboards for both datasets.
