from flask import Flask, render_template
import webbrowser
import requests
import os
import time

from werkzeug.utils import redirect

####################

sv_port = "80"
sv_hostip = "127.0.0.1"


app = Flask(__name__)

os.system("clear")
os.system("cls")

#####################

# <img> helpful i am dumb
@app.route("/")
def get_doggo():
    req = requests.get("https://api.thedogapi.com/v1/images/search")
    req1 = req.text.split('"url":"')
    url_cleaned = req1[1].split('"')
    url_to_open1 = str(url_cleaned).replace("[", "").replace("'", "").split("'")
    url_to_open2 = url_to_open1[0].split(",")
    print(str(url_cleaned[0]))
    return render_template("index.htm", iframesrc=url_to_open2[0])

if __name__ =='__main__':
        #os.system("clear")
        #os.system("cls")
        time.sleep(0.1)
        app.run(debug=True, host=sv_hostip, port=sv_port)