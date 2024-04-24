from flask import Flask, render_template, request, redirect, flash
from graph2image import fetch_plots

app = Flask(__name__)
channel_number = 2470056
secret_key = '6WA7QY0CC9HDX9UO'

@app.route('/')
def home():
    fetch_plots(channel_number,secret_key,'static/images/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)