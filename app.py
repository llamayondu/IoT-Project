from flask import Flask, render_template, request, redirect, flash
import json
import hashlib  # Import the hashlib library for password hashing

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)