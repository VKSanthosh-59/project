from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

if __name__== "__main__":
    app.run(debug=True)