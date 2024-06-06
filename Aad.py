from flask import *
import os, base64, sys, time
from pprint import pformat



def encode_string(text):
    encoded_text = '\u200D\u200B\uFEFF'.join(text)
    return encoded_text
    


def encoding(code):
        return "# Bybassed by Anti Ai Detector \n# Made by Abodx\n\n" + (encode_string(code))




print("Abodx..")
app = Flask(__name__)

@app.route('/encode', methods=['POST'])
def encode_text():
    text = request.form['textarea']
    encoded_text = encoding(text)
    return encoded_text

@app.route("/")
def home():
    
  return render_template('index.html')

  
if __name__ == '__main__':
  app.run("0.0.0.0", 9091)

