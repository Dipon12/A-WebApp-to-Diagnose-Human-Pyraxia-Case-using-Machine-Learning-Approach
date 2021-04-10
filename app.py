import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]

    features = [int(x) for x in request.form.values()]
    prediction = model.predict([features])

    my_dic = {1:"Dengue",2:"Malaria",3:"Typhoid"}
    #output = round(prediction[0], 2)
    output = my_dic[prediction[0]]
    print(output)

    return render_template('index.html', prediction_text='Patient is Diagnosed with {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([list(data.values())])

    my_dic = {1:"Dengue",2:"Malaria",3:"Typhoid"}
    output = my_dic[prediction[0]]

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)