from flask import Flask,render_template,request
import pickle


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods =['GET','POST'])
def predict():
    Classification = None
    if request.method == 'POST':
        SW= request.form['SW'] 
        print(SW)
        PW=request.form['PW']
        print(PW)
        SL=request.form['SL']
        print(SL)
        PL=request.form['PL']
        print(PL)

        model = pickle.load(open('model (2).pkl', 'rb'))
    

        Classification =  model.predict([[float(SW),float(PW),float(SL),float(PL)]])
        print(Classification)
    return render_template('prediction.html',Classification=Classification)

if __name__=='__main__':
    app.run()