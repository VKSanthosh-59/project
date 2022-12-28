from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('NBClassifier.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('index.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')


@app.route('/predict', methods=['POST'])
def home():
    n = request.form['n']
    p = request.form['p']
    k = request.form['k']
    t = request.form['t']
    h = request.form['h']
    ph = request.form['ph']
    rf = request.form['rf']
    arr = np.array([[n, p, k, t,h, ph , rf]],dtype=float)
    pred = model.predict(arr)
    print(pred)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)

