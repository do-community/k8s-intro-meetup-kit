from flask import Flask
import urllib.parse

app = Flask(__name__)

@app.route('/sample/')
def hello_world():
   s = urllib.parse.quote('https://github.com/BoazHalter/k8s-hello-world')
   return 'https://'+s'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
