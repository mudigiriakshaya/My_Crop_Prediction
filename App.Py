from flask import Flask,render_template,jsonify,request 
app=Flask(__name__)

@app.route('/')  #path for home 
def home():
    return render_template('home.html')  

@app.route('/Prediction')
def Prediction():
    return render_template('Prediction.html')

if __name__=='__main__':
    app.run() 



