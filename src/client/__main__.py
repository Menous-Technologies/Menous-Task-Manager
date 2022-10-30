from flask import *

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "snehashish" and password == "snehashish":
            return "Lol"
        else:
            return render_template('login.html')

    return render_template('login.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('/home.html')

if __name__ == '__main__':
    app.run(debug=True)