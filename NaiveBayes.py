import flask
import pickle
import pandas as pd


# Use pickle to load in the pre-trained model
with open(f'model/NBmodel.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')


# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def NaiveBayes():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('NaiveBayes.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        Bp = flask.request.form['Bp']
        Sg = flask.request.form['Sg']
        Al = flask.request.form['Al']
        Su = flask.request.form['Su']
        Rbc = flask.request.form['Rbc']
        Sc  = flask.request.form['Sc']
        Sod = flask.request.form['Sod']
        Pot = flask.request.form['Pot']
        Hemo = flask.request.form['Hemo']
        Wbcc = flask.request.form['Wbcc']
        Rbcc = flask.request.form['Rbcc']
        Htn = flask.request.form['Htn']
        # Make DataFrame for model
        input_variables = pd.DataFrame([[Bp,Sg,Al,Su,Rbc,Sc,Sod,Pot,Hemo,Wbcc,Rbcc,Htn]],
                                       columns=['Bp','Sg','Al','Su','Rbc','Sc','Sod','Pot','Hemo','Wbcc','Rbcc','Htn'],
                                       dtype=float,
                                       index=['input'])
                                        
         # Get the model's prediction
        prediction = model.predict(input_variables)[0]
                                        
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('NaiveBayes.html',
                                      original_input={'Bp':Bp,'Sg':Sg,'Al':Al,'Su':Su,'Rbc':Rbc,
                                                      'Sc':Sc,'Sod':Sod,'Pot':Pot,'Hemo':Hemo,'Wbcc':Wbcc,
                                                      'Rbcc':Rbcc,'Htn':Htn},
                                     result=prediction,)
                                        
                                        
                                        
if __name__ == '__main__':
    app.run(debug=True)