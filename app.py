from flask import Flask,render_template
app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'hello,world'

@app.route('/products')
def products():
    return 'this is a products'



if __name__=="__main__":
    app.run(debug=True,port=8000)