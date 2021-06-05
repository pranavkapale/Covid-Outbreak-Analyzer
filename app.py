import urllib.request
from flask import Flask, render_template, request, session, redirect
import json

app = Flask(__name__)
 


@app.route("/")
def index():

    #state data
    url = "https://api.rootnet.in/covid19-in/stats/latest"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    lis = list()
    for i in data['data']['regional']:
        lis.append(i['loc'])

    return render_template('index.html', lis = lis )
 

@app.route('/somework', methods=["GET", "POST"])
def somework():
    if request.method == "POST":
        statename = request.form.get("statename")
        statename = str(statename)
        # print(statename)
  
        url = "https://api.rootnet.in/covid19-in/stats/latest"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        reqdic = dict()
        for i in data['data']['regional']:
            abc = i['loc'] 
            abc = abc.split(" ")
            if abc[0] == statename:
                reqdic = i
        return render_template('showstatedata.html', reqdic = reqdic)

    return "hello"

@app.route("/notification")
def notification():
 
    #notification data
    url = "https://api.rootnet.in/covid19-in/notifications"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    notificationdict = dict()
    for i in data['data']['notifications']:
        abc = i['title']
        xyz = i['link']
        notificationdict[abc] = xyz

    return render_template('notification.html',  notificationdict=notificationdict)


@app.route("/testing")
def testing():

    url = "https://api.rootnet.in/covid19-in/stats/testing/history"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    lis = data['data']

    return render_template('testing.html',lis = lis)


@app.route("/beds")
def beds():

    url = "https://api.rootnet.in/covid19-in/hospitals/beds"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    lis = data['data']['regional']

    return render_template('beds.html', lis=lis)


@app.route("/contacts")
def contacts():

    url = "https://api.rootnet.in/covid19-in/contacts"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    lis = data['data']['contacts']['regional']

    return render_template('contacts.html', lis=lis)






if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
