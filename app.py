from flask import Flask, render_template, request, redirect, flash
from graph2image import fetch_plots

app = Flask(__name__)

@app.route('/')
def home():
    fetch_plots()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)