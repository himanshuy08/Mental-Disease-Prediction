from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the pre-trained machine learning model
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

    condition_templates = {
        0: 'anxiety.html',
        1: 'depression.html',
        2: 'loneliness.html',
        3: 'normal.html',
        4: 'stress.html',
    }

    condition_names = {
        0: 'Anxiety',
        1: 'Depression',
        2: 'Loneliness',
        3: 'Normal',
        4: 'Stress',
    }

    if res in condition_templates:
        condition_template = condition_templates[res]
        condition_name = condition_names[res]
        return render_template(condition_template, condition=condition_name)

if __name__ == "__main__":
    app.run()
