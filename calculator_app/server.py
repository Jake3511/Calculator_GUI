from flask import Flask, render_template
from waitress import serve 

app = Flask(__name__)

@app.route('/')

def calculator():
    return render_template('calculator.html')

if __name__ == '__main__':
    serve(app,host= "0.0.0.0", port= 49151) #run and then copy and past into browser- localhost:49151



    

