from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # default response for Get method
    text = 'Flask API example version 0.2.0'
    if request.method == 'POST':
        # get text from form
        text = request.form.get('sometext')
        print(text)
        # format as json for api call
        data = {"sometext": text}
        try:
            # call the api
            if text == '':
                response = requests.get('http://localhost:5000/api')
                text = response.text
            else:
                response = requests.post('http://localhost:5000/api', json=data)
                text = response.text
        except:
            text = 'API call failed'
    return render_template('index2.html', output=text)

if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
