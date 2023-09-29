import joblib
import numpy as np
from flask import Flask, render_template, request

loaded_model = joblib.load("Model/saved_model")

app = Flask(__name__)

@app.route('/')
def access():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def products():
    name = request.form.get('inputGroup-sizing-default')
    return render_template('pass.html', name=name)

@app.route('/uploader', methods=['POST'])
def getdata():
    feature = []
    for x in request.form.values():
        feature.append(int(x))
    arr = [np.array(feature, dtype=np.float32)]
    res = int(loaded_model.predict(arr))
    if res == 0:
        str = "You are suffering from anxiety\nYou need to seek psychological support"
    elif res == 1:
        str = "You are suffering from depression\nYou need to seek psychological support"
    elif res == 2:
        str = "You are suffering from loneliness\nSpeak to a counselor or spend some time with your loved ones"
    elif res == 3:  # Fixed the condition number
        str = "You are normal"
    elif res == 4:  # Fixed the condition number
        str = "You are stressed\nPractice yoga or talk to a counselor"
    return render_template('predict.html', label=str)

if __name__ == "__main__":
    app.run()
