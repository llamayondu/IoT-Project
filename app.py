from flask import Flask, render_template, redirect, url_for
from graph2image import fetch_plots
import execute

app = Flask(__name__)
channel_number = 2470056
secret_key = '6WA7QY0CC9HDX9UO'

@app.route('/')
def home():
    fetch_plots(channel_number,secret_key,'static/images/')
    return render_template('index.html')

@app.route('/on', methods=["POST"])
def switch_on_ac():
    print(f"{execute.talkback_id=}, {execute.key=}\n")
    execute.execute(execute.talkback_id, execute.key, 'TURN_ON') #ADDS TURN ON COMMAND TO THE QUEUE
    return redirect(url_for("home"))
    # return redirect(url_for("/"));

if __name__ == '__main__':
    app.run(debug=True)