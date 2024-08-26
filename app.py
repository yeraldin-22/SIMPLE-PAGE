from flask import Flask, render_template, url_for

servidor1 = Flask(__name__)

@servidor1.route('/inicio')
def home():
    return render_template('index.html')
if __name__=='__main__':
    servidor1.run(debug=True, port=5001)