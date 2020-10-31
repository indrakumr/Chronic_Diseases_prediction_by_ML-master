import flask
import pickle
import pandas as pd


# Use pickle to load in the pre-trained model
with open(f'model/Decisionmodel.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

def multiply(Age,Sex,Sc):
    a=int(Age)
    b=int(Sex)
    c=float(Sc)
    if b==1:
        m=(186*(c**-1.154)*(a**-0.203));
        ca=fun(m)
        return (ca,m)
    elif b==0:
        m=(186*(c**-1.154)*(a**-0.203)*0.742);
        cb=fun(m)
        return (cb,m)
    
    
def fun(m):
    if(m>90):
        return ("kidney is normal in conditon")
    elif(m >60 and m<90 ):
        return( "kidney is little bit damage")
    elif(m >30 and m<60 ):
        return( "moderate kidney damage")
    elif(m >15 and m<30 ):
        return("sereve kidney damage")
    elif(m <15 ):
        return("the kidney are closed to failure orhave ready failed")
def sex(Sex):
    if(Sex==1):
        se='Male'
        return se
    else:
        se='Female'
        return se
    
# Set up the main route

@app.route('/', methods=['GET', 'POST'])
def Random():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('Decisionmodel.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        Age= flask.request.form['Age']
        Sex= flask.request.form['Sex']
        Bp = flask.request.form['Bp']
        Sg = flask.request.form['Sg']
        Al = flask.request.form['Al']
        Su = flask.request.form['Su']
        Rbc = flask.request.form['Rbc']
        Bu = flask.request.form['Bu']
        Sc  = flask.request.form['Sc']
        Sod = flask.request.form['Sod']
        Pot = flask.request.form['Pot']
        Hemo = flask.request.form['Hemo']
        Wbcc = flask.request.form['Wbcc']
        Rbcc = flask.request.form['Rbcc']
        Htn = flask.request.form['Htn']
        # Make DataFrame for model
        input_variables = pd.DataFrame([[Bp,Sg,Al,Su,Rbc,Bu,Sc,Sod,Pot,Hemo,Wbcc,Rbcc,Htn]],
                                       columns=['Bp','Sg','Al','Su','Rbc','Bu','Sc','Sod','Pot','Hemo','Wbcc','Rbcc','Htn'],
                                       dtype=float,
                                       index=['input'])
                                        
         # Get the model's prediction
        prediction = model.predict(input_variables)[0]
        demo=multiply(Age,Sex,Sc)
        se=sex(Sex)
        
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('Decisionmodel.html',
                                      original_input={'Age':Age,'Sex':se,'Bp':Bp,'Sg':Sg,'Al':Al,'Su':Su,'Rbc':Rbc,'Bu':Bu,
                                                      'Sc':Sc,'Sod':Sod,'Pot':Pot,'Hemo':Hemo,'Wbcc':Wbcc,
                                                      'Rbcc':Rbcc,'Htn':Htn},
                                     result=prediction,demo=demo,)
                                        
                                        
                                        
if __name__ == '__main__':
    app.run(debug=True)