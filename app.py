from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'index page'
    

if __name__ == "__main__":
    app.run()
    
