Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
from flask import Flask ,render_template,url_for,request
import numpy as np 
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

# Home Route
@app.route('/')
def home():
	return render_template('home.html')

# prediction
@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [x for x in request.form.values()]
	print(int_feature)
	int_feature = [float(i) for i in int_feature]
	final_features = [np.array(int_feature)]
	prediction = model.predict(final_features)

	output = prediction
	print(output)

	return render_template('home.html',prediction_text= output)


if __name__ == "__main__":
	app.run(debug=True)