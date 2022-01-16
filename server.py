# from re import X
# from turtle import color
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')          
@app.route('/<int:x>/<int:y>/<color1>')
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard(x=8, y=8, color1='red', color2='black'):

    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
